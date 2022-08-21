from builder import HardwareEngineer


MINI14 = '1.4GHz Mac mini'
MINI15 = '1.5GHz Mac mini'
class AppleFactory:
    class MacMini14:
        def __init__(self):
            self.memory = 4  # in gigabytes
            self.hdd = 500  # in gigabytes
            self.gpu = 'Intel HD Graphics 5000'

        def __str__(self):
            info = (f'Model: {MINI14}',
                    f'Memory: {self.memory}GB',
                    f'Hard Disk: {self.hdd}GB',
                    f'Graphics Card: {self.gpu}')
            return '\n'.join(info)

    class CustomComputer:
        def __init__(self):
            self.memory = 10  # in gigabytes
            self.hdd = 5000  # in gigabytes
            self.gpu = 'Intel HD Graphics 6000'

        def main(self):
            engineer = HardwareEngineer()
            engineer.construct_computer(hdd=self.hdd,memory=self.memory,gpu=self.gpu)
            computer = engineer.computer
            return computer

    def build_computer(self, model):
        if model == MINI14:
            return self.MacMini14()
        else:
            return self.CustomComputer()


if __name__ == '__main__':
    factory = AppleFactory()
    mac_mini = factory.build_computer(MINI14)
    mac_mini1 = factory.build_computer(MINI15).main()
    print(mac_mini)
    print('\n')
    print(mac_mini1)
    print('\n')
#  Exemplos de uso: O padrão Factory Method é amplamente utilizado no código Python. É muito útil quando você precisa fornecer um alto nível de flexibilidade para seu código.