""" Visitor Pattern
データモデルとロジックを分けて各クラスの独立性を高めている
モデルからVisitorへ、Visitorからモデルへお互いに処理を投げあっている
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Union


class Visitor(ABC):
    @abstractmethod
    def visit(self, entry: Union[Directory, File]) -> None:
        pass


class ListVisitor(Visitor):
    def __init__(self, current_dir: str = ""):
        self.current_dir = current_dir

    def visit(self, entry: Union[Directory, File]) -> None:
        print(f"{self.current_dir}/{entry}")

        if isinstance(entry, Directory):
            backup = self.current_dir
            self.current_dir = f"{self.current_dir}//{entry.get_name()}"
            for e in entry.directory:
                e.accept(self)

            self.current_dir = backup


class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class Entry(Element):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    def add(self, entry: Entry):
        raise NotImplementedError

    def __str__(self):
        return f"{self.get_name()}({self.get_size()})"


class File(Entry):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        return self.size

    def accept(self, visitor: Visitor) -> None:
        visitor.visit(self)


class Directory(Entry):
    def __init__(self, name: str):
        self.name = name
        self.directory: list[Entry] = []

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        size = 0
        for d in self.directory:
            size += d.get_size()

        return size

    def add(self, entry: Entry) -> Entry:
        self.directory.append(entry)
        return self

    def accept(self, visitor: Visitor) -> None:
        visitor.visit(self)


if __name__ == "__main__":
    print("Making root entries...")
    rootdir = Directory("root")
    bindir = Directory("bin")
    tmpdir = Directory("tmp")
    usrdir = Directory("usr")
    rootdir.add(bindir)
    rootdir.add(tmpdir)
    rootdir.add(usrdir)
    bindir.add(File("vi", 10000))
    bindir.add(File("latex", 20000))

    rootdir.accept(ListVisitor())
