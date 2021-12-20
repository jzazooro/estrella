import turtle
from turtle import*
def estrella(vertex, firstcolor, secondcolor):
    color(firstcolor, secondcolor)
    begin_fill()
    vertex_int=int(vertex)
    cociente, resto=divmod(vertex_int, 2)
    if resto==0:
        vertex_int=vertex_int/2
    angle=180-(180/vertex_int)
    while True:
        forward(200)
        left(angle)
        if abs(pos())<1:
            break
    end_fill()
    done()
print("¿Cuantas puntas quieres que tenga tu estrella?")
vertex=input()
print("¿De que colres quieres la estrella?")
firstcolor=input()
secondcolor=input()
estrella(vertex, firstcolor, secondcolor)
