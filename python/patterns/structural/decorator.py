class Message():

    def sendMessage(self) -> str:
        pass


class MessageComponent(Message):

    def sendMessage(self) -> str:
        print('MESSAGE LOGIC')
        return "MessageComponent"


class InitWarp(Message):

    _component: Message = None

    def __init__(self, component: Message) -> None:
        self._component = component

    @property
    def component(self) -> Message:
        return self._component

    def sendMessage(self) -> str:
        return self._component.sendMessage()


class DecoratorProviderA(InitWarp):

    def sendMessage(self) -> str:
        return f"DecoratorProviderA({self.component.sendMessage()})"


class DecoratorProviderB(InitWarp):
    def sendMessage(self) -> str:
        return f"DecoratorProviderB({self.component.sendMessage()})"


def client_code(component: Message) -> None:
    print(f"RESULT: {component.sendMessage()}", end="")

if __name__ == "__main__":
    # This way the client code can support both simple components...
    simple = MessageComponent()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as decorated ones.
    #
    # Note how decorators can wrap not only simple components but the other
    # decorators as well.
    decorator1 = DecoratorProviderA(simple)
    decorator2 = DecoratorProviderB(decorator1)
    print("Client: Now I've got a decorated component:")
    client_code(decorator2)






# This can be used to have one same behavior for all the providers.
# Use the Decorator pattern when you need to be able to assign extra behaviors to objects at runtime without breaking the code that uses these objects.