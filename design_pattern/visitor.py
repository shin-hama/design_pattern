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


class FileFindVisitor(Visitor):
    def __init__(self, suffix: str):
        self.suffix = suffix
        self.found_file: list[File] = []

    def visit(self, entry: Union[Directory, File]) -> None:
        if isinstance(entry, File) and entry.get_name().endswith(self.suffix):
            self.found_file.append(entry)

        if isinstance(entry, Directory):
            for e in entry.directory:
                e.accept(self)

    def get_found_file(self):
        return self.found_file


class SizeVisitor(Visitor):
    def __init__(self):
        self.size = 0

    def get_size(self) -> int:
        return self.size

    def visit(self, entry: Union[Directory, File]) -> None:
        if isinstance(entry, File):
            self.size += entry.get_size()

        if isinstance(entry, Directory):
            for d in entry.directory:
                d.accept(self)


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
        sv = SizeVisitor()
        self.accept(sv)
        return sv.get_size()

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
    bindir.add(File("vi.md", 10000))
    bindir.add(File("latex.tx", 20000))

    foo = Directory("foo")
    bar = Directory("bar")
    usrdir.add(foo)
    usrdir.add(bar)

    foo.add(File("index.html", 200))
    foo.add(File("memo.txt", 250))
    bar.add(File("sample.html", 500))
    foo.add(File("readme.txt", 50))

    ffv = ListVisitor()
    rootdir.accept(ffv)
