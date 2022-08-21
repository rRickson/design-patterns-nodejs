import threading
import logging
import time

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        a = 'a'
        b = 'b'
        if a != b:
            return 'A diff B'

def createThread(name):
    print("Thread %s: starting", name)
    s1 = Singleton()
    print("Thread %s: finishing", name)
    return s1

# python3 -u "/Users/ricksonvasconcelos/Desktop/Arquitetura/python/patterns/creational/singleton.py"

if __name__ == "__main__":

    s1 = threading.Thread(target=createThread, args=(1,)).start()
    s2 = threading.Thread(target=createThread, args=(2,)).start()
    # threading.Thread().start()
    # threading.Thread().start()
    # s1 = Singleton();
    # s2 = Singleton()
    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")


# This can be used to have only one instance of send message to external services.
# Use the Singleton pattern when you need stricter control over global variables.

