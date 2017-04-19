# Wizard Simulator 20XX
#
# Rather than figuring out the optimal pattern of magic to apply,
# my approach is to try 100000 random fights to determine minimum mana.
# 
import logging

BOSS_HITPOINTS = 51
BOSS_DAMAGE = 9
MY_HITPOINTS = 50
MY_MANA = 500
MIN_MANA = 53
ENABLE_PART_TWO = True
ENABLE_LOGGING = True

class Spell(object):
    def __init__(self, attacker, target):
        self.attacker = attacker
        self.target = target

    def cast(self):
        logging.debug("Wizard casts {} costing {}".format(self.__class__.__name__, self.__class__.cost))
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

    def begin(self):
        pass

    def apply(self):
        if self.__class__.turns == self.turns_remaining:
            self.begin()
        self.turns_remaining -= 1
        logging.debug("Effect {} applied; has {} turns reminaing".format(self.__class__.__name__, self.turns_remaining))

    def wear_off(self):
        pass

    def is_wearing_off(self):
        return self.turns_remaining == 0

class ShieldEffect(Effect):
    cost = 113
    turns = 6

    def begin(self):
        self.attacker.armor += 7

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

class NPC(object):
    def __init__(self, hitpoints, **kwargs):
        self.hitpoints = hitpoints
        self.damage = kwargs.pop('damage', 0)
        self.armor = kwargs.pop('armor', 0)
        self.mana = kwargs.pop('mana', 0)

    def pre_fight(self):
        pass

    def can_fight(self):
        return True

    def mana_spent(self):
        return 0

class Warrior(NPC):
    # Warrior attacks for (their damage - player's armor) (min 1)
    def fight(self, target):
        damage = max(1, self.damage - target.armor) 
        logging.debug("Boss deals {} damage".format(damage))
        target.hitpoints -= damage

class Wizard(NPC):
    def __init__(self, hitpoints, **kwargs):
        super(self.__class__, self).__init__(hitpoints, **kwargs)
        self.magic_manager = self.MagicManager()

    # Wizard casts a spell or effect every turn.
    # - Mana is deducted immediately
    # - Spells have immediate impact
    # - Effects do not
    def fight(self, target):
        self.magic_manager.start(
            self.magic_manager.next_magic(self.mana)(self, target)
        )

    def pre_fight(self):
        self.magic_manager.apply_effects()

    def mana_spent(self):
        return self.magic_manager.cost()

    def can_fight(self):
        return self.mana >= MIN_MANA

    class MagicManager():
        ALL_MAGIC = Spell.__subclasses__() + Effect.__subclasses__()

        def __init__(self):
            self.active_effects = []
            self.magic_used = []

        def cost(self):
            return sum(magic.cost for magic in self.magic_used)

        def apply_effects(self):
            # Apply active effects and remove any effects that have worn out
            for effect in self.active_effects:
                effect.apply()
                if effect.is_wearing_off():
                    effect.wear_off()
                    self.active_effects.remove(effect)

        def start(self, magic):
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
        def next_magic(self, available_mana):
            import random
            return random.choice(self.magic_options(available_mana))

        def magic_options(self, available_mana):
            return [magic for magic in self.available_spells_and_effects()
                    if magic.cost <= available_mana]

        def active_effects_by_class(self):
            return [effect.__class__ for effect in self.active_effects]

        def available_spells_and_effects(self):
            return [magic for magic in self.__class__.ALL_MAGIC
                    if magic not in self.active_effects_by_class()]


class Fight():
    def __init__(self, player, boss):
        self.attacker = self.player = player
        self.target = self.boss = boss
        self.winner = None

    def go(self):
        while True:
            if ENABLE_PART_TWO and self.attacker == self.player:
                self.player.hitpoints -= 1

            self.log_summary()
            self.attacker.pre_fight()
            self.target.pre_fight()

            if self.determine_winner():
                break

            if not self.attacker.can_fight():
                self.winner = self.target
                break

            self.attacker.fight(self.target)

            self.target, self.attacker = self.attacker, self.target
        return self

    def log_summary(self):
        def summarize_npc(npc):
            logging.debug("{} has {} hitpoints; {} damage; {} armor; {} mana.".format(
                npc.__class__.__name__, npc.hitpoints, npc.damage, npc.armor, npc.mana
            ))

        logging.debug("-- " + self.attacker.__class__.__name__ + "'s turn --")
        summarize_npc(self.attacker)
        summarize_npc(self.target)

    def determine_winner(self):
        if not self.winner:
            if self.boss.hitpoints <= 0:
                self.winner = self.player
            if self.player.hitpoints <= 0:
                self.winner = self.boss
        return self.winner

def main():
    min_cost = 100000
    for i in range(10000):
        logging.debug("------- New fight ---------")
        boss = Warrior(BOSS_HITPOINTS, damage=BOSS_DAMAGE)
        me = Wizard(MY_HITPOINTS, mana=MY_MANA)
        fight = Fight(me, boss).go()
        if fight.winner == me:
            cost = me.mana_spent()
            logging.debug("Player wins fight with cost {}.".format(cost))
            if cost < min_cost:
                min_cost = cost
        else:
            logging.debug("Boss wins fight.")
    print min_cost

if __name__ == '__main__':
    if ENABLE_LOGGING:
        logging.basicConfig(filename='day22.log', filemode='w', level=logging.DEBUG)
    main()
