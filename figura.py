#! /usr/bin/python3

class figura:
    
    __dimensiones = []
    
    def __init__(self, dimensions=[1,1]) -> None:
        self.__dimensiones = dimensions

    def getDimensiones(self):
        return self.__dimensiones

    def perimetro(self):
        return "P"

    def area(self):
        return "A"

    def __str__(self) -> str:
        answ = f"figura: "
        answ += f"area: {self.area()} "
        answ += f"perim: {self.perimetro()} "
        return answ

if __name__ == "__main__":
    
    f0 = figura()
    # print(f0.getDimensiones())
    print(f0)
    
    f1 = figura([2])
    # print(f1.getDimensiones())
    print(f1)    
    
    f3 = figura([2,3])
    # print(f3.getDimensiones())
    print(f3)    
    