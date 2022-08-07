from __future__ import annotations
from abc import ABC, abstractmethod


class MessageFactory(ABC):
  
    @abstractmethod
    def factory_method(self):
        message = 'Test'
        return message

    def some_operation(self) -> str:
        message = self.factory_method()

        result = f"Message is: {message.operation()}"

        return result

class MessageCreator(MessageFactory):

    def factory_method(self) -> Message:
        return MessageCreation()

class Message(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass

    @abstractmethod
    def check(self)-> bool:
        pass


class MessageCreation(Message):

    def operation(self) -> str:
        return "{Result of the send message}"
    
    def check(self) -> bool:
        print('values compared')
        return True

def client_code(creator: MessageFactory) -> None:

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(MessageCreator())
    print("\n")

    # Probable we will not se this because we know what we want to return.
    ## Use the Factory Method when you want to provide users of your library or framework with a way to extend its internal components.
    ## Use the Factory Method when you don’t know beforehand the exact types and dependencies of the objects your code should work with.