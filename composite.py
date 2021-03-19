""" Composite Pattern
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Entry(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def print_list(self, prefix: str = "") -> None:
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

    def print_list(self, prefix: str = "") -> None:
        print(f"{prefix}/{self}")


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

    def print_list(self, prefix: str = "") -> None:
        print(f"{prefix}/{self}")
        for d in self.directory:
            d.print_list(f"{prefix}/{self.name}")


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

    rootdir.print_list()
