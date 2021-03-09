""" Factory Method Pattern

サブクラスの実装例、インスタンス化の具体的な処理を記載
"""
from factory_framework import Product, Factory


class IDCard(Product):
    def __init__(self, owner: str):
        print(f"We will create {owner}'s card.")
        self.owner = owner

    def use(self) -> None:
        print(f"Use the card of {self.owner}")

    def get_owner(self) -> str:
        return self.owner


class IDCardFactory(Factory):
    def __init__(self):
        self.owners = []

    def create_product(self, owner: str) -> Product:
        return IDCard(owner)

    def register_product(self, product: IDCard) -> None:
        self.owners.append(product.get_owner())

    def get_owners(self) -> list:
        return self.owners


if __name__ == "__main__":
    factory = IDCardFactory()
    card1 = factory.create("hoge")
    card2 = factory.create("bar")
    card3 = factory.create("foo")
    card1.use()
    card2.use()
    card3.use()
