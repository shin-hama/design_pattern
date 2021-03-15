""" Factory Method Pattern

特定のクラスを継承したインスタンスを作成する処理を共通化する
具体的なサブクラスに依存しない処理を実現することができる。
"""

from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def use(self) -> None:
        raise NotImplementedError


class Factory(ABC):
    def create(self, owner: str) -> Product:
        """ Template method to create instance of `Product`. This method
        supports to create the class implemented `Product`
        """
        product = self.create_product(owner)
        self.register_product(product)

        return product

    @abstractmethod
    def create_product(self, owner: str) -> Product:
        raise NotImplementedError

    @abstractmethod
    def register_product(self, product: Product) -> None:
        raise NotImplementedError
