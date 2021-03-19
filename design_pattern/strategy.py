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
        return self.fight(h) == 1

    def is_weaker_than(self, h: Hand) -> bool:
        return self.fight(h) == -1

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


class Player(object):
    def __init__(self, name: str, strategy: Strategy):
        self.name = name
        self.strategy = strategy
        self.wincount = 0
        self.losecount = 0
        self.gamecount = 0

    def next_hand(self) -> Hand:
        return self.strategy.next_hand()

    def win(self) -> None:
        self.wincount += 1
        self.gamecount += 1

    def lose(self) -> None:
        self.losecount += 1
        self.gamecount += 1

    def even(self) -> None:
        self.gamecount += 1

    def __str__(self):
        return (
            f"{self.name}:{self.gamecount} games, {self.wincount} win, "
            f"{self.losecount} lose."
        )


if __name__ == "__main__":
    p1 = Player("taro", WinningStrategy())
    p2 = Player("jiro", ProbStrategy())

    for _ in range(10000):
        hand1 = p1.next_hand()
        hand2 = p2.next_hand()
        if hand1.is_stronger_than(hand2):
            p1.win()
            p2.lose()
        elif hand1.is_weaker_than(hand2):
            p1.lose()
            p2.win()
        else:
            p1.even()
            p2.even()

    print("result")
    print(p1)
    print(p2)
