
from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class AbstractProductA:
    def useful_abstraction_a(self) -> str:
        pass
class AbstractProductB:
    def useful_abstraction_b(self) -> str:
        pass


class ProductA(AbstractProductA):
    def useful_abstraction_a(self) -> str:
        return 'Product A'

class ProductB(AbstractProductA):
    def useful_abstraction_b(self) -> str:
        return 'Product B'

    def second_abstraction_b(self) -> str:
        return 'second abstraction b'


if __name__ == "__main__":
    print(ProductB().useful_abstraction_b())
    print('\n')
    print(ProductB().useful_abstraction_a())
    print('\n')
# Since this will be a delivery message framework Abstract doesn't see much sense since it will be straight forward
# Use the Abstract Factory when your code needs to work with various families of related products, but you don’t want it to depend on the concrete classes of those products—they might be unknown beforehand or you simply want to allow for future extensibility.