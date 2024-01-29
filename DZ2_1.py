import turtle


def draw_rec(t, order, size):
    if order == 0:
        t.forward(size)
        t.penup()
        t.left(180)
        t.forward(size)
        t.pendown()
        t.left(180)
    else:
        t.forward(size)
        t.left(45)
        draw_rec(t, order - 1, size / 2**0.5)
        t.right(90)
        draw_rec(t, order - 1, size / 2**0.5)
        t.penup()
        t.left(225)
        t.forward(size)
        t.left(180)
        t.pendown()


def draw(order, size=100):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -size)
    t.pendown()
    t.left(90)
    draw_rec(t, order, size)

    window.mainloop()


if __name__ == "__main__":
    recursion = input("Input recursion level\n")
    if recursion.isdigit() and int(recursion) >= 0:
        draw(int(recursion))
    else:
        print("Wrong input")
