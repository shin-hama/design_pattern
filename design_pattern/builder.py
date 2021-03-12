""" Builder Pattern

複雑な工程を実施するクラスを用意して、過程を隠蔽する
複雑な処理自体もインターフェースで実装を隠蔽することで、インターフェースを実装したもの
であればどんなものでも再利用可能にする
"""

from abc import ABC, abstractmethod
import sys


class Builder(ABC):
    @abstractmethod
    def make_title(self, title: str) -> None:
        pass

    @abstractmethod
    def make_string(self, string: str) -> None:
        pass

    @abstractmethod
    def make_items(self, items: list[str]) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass


class Director(object):
    def __init__(self, builder: Builder):
        self.builder = builder

    def construct(self) -> None:
        """ Use only Builder interface
        """
        self.builder.make_title("Greeting")
        self.builder.make_string("from morning to noon")
        self.builder.make_items([
            "Good morning",
            "Good evening",
        ])
        self.builder.make_string("at night")
        self.builder.make_items([
            "Good night",
            "Good bye",
        ])

        self.builder.close()


class TextBuilder(Builder):
    def __init__(self):
        self._buffer = []

    def make_title(self, title: str) -> None:
        self._buffer.append(f"{'='*20}\n")
        self._buffer.append(f"[ {title} ]\n")
        self._buffer.append("\n")

    def make_string(self, string: str) -> None:
        self._buffer.append(f"> {string}\n")
        self._buffer.append("\n")

    def make_items(self, items: list[str]) -> None:
        for item in items:
            self._buffer.append(f"  - {item}\n")
        self._buffer.append("\n")

    def close(self) -> None:
        self._buffer.append(f"{'='*20}\n")

    def get_result(self):
        return "".join(self._buffer)


class HTMLBuilder(Builder):
    def __init__(self):
        self._buffer = []

    def make_title(self, title: str) -> None:
        self._buffer.append(f"<html><head><title>{title}</title></head><body>")
        self._buffer.append(f"<h1>{title}</h1>")

    def make_string(self, string: str) -> None:
        self._buffer.append(f"<p>{string}</p>")

    def make_items(self, items: list[str]) -> None:
        self._buffer.append("<ul>")
        for item in items:
            self._buffer.append(f"<li>{item}</li>")
        self._buffer.append("</ul>")

    def close(self) -> None:
        self._buffer.append("</body></html>")

    def get_result(self):
        return "".join(self._buffer)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit()

    target = sys.argv[1]
    if target == "plain":
        builder = TextBuilder()
    elif target == "html":
        builder = HTMLBuilder()
    else:
        exit()

    director = Director(builder)
    director.construct()
    print(builder.get_result())
