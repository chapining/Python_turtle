import turtle as t


def build_house(base_x = -500, base_y = -500, base_width = 100, base_height = 10, base_fill = "#000000", walls_width = 20, walls_height = 30000, walls_fill = "#000000", roof_width = 0, roof_height = 0, roof_fill = "#000000", door_fill = "pink"):
    """
        base_x — X левого нижнего угла фундамента
        base_y — Y левого нижнего угла фундамента
        base_width — ширина фундамента
        base_height — высота фундамента
        base_fill — цвет заливки фундамента

        walls_x - считаем автоматически
        walls_y - считаем автоматически
        walls_width - спрашиваем у заказчика
        walls_height - спрашиваем у заказчика
        walls_fill - спрашиваем у заказчика
        
        door_width - 30% от ширины стен
        door_x - (ширина стен - ширина двери) / 2
        door_fill

        roof_x - считаем автоматически
        roof_y - считаем автоматически
        roof_width - 120% ширины
        roof_height - спрашиваем у заказчика
        roof_fill - спрашиваем у заказчика
    """
    t.speed(5)

    # считаем автоматические переменные
    walls_x = base_x
    walls_y = base_y + base_height
    walls_width = base_width

    door_width = walls_width * 0.3
    door_height = walls_height * 0.8
    door_x = walls_x + (walls_width - door_width) / 2
    door_y = walls_y 

    roof_y = walls_y + walls_height
    roof_x = base_x - (base_width * 0.05)
    roof_width = walls_width * 1.1


    def build_base(base_x, base_y, base_width, base_height, base_fill):
        t.penup()
        t.goto(base_x, base_y)
        t.setheading(0)
        t.fillcolor(base_fill)
        t.begin_fill()
        t.pendown()
        t.forward(base_width)
        t.left(90)
        t.forward(base_height)
        t.left(90)
        t.forward(base_width)
        t.left(90)
        t.forward(base_height)
        t.left(90)
        t.end_fill()


    def build_walls(walls_x, walls_y, walls_width, walls_height, walls_fill):
        t.penup()
        t.goto(walls_x, walls_y)
        t.setheading(0)
        t.fillcolor(walls_fill)
        t.begin_fill()
        t.pendown()
        print(walls_height)
        input()
        t.forward(walls_width)
        t.left(90)
        t.forward(walls_height)
        t.left(90)
        t.forward(walls_width)
        t.left(90)
        t.forward(walls_height)
        t.left(90)
        t.end_fill()
        

    def build_door(door_x, door_y, door_width, door_height, door_fill):
        t.penup()
        t.goto(door_x, door_y)
        t.setheading(0)
        t.fillcolor(door_fill)
        t.begin_fill()
        t.pendown()
        t.forward(door_width)
        t.left(90)
        t.forward(door_height)
        t.left(90)
        t.forward(door_width)
        t.left(90)
        t.forward(door_height)
        t.left(90)
        t.end_fill()


    def build_roof(roof_x, roof_y, roof_width, roof_height, roof_fill):
        t.penup()
        t.goto(roof_x, roof_y)
        t.setheading(0)
        t.fillcolor(roof_fill)
        t.pendown()
        t.begin_fill()
        t.forward(roof_width)
        t.goto(roof_x + roof_width / 2, roof_y + roof_height)
        t.goto(roof_x, roof_y)
        t.end_fill()


    build_base(base_x, base_y, base_width, base_height, base_fill)
    build_walls(walls_x, walls_y, walls_width, walls_width, walls_fill)
    build_door(door_x, door_y, door_width, door_height, door_fill)
    build_roof(roof_x, roof_y, roof_width, roof_height, roof_fill)

build_house(base_x = 0, base_y = 0, base_width = 200, base_height = 10, base_fill = "#660000", walls_fill = "#ff7f00", walls_height = 300, roof_height = 300, door_fill = "#ff0809")

t.done()
