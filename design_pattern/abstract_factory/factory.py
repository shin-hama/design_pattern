""" Implemented Abstract Factory
抽象クラスの実装、抽象クラスにのみ依存する
"""
from abstract_factory import Factory, Item, Link, Page, Tray


class ListLink(Link):
    def __init__(self, caption: str, url: str):
        super().__init__(caption, url)

    def make_html(self) -> str:
        return f"<li><a href={self.url}>{self.caption}</a></li>\n"


class ListTray(Tray):
    def __init__(self, caption: str):
        super().__init__(caption)

    def make_html(self) -> str:
        buf: list[str] = []
        buf.append("<li>\n")
        buf.append(f"{self.caption}\n")
        buf.append("<ul>\n")
        for t in self.tray:
            buf.append(t.make_html())

        buf.append("</ul>\n")
        buf.append("</li>\n")

        return "".join(buf)


class ListPage(Page):
    def __init__(self, title: str, author: str):
        super().__init__(title, author)

    def make_html(self) -> str:
        buf = []

        buf.append(f"<html><head><title>{self.title}</title></head>\n")
        buf.append("<body>\n")
        buf.append(f"<h1>{self.title}</h1>\n")
        buf.append("<ul>\n")
        for c in self.content:
            buf.append(c.make_html())

        buf.append("</ul>\n")
        buf.append(f"<hr><address>{self.author}</address>")
        buf.append("</body></html>\n")

        return "".join(buf)


class ListFactory(Factory):
    def create_link(self, caption: str, url: str) -> ListLink:
        return ListLink(caption, url)

    def create_tray(self, caption: str) -> ListTray:
        return ListTray(caption)

    def create_page(self, title: str, author: str) -> ListPage:
        return ListPage(title, author)
