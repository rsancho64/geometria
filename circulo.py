#! /usr/bin/python3

from figura import figura

class circulo (figura):
    
    __color = None
    
    # TODO elevar color a la superclase
    def __init__(self, dimensions=..., color=None) -> None:
        super().__init__(dimensions)
        self.__color == color

if __name__ == "__main__":

    f0 = figura()
    # print(f0.getDimensiones())
    print(f0)
    
    c0 = circulo()
    # print(c0.getDimensiones())
    print(c0)