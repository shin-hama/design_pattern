from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, caption: str):
        self.caption = caption

    @abstractmethod
    def make_html(self) -> str:
        pass


class Link(Item):
    def __init__(self, caption: str, url: str):
        super().__init__(caption)
        self.url = url


class Tray(Item):
    def __init__(self, caption: str):
        super().__init__(caption)
        self.tray: list = []

    def add(self, item: Item):
        self.tray.append(item)


class Page(ABC):
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.content: list = []

    def add(self, item: Item) -> None:
        self.content.append(item)

    def output(self) -> None:
        try:
            filename = f"{self.title}.html"
            with open(filename, mode="w", encoding="utf-8") as f:
                f.writelines(self.make_html())

            print(f"Has created {filename}")
        except Exception as e:
            raise e

    @abstractmethod
    def make_html(self) -> list:
        pass
