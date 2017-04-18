# Wizard Simulator 20XX
#
import logging
logging.basicConfig(filename='day22.log', filemode='w', level=logging.DEBUG)

#
## Finally:
# If the player won, sum mana cost and keep track of minimum mana required (our output)
# Try 10000 random fights to determine minimum?

class Spell(object):
    def __init__(self, attacker, target):
        self.attacker = attacker
        self.target = target

    def cast(self):
        logging.debug("Attacker cast " + self.__class__.__name__)
        self.attacker.mana -= self.__class__.cost

    def __repr__(self):
        return self.name

class MagicMissileSpell(Spell):
    cost = 53

    def cast(self):
        super(self.__class__, self).cast()
        self.target.hitpoints -= 4

class DrainSpell(Spell):
    cost = 73

    def cast(self):
        super(self.__class__, self).cast()
        self.target.hitpoints -= 2
        self.attacker.hitpoints += 2

class Effect(object):
    def __init__(self, attacker, target):
        logging.debug("Effect " + self.__class__.__name__ + " started")
        self.attacker = attacker
        self.target = target
        self.turns_remaining = self.__class__.turns
        self.attacker.mana -= self.__class__.cost

    def apply(self):
        self.turns_remaining -= 1
        logging.debug("Effect {} applied; has {} turns reminaing".format(self.__class__.__name__, self.turns_remaining))

    def wear_off(self):
        pass

    def is_wearing_off(self):
        return self.turns_remaining == 0

class ShieldEffect(Effect):
    cost = 113
    turns = 6

    def first_turn(self):
        self.attacker.armor += 7

    def apply(self):
        if self.__class__.turns == self.turns_remaining:
            self.first_turn()
        super(self.__class__, self).apply()

    def wear_off(self):
        self.attacker.armor -= 7

class PoisonEffect(Effect):
    cost = 173
    turns = 6

    def apply(self):
        super(self.__class__, self).apply()
        self.target.hitpoints -= 3

class RechargeEffect(Effect):
    cost = 229
    turns = 5

    def apply(self):
        super(self.__class__, self).apply()
        self.attacker.mana += 101

class MagicManager():
    def __init__(self):
        self.active_effects = []
        self.magic_used = []

    def cost(self):
        return sum(magic.cost for magic in self.magic_used)

    def tick(self):
        # Apply active effects
        # Remove any effects that have worn out
        for effect in self.active_effects:
            effect.apply()
            if effect.is_wearing_off():
                effect.wear_off()
                self.active_effects.remove(effect)

    def apply(self, magic):
        if issubclass(magic.__class__, Effect):
            self.active_effects.append(magic)
        else:
            magic.cast()

        self.magic_used.append(magic.__class__)

    ## Choosing which spells to cast, and when:
    # Approach: Let's try random selection!
    # - Repeated cast of the same spell are fine
    # - Player cannot cast an effect already in progress
    # - Only choose spells player can afford
    # We just need to select one at random from (all available spells - effects in progress)
    def choose_magic(self, available_mana):
        import random
        return random.choice(self.magic_options(available_mana))

    def magic_options(self, available_mana):
        return [magic for magic in self.available_spells_and_effects()
                if magic.cost <= available_mana]

    def active_effects_by_class(self):
        return [effect.__class__ for effect in self.active_effects]

    def available_spells_and_effects(self):
        return [magic for magic in ALL_SPELLS_AND_EFFECTS
                if magic not in self.active_effects_by_class()]


class NPC():
    def __init__(self, hitpoints, **kwargs):
        self.hitpoints = hitpoints
        self.damage = kwargs.pop('damage', 0)
        self.armor = kwargs.pop('armor', 0)
        self.mana = kwargs.pop('mana', 0)
        self.magic_manager = kwargs.pop('magic_manager', 0)

    def set_target(self, target):
        self.target = target

class Warrior(NPC):
    # Warrior attacks for (their damage - player's armor) (min 1)
    def fight(self):
        damage = max(1, self.damage - self.target.armor) 
        logging.debug("Boss deals {} damage".format(damage))
        self.target.hitpoints -= damage

    def has_enough_mana(self):
        return True
 
class Wizard(NPC):
    # Wizard casts a spell or effect every turn.
    #   - Mana is deducted immediately
    #   - Spells have immediate impact
    def fight(self):
        magic = self.magic_manager.choose_magic(self.mana)(self, self.target)
        self.magic_manager.apply(magic)

    def has_enough_mana(self):
        return self.mana >= MIN_MANA


class Fight():
    def __init__(self, attacker, target, magic_manager):
        self.attacker = self.wizard = attacker
        self.target = self.boss = target
        self.magic_manager = magic_manager
        self.winner = None
        self.summary = ""

    def go(self):
        while True:
            if self.determine_winner():
                break

            self.summarize_fight()

            self.magic_manager.tick()

            if not self.attacker.has_enough_mana():
                self.winner = self.target
                break

            self.attacker.fight()

            # Swap roles
            self.target, self.attacker = self.attacker, self.target

    def summarize_fight(self):
        logging.debug("-- " + self.attacker.__class__.__name__ + "'s turn --")
        self.summarize_npc(self.attacker)
        self.summarize_npc(self.target)

    def summarize_npc(self, npc):
        logging.debug("{} has {} hitpoints; {} damage; {} armor; {} mana.".format(
            npc.__class__.__name__, npc.hitpoints, npc.damage, npc.armor, npc.mana
        ))

    def determine_winner(self):
        if not self.winner:
            if self.boss.hitpoints <= 0:
                self.winner = self.boss
            if self.wizard.hitpoints <= 0:
                self.winner = self.wizard
        return self.winner

BOSS_HITPOINTS = 51
BOSS_DAMAGE = 9
MY_HITPOINTS = 50
MY_MANA = 500
MIN_MANA = 53
ALL_SPELLS_AND_EFFECTS = vars()['Spell'].__subclasses__() + vars()['Effect'].__subclasses__()

def main():
    min_cost = 100000
    for i in range(10000):
        logging.debug("------- New fight {} ---------".format(i))
        magic_manager = MagicManager()
        boss = Warrior(BOSS_HITPOINTS, damage=BOSS_DAMAGE)
        me = Wizard(MY_HITPOINTS, mana=MY_MANA, magic_manager=magic_manager)
        boss.set_target(me)
        me.set_target(boss)
        fight = Fight(me, boss, magic_manager)
        fight.go()
        if fight.winner == me:
            cost = magic_manager.cost()
            logging.debug("Player wins fight {} with cost {}.".format(i, cost))
            if cost < min_cost:
                min_cost = cost
        else:
            logging.debug("Player wins fight {}.".format(i))
    print min_cost

if __name__ == '__main__':
    main()
