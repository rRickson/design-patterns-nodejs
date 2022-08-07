from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def request(self) -> None:
        pass

class SendLogic(Subject):

    def request(self) -> None:

        print("SendLogic: Handling request to send request to message provider.")

    def response(self)-> None:
        print('Response Sending')

class Proxy(Subject):

    def __init__(self, real_subject: SendLogic) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")


def client_code(subject: Subject) -> None:
    subject.request()



if __name__ == "__main__":

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(SendLogic())
    client_code(proxy)
    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(SendLogic())
    client_code(proxy)

'''
Should be good use to protect the framework with some auth method, or verifications.
Logging requests (logging proxy). This is when you want to keep a history of requests to the service object.
'''