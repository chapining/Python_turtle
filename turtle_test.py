# ReadMe https://digitology.tech/docs/python_3/library/tutrle.html
import turtle as trl


#ToDo: узнать размер экрана
def draw_square(side_length = 100, x = 0, y = 0, line_color ="#FF6600", fill_color = "#00CCFF"):
    # настройка
    trl.pencolor(line_color)
    trl.fillcolor(fill_color)
    trl.penup()
    trl.goto(0, 0)
    trl.pendown()

    # рисование
    trl.begin_fill()
    trl.forward(side_length)
    trl.right(90)
    trl.forward(side_length)
    trl.right(90)
    trl.forward(side_length)
    trl.right(90)
    trl.forward(side_length)
    trl.right(90)
    trl.end_fill()

trl.shape("turtle")
trl.speed(1)

draw_square()


trl.done() 
