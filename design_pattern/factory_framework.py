from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def use(self) -> None:
        raise NotImplementedError


class Factory(ABC):
    def create(self, owner: str):
        product = self.create_product(owner)
        self.register_product(product)

        return product

    @abstractmethod
    def create_product(self) -> Product:
        raise NotImplementedError

    @abstractmethod
    def register_product(self, product: Product):
        raise NotImplementedError
