from abc import ABC, abstractmethod


class Banner(object):
    def __init__(self, string: str):
        self.string = string

    def show_with_paren(self) -> None:
        print(f"({self.string})")

    def show_with_aster(self) -> None:
        print(f"*{self.string}*")


class Print(ABC):
    @abstractmethod
    def print_weak(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def print_strong(self) -> None:
        raise NotImplementedError


class PrintBanner(Banner, Print):
    def __init__(self, string: str):
        super().__init__(string)

    def print_weak(self) -> None:
        self.show_with_paren()

    def print_strong(self) -> None:
        self.show_with_aster()


if __name__ == '__main__':
    pb = PrintBanner("Hello")
    pb.print_weak()
    pb.print_strong()
