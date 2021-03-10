""" Prototype Pattern

すでにあるインスタンスをコピーして新たなインスタンスを生成する
生成に複雑な過程が必要なもの、大枠は同じだが細部が異なるものに対して効果的
"""


from __future__ import annotations
from abc import ABC, abstractmethod
import copy
from unicodedata import east_asian_width


class Product(ABC):
    """ The cloneable interface
    """
    @abstractmethod
    def use(self, string: str) -> None:
        pass

    def create_clone(self) -> Product:
        return copy.deepcopy(self)


class Manager(object):
    def __init__(self):
        self.showcase: dict[str, Product] = {}

    def register(self, name: str, prototype: Product) -> None:
        """ Register instance that implement Product interface.
        """
        self.showcase[name] = prototype

    def create(self, name: str) -> Product:
        """ Create clone of registered prototype by Product.create_clone()
        """
        p: Product = self.showcase[name]
        return p.create_clone()


class MessageBox(Product):
    def __init__(self, decochar: str):
        if len(decochar) != 1:
            raise AttributeError

        self.decochar = decochar

    def use(self, string: str) -> None:
        # Always fill 2 char margins at both head and end.
        length = 4
        for c in string:
            if east_asian_width(c) in "FWA":
                # 全角文字は長さ 2 としてカウント
                length += 2
            else:
                # それ以外は長さ 1 としてカウント
                length += 1

        print(self.decochar * length)
        print()
        print(f"{self.decochar} {string} {self.decochar}")
        print()
        print(self.decochar * length)


class UnderLinePen(Product):
    def __init__(self, decochar: str):
        if len(decochar) != 1:
            raise AttributeError

        self.decochar = decochar

    def use(self, string: str):
        length = 0
        for c in string:
            if east_asian_width(c) in "FWA":
                # 全角文字は長さ 2 としてカウント
                length += 2
            else:
                # それ以外は長さ 1 としてカウント
                length += 1

        print(f'"{string}"')
        print(f" {self.decochar * length} ")


if __name__ == "__main__":
    m = Manager()
    upen = UnderLinePen("~")
    aster_box = MessageBox("*")
    slash_box = MessageBox("/")
    m.register("strong", upen)
    m.register("warning", aster_box)
    m.register("slash", slash_box)

    string = "Hello World!"
    p1 = m.create("strong")
    p1.use(string)
    p2 = m.create("warning")
    p2.use(string)
    p3 = m.create("slash")
    p3.use(string)
