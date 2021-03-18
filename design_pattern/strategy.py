""" Strategy Pattern
"""
from __future__ import annotations
from abc import ABC, abstractmethod
import random


class Hand(object):
    guu = 0
    cho = 1
    paa = 2
    hands = {
        guu: "guu",
        cho: "cho",
        paa: "paa",
    }

    def __init__(self, handvalue: int):
        self.handvalue = handvalue

    @classmethod
    def get_hand(cls, handvalue: int) -> Hand:
        return cls(handvalue)

    def is_stronger_than(self, h: Hand) -> bool:
        return self.fight(h)

    def is_weaker_than(self, h: Hand) -> bool:
        return self.fight(h)

    def fight(self, h: Hand):
        if self.handvalue == h.handvalue:
            return 0
        elif (self.handvalue + 1) % 3 == h.handvalue:
            return 1
        else:
            return -1


class Strategy(ABC):
    @abstractmethod
    def next_hand(self) -> Hand:
        pass

    @abstractmethod
    def study(self, win: bool) -> None:
        pass


class WinningStrategy(Strategy):
    def __init__(self):
        self.won = False
        self.previous_hand: Hand = None

    def next_hand(self) -> Hand:
        if not self.won:
            self.previous_hand = Hand.get_hand(random.randint(0, 2))

        return self.previous_hand

    def study(self, win: bool) -> None:
        self.won = win


class ProbStrategy(Strategy):
    def __init__(self):
        self.history = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]
        self.prev_hand = 0
        self.current_hand = 0

    def next_hand(self) -> Hand:
        bet: int = random.randint(0, self.get_sum(self.current_hand))
        handvalue = 0
        if bet < self.history[self.current_hand][0]:
            handvalue = 0
        elif (bet < self.history[self.current_hand][0] +
              self.history[self.current_hand][1]):
            handvalue = 1
        else:
            handvalue = 2
        self.prev_hand = self.current_hand
        self.current_hand = handvalue
        return Hand.get_hand(handvalue)

    def get_sum(self, handvalue: int) -> int:
        _sum = 0
        for v in self.history[handvalue]:
            _sum += v

        return _sum

    def study(self, win: bool) -> None:
        if win:
            self.history[self.prev_hand][self.current_hand] += 1
        else:
            self.history[self.prev_hand][(self.current_hand + 1) % 3] += 1
            self.history[self.prev_hand][(self.current_hand + 2) % 3] += 1
