

class Towel:
    def __init__(self, color: str, size: str): # construtor
        self.color = color # atributos
        self.size = size
        self.wetness = 0
    def __str__(self):
        return f"color: {self.color}, tam: {self.size}, umi: {self.wetness}"
# referência
towel = Towel("green", "G") # objetos
print(towel.color)
print(towel.size)
print(towel.wetness)

print(towel)