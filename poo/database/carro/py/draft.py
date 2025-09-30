class Carro:
    def __init__ (self, Pass: int, km: int, PassMax: int, gas: int, gasMax: int):
        self.Pass: int = Pass
        self.km: int = km
        self.PassMax: int = PassMax
        self.gas: int = gas
        self.gasMax: int = gasMax
    
    def boarding(self) -> None:
        if self.Pass < self.PassMax:
            self.Pass += 1
        else:
            print("fail: limite de pessoas atingido")
    def landing(self) -> None:
        if self.Pass > 0:
            self.Pass -= 1
        else:
            print("fail: nao ha ninguem no carro")
    def gasInc(self, amount: int) -> None:
        self.gas += amount
        if self.gas > self.gasMax:
            self.gas = self.gasMax
    def driveCar(self, amount: int) -> None:
        if self.Pass == 0:
            print("fail: nao ha ninguem no carro")
            return
        elif self.gas == 0:
            print("fail: tanque vazio")
            return
        elif amount > self.gas:
            self.km += self.gas
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.gas = 0
            return
        self.gas -= amount
        self.km += amount
    def __str__(self) -> str:
        return f"pass: {self.Pass}, gas: {self.gas}, km: {self.km}"

def main():
    carro = Carro(0, 0, 2, 0, 100)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(carro)
        elif args[0] == "enter":
            carro.boarding()
        elif args[0] == "leave":
            carro.landing()
        elif args[0] == "fuel":
            amount: int = int(args[1])
            carro.gasInc(amount)
        elif args[0] == "drive":
            amount: int = int(args[1])
            carro.driveCar(amount)
main()