""" Factory Method Pattern

サブクラスの実装例、インスタンス化の具体的な処理を記載
"""
from factory_framework import Product, Factory


class IDCard(Product):
    def __init__(self, owner: str, serial: int):
        print(f"We will create {owner}'s({serial}) card.")
        self.owner = owner
        self.serial = serial

    def use(self) -> None:
        print(f"Use the card of {self.owner}({self.serial})")

    def get_owner(self) -> str:
        return self.owner

    def get_serial(self) -> int:
        return self.serial


class IDCardFactory(Factory):
    def __init__(self):
        self.owners = []
        self.serial = 0

    def create_product(self, owner: str) -> Product:
        self.serial += 1
        return IDCard(owner, self.serial)

    def register_product(self, product: IDCard) -> None:
        self.owners.append({
            "owner": product.get_owner(),
            "serial": product.get_serial()
        })

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

    print(factory.owners)
