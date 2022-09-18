from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler): 
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

class GymGuyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Chicken":
            return f"Gym Guy: I'll eat the {request}"
        else:
            return super().handle(request)


class VeganGuyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Salad":
            return f"Vegan Guy: I'll eat the {request}"
        else:
            return super().handle(request)


class CarnivoreGuyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Ribs":
            return f"Carnivore Guy: I'll eat the {request}"
        else:
            return super().handle(request)

class ITGuyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Cup of coffee":
            return f"IT Guy: I'll drink a {request}"
        else:
            return super().handle(request)

def client_code(handler: Handler) -> None:
    
    for food in ["Chicken", "Salad", "Ribs", "Cup of coffee"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")


if __name__ == "__main__":
    gymGuy = GymGuyHandler()
    veganGuy = VeganGuyHandler()
    carnivoreGuy = CarnivoreGuyHandler()
    itGuy = ITGuyHandler();

    itGuy.set_next(veganGuy).set_next(carnivoreGuy).set_next(gymGuy)

    client_code(itGuy)
    print("\n")
    
    # The pattern lets you link several handlers into one chain and, upon receiving a request, 
    # “ask” each handler whether it can process it. This way all handlers get a chance to process the request.