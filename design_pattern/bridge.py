""" Bridge Pattern
機能側に実装を委譲することで機能と実装を分けることができる。
    機能：処理の大まかな流れ
    実装：流れの中の細かい処理
コードサンプルによれば、コンソールに表示するために前処理、本処理、後処理を行うという
流れを機能側で定義。各工程での処理内容は実装側で定義している。
"""
from abc import ABC, abstractmethod
from typing import final


class DisplayImpl(ABC):
    """ Abstract implementer
    """
    @abstractmethod
    def raw_open(self):
        pass

    @abstractmethod
    def raw_print(self):
        pass

    @abstractmethod
    def raw_close(self):
        pass


class StringDisplay(DisplayImpl):
    def __init__(self, string: str):
        self.string = string

    def raw_open(self):
        self.print_line()

    def raw_print(self):
        print(self.string)

    def raw_close(self):
        self.print_line()

    def print_line(self):
        print("-" * 10)


class CharDisplay(DisplayImpl):
    def __init__(self, char: str):
        self.char = char[0]
        self.buf: list = []

    def raw_open(self):
        self.buf.append("<")

    def raw_print(self):
        self.buf.append(self.char)

    def raw_close(self):
        self.buf.append(">")
        print("".join(self.buf))
        self.buf = []


class Display(object):
    """ Abstract abstraction
    """

    def __init__(self, impl: DisplayImpl):
        self.impl = impl

    def open(self):
        self.impl.raw_open()

    def print(self):
        self.impl.raw_print()

    def close(self):
        self.impl.raw_close()

    @final
    def display(self):
        self.open()
        self.print()
        self.close()


class CountDisplay(Display):
    def multi_display(self, times: int) -> None:
        """ Add different process flow
        """
        self.open()
        for i in range(0, times):
            self.print()
        self.close()


class IteratorDisplay(CountDisplay):
    def __init__(self, impl: DisplayImpl, steps: int):
        self.steps = steps
        super().__init__(impl)

    def iterate_display(self, times: int) -> None:
        count = 0
        for i in range(0, times):
            self.multi_display(count)
            count += self.steps


if __name__ == "__main__":
    d = IteratorDisplay(CharDisplay("test"), 2)
    d.iterate_display(6)
