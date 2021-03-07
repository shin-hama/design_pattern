""" Adapter pattern
インターフェースと実装済みのクラスのズレを埋めるようなデザインパターン。
すでに実装済みのクラスを継承し、インターフェースのメソッドから呼び出すことで、
使う側はインターフェース以外の情報を知る必要がなくなる。
"""

from abc import abstractmethod


class Banner(object):
    """ Target is connected to the interface
    """

    def __init__(self, string: str):
        self.string = string

    def show_with_paren(self) -> None:
        print(f"({self.string})")

    def show_with_aster(self) -> None:
        print(f"*{self.string}*")


class Print(object):
    """ Interface
    """
    @abstractmethod
    def print_weak(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def print_strong(self) -> None:
        raise NotImplementedError


class PrintBanner(Print):
    """ Adapter Class

    Create banner field and entrust to run.
    """

    def __init__(self, string: str):
        self.banner = Banner(string)

    def print_weak(self) -> None:
        self.banner.show_with_paren()

    def print_strong(self) -> None:
        self.banner.show_with_aster()


if __name__ == '__main__':
    pb = PrintBanner("Hello")
    pb.print_weak()
    pb.print_strong()
