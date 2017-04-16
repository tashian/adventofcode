import unittest

class Player():
    def __init__(self, hitpoints, damage = 0, armor = 0):
        self.hitpoints = hitpoints
        self.armor = armor
        self.damage = damage

    def wield(self, item):
        self.armor += item.armor
        self.damage += item.damage

    def attack(self, defender):
        defender.hitpoints -= max(1, self.damage - defender.armor)

class Fight():
    def __init__(self, player1, player2):
        self.attacker = player1
        self.defender = player2
        self.winner = None

    def go(self, attacker_eq = []):
        for item in attacker_eq:
            self.attacker.wield(item)
        while not self.winner:
            self.attacker.attack(self.defender)
            if self.defender.hitpoints <= 0:
                self.winner = self.attacker
            elif self.attacker.hitpoints <= 0:
                self.winner = self.defender
            self.swap_roles()

    def swap_roles(self):
        self.attacker, self.defender = self.defender, self.attacker

class Item():
    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

    def __repr__(self):
        return self.name

# Choose one weapon
WEAPONS = [
        Item('Dagger',     8, 4, 0),
        Item('Shortsword', 10, 5, 0),
        Item('Warhammer',  25, 6, 0),
        Item('Longsword',  40, 7, 0),
        Item('Greataxe',   74, 8, 0)
]

# Choose one armor
ARMOR = [
        Item('No Armor',    0, 0, 0),
        Item('Leather',    13, 0, 1),
        Item('Chainmail',  31, 0, 2),
        Item('Splintmail', 53, 0, 3),
        Item('Bandedmail', 75, 0, 4),
        Item('Platemail', 102, 0, 5)
]

# Choose 1-2 distinct rings
RINGS = [
        Item('No Ring',     0, 0, 0), 
        Item('D+1',        25, 1, 0), 
        Item('D+2',        50, 2, 0), 
        Item('D+3',       100, 3, 0), 
        Item('A+1',        20, 0, 1), 
        Item('A+2',        40, 0, 2), 
        Item('A+3',        80, 0, 3)
]

BOSS_HITPOINTS = 103
BOSS_DAMAGE = 9
BOSS_ARMOR = 2
MY_HITPOINTS = 100

def main():
    min_cost_to_win = float('inf')
    max_cost_to_lose = 0
    for eq in eq_options():
        boss = Player(BOSS_HITPOINTS, BOSS_DAMAGE, BOSS_ARMOR)
        me = Player(MY_HITPOINTS)
        fight = Fight(me, boss)
        fight.go(eq)
        cost = sum(item.cost for item in eq)
        # print "I won." if fight.winner == me else "Boss won."
        # print "I wielded", eq, "at a cost of", cost
        if fight.winner == me and cost < min_cost_to_win:
            min_cost_to_win = cost
        if fight.winner == boss and cost > max_cost_to_lose:
            max_cost_to_lose = cost
    print min_cost_to_win, max_cost_to_lose

def eq_options():
    # Glad there's only a handful.
    for w in WEAPONS:
        for a in ARMOR:
            for r1 in RINGS:
                for r2 in RINGS:
                    if r1 != r2:
                        yield [w, a, r1, r2]


class TestFight(unittest.TestCase):
    def test_fight(self):
        player = Player(7, 5, 5)
        boss = Player(12, 7, 2)
        fight = Fight(player, boss)
        fight.go()
        self.assertEqual(fight.winner, player)

if __name__ == '__main__':
    main()
    unittest.main()
