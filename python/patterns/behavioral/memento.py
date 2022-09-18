from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits


class Originator(): #Editor
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def do_something(self) -> None:
        print("Originator: I'm doing something important.")
        self._state = self._generate_random_string(30)
        print(f"Originator: and my state has changed to: {self._state}")

    def _generate_random_string(self, length: int = 10) -> None:
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:

        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:

        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


class Memento(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    # @abstractmethod
    # def get_date(self) -> str:
    #     pass


class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        # self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        return self._state

    def get_name(self) -> str:

        return f"({self._state[0:9]}...)"

    # def get_date(self) -> str:
    #     return self._date


class PowerPoint():

    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\PowerPoint: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"PowerPoint: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def specific(self) -> None:
        if not len(self._mementos):
            return
        
        memento = self._mementos[0]
        print(f"PowerPoint: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()        

    def show_history(self) -> None:
        print("PowerPoint: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    originator = Originator("Power Point about SDUI.")
    powerPoint = PowerPoint(originator)

    powerPoint.backup()
    originator.do_something()

    powerPoint.backup()
    originator.do_something()

    powerPoint.backup()
    originator.do_something()

    print()
    powerPoint.show_history()

    print("\nClient: Now, let's rollback!\n")
    powerPoint.undo()

    print("\nClient: Once more!\n")
    powerPoint.undo()

    print()
    powerPoint.show_history()
    print("\nClient: Specific!\n")
    powerPoint.specific()





# Use the Memento pattern when you want to produce snapshots of the object’s state 
# to be able to restore a previous state of the object.