""" Abstract Factory Client
Abstract Factory モジュール内のインターフェースのみを使用して実態を作成する
クライアント内はAbstract Factory の実装を知らなくても動くため、新しい実装の追加が容易
"""
from abstract_factory import Factory


class Client:
    def main(self, factory: Factory):
        asahi = factory.create_link("asahi", "http://www.asahi.com/")
        yomiuri = factory.create_link("yomiuri", "http://www.yomiuri.co.jp/")

        us_yahoo = factory.create_link("Yahoo!", "http://www.yahoo.com/")
        jp_yahoo = factory.create_link("Yahoo!", "http://www.yahoo.co.jp/")
        excite = factory.create_link("Excite", "http://excite.com")
        google = factory.create_link("Google", "http://google.com")

        tray_news = factory.create_tray("news paper")
        tray_news.add(asahi)
        tray_news.add(yomiuri)

        tray_yahoo = factory.create_tray("yahoo")
        tray_yahoo.add(us_yahoo)
        tray_yahoo.add(jp_yahoo)

        tray_search = factory.create_tray("Search Engine")
        tray_search.add(tray_yahoo)
        tray_search.add(excite)
        tray_search.add(google)

        page = factory.create_page("LinkPage", "shinichiro")
        page.add(tray_news)
        page.add(tray_search)
        page.output()


if __name__ == "__main__":
    client = Client()

    # クライアントを呼び出す側は実装の知識が必要
    from factory import ListFactory
    client.main(ListFactory())
