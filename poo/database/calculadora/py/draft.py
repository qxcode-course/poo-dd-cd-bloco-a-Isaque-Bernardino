class Calculator:
    def __init__(self, batteryMax: int, display: float, battery: int):
        self.batteryMax: int = batteryMax
        self.display: float = display
        self.battery: int = battery
    def batInit(self, amount: int) -> None:
        self.batteryMax = amount
        self.display = 0
        self.battery = 0
    def batInc(self, amount: int) -> None:
        self.battery += amount
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax
    def soma(self, a: float, b: float) -> None:
        if self.battery == 0:
            print("fail: bateria insuficiente")
            return   
        self.battery -= 1
        self.display = a + b
    def division(self, den: float, num: float) -> None:
        if self.battery == 0:
            print("fail: bateria insuficiente")
            return
        self.battery -= 1
        if num == 0:
            print("fail: divisao por zero")
            return
        self.display = den / num
        
    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
def main():
    calculadora = Calculator( 0, 0, 0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(calculadora)
        elif args[0] == "init":
            amount: int = int(args[1])
            calculadora.batInit(amount)
        elif args[0] == "charge":
            amount: int = int(args[1])
            calculadora.batInc(amount)
        elif args[0] == "sum":
            calculadora.soma(float(args[1]), float(args[2]))
        elif args[0] == "div":
            calculadora.division(float(args[1]), float(args[2]))

            
main()