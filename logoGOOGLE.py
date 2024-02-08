import turtle

gg = turtle.Turtle()
turtle.bgcolor("black")
gg.color("#4285F4", "#4285F4")
gg.pensize(5)


# gg.speed(0)

# [ google color codes ]
#   red    = #DB4437
#   blue   = #4285F4
#   green  = #0F9D58
#   yellow = #F4B400

def google():
    gg.forward(120)   # Движение вперед на 120 единиц
    gg.right(90)   # Поворот направо на 90 градусов
    gg.circle(-150, 50)      # Рисование дуги с радиусом -150 и углом 50 градусов влево
    gg.color("#0F9D58")   # Установка цвета рисования в зеленый
    gg.circle(-150, 100)   # Рисование дуги с радиусом -150 и углом 100 градусов влево
    gg.color("#F4B400")  # Установка цвета рисования в оранжевый
    gg.circle(-150, 60)    # Рисование дуги с радиусом -150 и углом 60 градусов влево
    gg.color("#DB4437", "#DB4437")  # Установка цвета рисования и заливки в красный
    gg.begin_fill()    # Начало заливки фигуры
    gg.circle(-150, 100)  # Рисование дуги с радиусом -150 и углом 100 градусов влево
    gg.right(90)  # Поворот направо на 90 градусов
    gg.forward(50)  # Движение вперед на 50 единиц
    gg.right(90)
    gg.circle(100, 100)
    gg.right(90)
    gg.forward(50)
    gg.end_fill()
    gg.begin_fill()
    gg.color("#F4B400", "#F4B400")
    gg.right(180)
    gg.forward(50)
    gg.right(90)
    gg.circle(100, 60)
    gg.right(90)
    gg.forward(50)
    gg.right(90)
    gg.circle(-150, 60)
    gg.end_fill()
    gg.right(90)
    gg.forward(50)
    gg.right(90)
    gg.circle(100, 60)
    gg.color("#0F9D58", "#0F9D58")
    gg.begin_fill()
    gg.circle(100, 100)
    gg.right(90)
    gg.forward(50)
    gg.right(90)
    gg.circle(-150, 100)
    gg.right(90)
    gg.forward(50)
    gg.end_fill()
    gg.right(90)
    gg.circle(100, 100)
    gg.color("#4285F4", "#4285F4")
    gg.begin_fill()
    gg.circle(100, 25)
    gg.left(115)
    gg.forward(65)
    gg.right(90)
    gg.forward(42)
    gg.right(90)
    gg.forward(124)
    gg.right(90)
    gg.circle(-150, 50)
    gg.right(90)
    gg.forward(50)
    gg.end_fill()


google()
gg.hideturtle()
turtle.done()