class Computer:
    def __init__(self):
        self.serial = None
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = (f'Memory: {self.memory}GB',
                f'Hard Disk: {self.hdd}GB',
                f'Graphics Card: {self.gpu}',
                f'Serial: {self.serial}')
        return '\n'.join(info)

class ComputerBuilder:
    
    def __init__(self):
        self.computer = Computer()

    def set_serial(self, serial):
        self.computer.serial = serial
        return self 
    def set_memory(self, amount):
        self.computer.memory = amount
        return self
    def set_hdd(self, amount):
        self.computer.hdd = amount
        return self 
    def set_gpu(self, gpu_model):
        self.computer.gpu = gpu_model
        return self

    def build(self):
        return self.computer

if __name__ == '__main__':
    computer = ComputerBuilder()\
        .set_gpu("GeForce GTX 650 Ti")\
            .set_hdd('500')\
                .set_memory("8")\
                    .set_serial("AG23385193")\
                        .build()
    print(computer)