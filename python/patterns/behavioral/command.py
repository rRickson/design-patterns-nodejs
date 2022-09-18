
from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like "
              f"({self._payload})")


class Processor:

    _on_start = None
    _on_finish = None

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":

    invoker = Invoker()
    invoker.set_on_finish(SimpleCommand("Send Report"))

    invoker.do_something_important()




#  Use the Command pattern when you want to parametrize objects with operations.

