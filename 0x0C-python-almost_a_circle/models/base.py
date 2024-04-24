Args:
    list_rectangles (list): A list of Rectangle objects to draw.
    list_squares (list): A list of Square objects to draw.

    """
    turt = turtle.Turtle()
    turt.screen.bgcolor("#b7312c")
    turt.pensize(3)
    turt.shape("turtle")
    """
    turt.color("#ffffff")
    for rect in list_rectangles:
        turt.showturtle()
        turt.up()
        turt.goto(rect.x, rect.y)
        turt.down()
        for i in range(2):
            turt.forward(rect.width)
            turt.left(90)
            turt.forward(rect.height)
            turt.left(90)
        turt.hideturtle()

    turt.color("#b5e3d8")
    for sq in list_squares:
        turt.up()
        turt.goto(sq.x, sq.y)
        turt.down()
        for i in range(2):
            turt.forward(dq.width)
            turt.left(90)
            turt.forward(sq.helight)
            turt.left(90)
        turt.hideturle()


    turtle.exitonclick()


