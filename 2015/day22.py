# i Wizard Simulator 20XX
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
ENABLE_LOGGING = False


class Spell(object):

    def __init__(self, attacker, target):
        self.attacker = attacker
        self.target = target

    def cast(self):
        logging.debug(
            "Wizard casts {} costing {}".format(
                self.__class__.__name__, self.__class__.cost
            )
        )
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
        self.attacker.mana -= self.__class__.cost

    def begin(self):
        pass

    def wear_off(self):
        pass

    def run(self):
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

    def run(self):
        self.target.hitpoints -= 3


class RechargeEffect(Effect):
    cost = 229
    turns = 5

    def run(self):
        self.attacker.mana += 101


class NPC(object):

    def __init__(self, hitpoints, **kwargs):
        self.hitpoints = hitpoints
        self.damage = kwargs.pop("damage", 0)
        self.armor = kwargs.pop("armor", 0)
        self.mana = kwargs.pop("mana", 0)

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
        self.magic_chooser = self.MagicChooser()
        self.effect_runner = self.EffectRunner()

    # Wizard casts a spell or effect every turn.
    # - Mana is deducted immediately
    # - Spells have immediate impact
    # - Effects do not
    def fight(self, target):
        self.choose_magic(
            self.magic_chooser.next_magic(
                self.mana, self.effect_runner.active_effects_by_class()
            )(self, target)
        )

    def choose_magic(self, magic):
        if issubclass(magic.__class__, Effect):
            self.effect_runner.add(magic)
        else:
            magic.cast()

    def pre_fight(self):
        self.effect_runner.run()

    def mana_spent(self):
        return self.magic_chooser.cost()

    def magic_used(self):
        return self.magic_chooser.magic_used

    def can_fight(self):
        return self.mana >= MIN_MANA

    class MagicChooser:
        ALL_MAGIC = Spell.__subclasses__() + Effect.__subclasses__()

        def __init__(self):
            self.magic_used = []

        def cost(self):
            return sum(magic.cost for magic in self.magic_used)

        ## Choosing which spells to cast, and when:
        # - Repeated cast of the same spell are fine
        # - Player cannot cast an effect already in progress
        # - Only choose spells player can afford
        def next_magic(self, available_mana, active_effects):
            import random

            magic = random.choice(
                [
                    magic
                    for magic in self.magic_options(available_mana)
                    if magic not in active_effects
                ]
            )
            self.magic_used.append(magic)
            return magic

        def magic_options(self, available_mana):
            return [
                magic
                for magic in self.__class__.ALL_MAGIC
                if magic.cost <= available_mana
            ]

    class EffectRunner:

        def __init__(self):
            self.active_effects = {}

        def add(self, effect):
            self.active_effects[effect] = effect.turns

        def apply(self, effect):
            if effect.turns == self.active_effects[effect]:
                effect.begin()
            self.active_effects[effect] -= 1
            effect.run()
            logging.debug(
                "Effect {} applied; has {} turns reminaing".format(
                    effect.__class__.__name__, self.active_effects[effect]
                )
            )

        def run(self):
            # Apply active effects and remove any effects that have worn out
            for effect in self.active_effects.keys():
                self.apply(effect)
                if self.active_effects[effect] == 0:
                    effect.wear_off()
                    del self.active_effects[effect]

        def active_effects_by_class(self):
            return [effect.__class__ for effect in self.active_effects]


class Fight:

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
            logging.debug(
                "{} has {} hitpoints; {} damage; {} armor; {} mana.".format(
                    npc.__class__.__name__,
                    npc.hitpoints,
                    npc.damage,
                    npc.armor,
                    npc.mana,
                )
            )

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
    for i in range(100000):
        logging.debug("------- New fight ---------")
        boss = Warrior(BOSS_HITPOINTS, damage=BOSS_DAMAGE)
        me = Wizard(MY_HITPOINTS, mana=MY_MANA)
        fight = Fight(me, boss).go()
        if fight.winner == me:
            min_cost = min(me.mana_spent(), min_cost)
            logging.debug("Player wins fight with cost {}.".format(min_cost))
        else:
            logging.debug("Boss wins fight.")
    print(min_cost)


if __name__ == "__main__":
    if ENABLE_LOGGING:
        logging.basicConfig(filename="day22.log", filemode="w", level=logging.DEBUG)
    main()
