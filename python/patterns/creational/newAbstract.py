from abc import abstractmethod,ABC


class Computer(ABC):

    @abstractmethod
    def getRAM(self):
        pass

    @abstractmethod
    def getHDD(self):
        pass

    @abstractmethod
    def getCPU(self):
        pass

    def __str__(self) -> str:
        return "RAM= "+self.getRAM()+", HDD="+self.getHDD()+", CPU="+self.getCPU()

class PC(Computer):

    def __init__(self, ram, hdd, cpu):
        self.ram = ram
        self.hdd = hdd
        self.cpu = cpu

    def getRAM(self):
        return self.ram
    
    def getHDD(self):
        return self.hdd

    def getCPU(self):
        return self.cpu

        
class Server(Computer):

    def __init__(self, ram, hdd, cpu):
        self.ram = ram
        self.hdd = hdd
        self.cpu = cpu

    def getRAM(self):
        return self.ram
    
    def getHDD(self):
        return self.hdd
        
    def getCPU(self):
        return self.cpu

class ComputerAbstractFactory:

    def createComputer(self):
        pass

class PCFactory(ComputerAbstractFactory):

    def __init__(self, ram, hdd, cpu):
        self.ram = ram
        self.hdd = hdd
        self.cpu = cpu

    def createComputer(self):
        return PC(self.ram,self.hdd,self.cpu)

class ServerFactory(ComputerAbstractFactory):

    def __init__(self, ram, hdd, cpu):
        self.ram = ram
        self.hdd = hdd
        self.cpu = cpu

    def createComputer(self):
        return Server(self.ram,self.hdd,self.cpu)

class ComputerFactory:

    def getComputer(factory:ComputerAbstractFactory):
        return factory.createComputer()

def main():
    pc = ComputerFactory.getComputer(PCFactory("16 GB","500 GB","2.4 GHz"))
    server = ComputerFactory.getComputer(ServerFactory("32 GB","1 TB","2.9 GHz"))
    print(pc)
    print(server)

if __name__ == '__main__':
    main()

# Abstract Factory pattern is robust and avoid conditional logic of Factory pattern.

# Abstract Factory design pattern provides approach to code for interface rather than implementation.
# Abstract Factory pattern is “factory of factories” and can be easily extended to accommodate more products,
#  for example we can add another sub-class Laptop and a factory LaptopFactory.