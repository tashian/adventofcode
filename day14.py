# Reindeer Olympics
# http://adventofcode.com/2015/day/14
# 

import re

class Reindeer(object):
    def __init__(self, name, speed, fly_interval, rest_interval):
        self.name = name
        self.speed = speed
        self.fly_interval = fly_interval
        self.rest_interval = rest_interval
        self.flying = True
        self.current_interval = self.fly_interval
        self.distance = 0
        self.tick_count = 0

    def rest(self):
        self.flying = False
        self.current_interval = self.rest_interval

    def takeoff(self):
        self.flying = True
        self.current_interval = self.fly_interval

    def tick(self):
        self.tick_count += 1

        if self.current_interval == 0:
            if self.flying:
                self.rest()
            else:
                self.takeoff()

        self.current_interval -= 1

        if self.flying:
           self.distance += self.speed


def day14(reindeer):
    [[r.tick() for r in reindeer] for i in range(1, 2504)]
    print [[r.name, r.distance] for r in reindeer]


LINE_FORMAT = re.compile(
        r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'
)

with open('day14.txt') as f:
    reindeer = []
    for line in f:
        matches = LINE_FORMAT.match(line)
        name, speed, fly_interval, rest_interval = matches.groups()
        reindeer.append(Reindeer(name, int(speed), int(fly_interval), int(rest_interval)))
    day14(reindeer)

