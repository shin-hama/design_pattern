""" Strategy Pattern
"""
from __future__ import annotations
from abc import ABC, abstractmethod


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
