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
        self._buffer = ""

    def make_title(self, title: str) -> None:
        self._buffer += f"{'='*20}\n"
        self._buffer += f"[ {title} ]\n"
        self._buffer += "\n"

    def make_string(self, string: str) -> None:
        self._buffer += f"> {string}\n"
        self._buffer += "\n"

    def make_items(self, items: list[str]) -> None:
        for item in items:
            self._buffer += (f"  - {item}\n")
        self._buffer += "\n"

    def close(self) -> None:
        self._buffer += f"{'='*20}\n"

    def get_result(self):
        return self._buffer


class HTMLBuilder(Builder):
    def __init__(self):
        self._buffer = ""

    def make_title(self, title: str) -> None:
        self._buffer += f"<html><head><title>{title}</title></head><body>"
        self._buffer += f"<h1>{title}</h1>"

    def make_string(self, string: str) -> None:
        self._buffer += f"<p>{string}</p>"

    def make_items(self, items: list[str]) -> None:
        self._buffer += "<ul>"
        for item in items:
            self._buffer += (f"<li>{item}</li>")
        self._buffer += "</ul>"

    def close(self) -> None:
        self._buffer += "</body></html>"

    def get_result(self):
        return self._buffer


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
