from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class MessageBuilder(ABC):

    @property
    @abstractmethod
    def message(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(MessageBuilder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._message = Message1()

    @property
    def message(self) -> Message1:
    
        message = self._message
        self.reset()
        return message

    def produce_part_a(self) -> None:
        self._message.add("PartA1")

    def produce_part_b(self) -> None:
        self._message.add("PartB1")

    def produce_part_c(self) -> None:
        self._message.add("PartC1")


class Message1():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Messages parts: {', '.join(self.parts)}", end="")


class User:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> MessageBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: MessageBuilder) -> None:
        self._builder = builder


    def build_minimal_viable_message(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_message(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":

    user = User()
    builder = ConcreteBuilder1()
    user.builder = builder

    print("Standard basic product: ")
    user.build_minimal_viable_message()
    builder.message.list_parts()
    print('\n')
    



 # Builder in this case will not be useful since we will have only one type of class "Message".
 # Use the Builder pattern when you want your code to be able to create different representations of some product (for example, stone and wooden houses).