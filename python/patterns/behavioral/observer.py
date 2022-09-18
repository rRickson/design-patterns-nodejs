
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Product(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteProduct(Product):
    _state: int = None

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Product: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Product: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:

        print("\nProduct: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Product: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):

    @abstractmethod
    def update(self, product: Product) -> None:
        pass


class Client(Observer):
    def update(self, product: Product) -> None:
        if product._state < 3:
            print("Client: Send Email about the product")


class GoogleAd(Observer):
    def update(self, product: Product) -> None:
        if product._state == 0 or product._state >= 2:
            print("Google: Create New AD")


if __name__ == "__main__":
    # The client code.

    product = ConcreteProduct()

    client = Client()
    product.attach(client)

    googleAd = GoogleAd()
    product.attach(googleAd)

    product.some_business_logic()
    product.some_business_logic()


#  Use the Observer pattern when changes to the state of one object may require changing other objects,
#  and the actual set of objects is unknown beforehand or changes dynamically.