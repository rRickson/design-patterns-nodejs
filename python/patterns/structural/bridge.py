from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")


class ProvideAbstraction(Abstraction):

    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


class Implementation(ABC):

    @abstractmethod
    def operation_implementation(self) -> str:
        pass

class Provide1(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class Provide2(Implementation):
    # Use different implementation to create multiple configuration to multiple providers.
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


def client_code(abstraction: Abstraction) -> None:

    print(abstraction.operation(), end="")

if __name__ == "__main__":

    implementation = Provide1()
    abstraction = ProvideAbstraction(implementation)
    client_code(abstraction)



# To allow the user to send message trought multiple providers having a bridge to allow this would be helpful.
# To allow the user to change keys in run time also will be useful.

''' 
Use the Bridge if you need to be able to switch implementations at runtime.

Use the Bridge pattern when you want to divide and organize a monolithic class that has several variants of some functionality 
(for example, if the class can work with various database servers).
'''