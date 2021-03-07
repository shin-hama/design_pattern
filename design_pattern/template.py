""" Template Method Pattern

大まかな処理の流れを基底クラスで共通化し、詳細な処理をサブクラス上で実装する。
似たような処理を行う異なるクラスを複数作る必要がなくなり、メンテナンスも楽になる。
しかし、基底クラスとサブクラスの結合度は高くなってしまう。
"""

from abc import ABC, abstractmethod
from typing import final
from unicodedata import east_asian_width


class AbstractDisplay(ABC):
    @abstractmethod
    def open(self):
        raise NotImplementedError

    @abstractmethod
    def close(self):
        raise NotImplementedError

    @abstractmethod
    def print(self):
        raise NotImplementedError

    @final
    def display(self):
        """ Prohibits override
        """
        self.open()

        for i in range(0, 5):
            self.print()

        self.close()


class CharDisplay(AbstractDisplay):
    """ Display a charactor between << and >>
    """

    def __init__(self, c: str):
        if len(c) != 1:
            raise AttributeError
        self.c: str = c

    def open(self):
        print("<<")

    def close(self):
        print(">>")

    def print(self):
        print(self.c)


class StringDisplay(AbstractDisplay):
    """ Display string that is framed by line.
    """

    def __init__(self, string: str):
        self.string = string
        self.width = 0
        for c in self.string:
            if east_asian_width(c) in "FWA":
                # 全角文字は長さ 2 としてカウント
                self.width += 2
            else:
                # それ以外は長さ 1 としてカウント
                self.width += 1

    def open(self):
        self.print_frame()

    def close(self):
        self.print_frame()

    def print(self):
        print(f"|{self.string}|")

    def print_frame(self):
        print(f"+{'-'*self.width}+")


if __name__ == "__main__":
    ch = CharDisplay("r")
    ch.display()

    st = StringDisplay("test てすと")
    st.display()
