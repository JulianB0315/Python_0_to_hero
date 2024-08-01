import turtle as t

def draw_petal(turtle, fill_color, border_color, radius):
    turtle.color(border_color)
    turtle.begin_fill()
    turtle.circle(radius, 60)  # Arc for one side of the petal
    turtle.left(120)           # Angle to draw the petal shape
    turtle.circle(radius, 60)  # Arc for the other side of the petal
    turtle.left(120)           # Reset angle
    turtle.end_fill()
    turtle.color(fill_color)
    turtle.begin_fill()
    turtle.circle(radius, 60)  # Arc for one side of the petal
    turtle.left(120)           # Angle to draw the petal shape
    turtle.circle(radius, 60)  # Arc for the other side of the petal
    turtle.left(120)           # Reset angle
    turtle.end_fill()

def draw_circle(turtle, color, radius, x, y):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_text(turtle, text, position, color, font_size, font_style):
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()
    turtle.color(color)
    turtle.write(text, align="center", font=("Arial", font_size, font_style))

def draw_sunflower():
    screen = t.Screen()
    screen.bgcolor("lightblue")
    screen.title("Te quiero mucho")

    flower = t.Turtle()
    flower.speed(10)

    # Draw the stem
    flower.penup()
    flower.goto(0, -100)  # Start the stem at the base of the flower
    flower.setheading(-90)
    flower.color("green")
    flower.pendown()
    flower.pensize(30)  # Increase the thickness of the stem
    flower.forward(300)  # Length of the stem

    # Draw leaves
    flower.penup()
    flower.goto(-120, -350)  # Position for the leaves
    flower.setheading(-45)
    flower.color("green")
    flower.pendown()
    flower.begin_fill()
    flower.circle(100, 90)  # Adjusted leaf size
    flower.left(90)
    flower.circle(100, 90)
    flower.end_fill()

    flower.penup()
    flower.goto(120, -350)  # Position for the leaves
    flower.setheading(135)
    flower.pendown()
    flower.begin_fill()
    flower.circle(100, 90)  # Adjusted leaf size
    flower.left(90)
    flower.circle(100, 90)
    flower.end_fill()

    # Draw petals
    flower.penup()
    flower.goto(0, 50)  # Position the flower higher up
    flower.setheading(0)
    flower.pendown()
    flower.pensize(1)  # Reset to default
    for _ in range(20):  # Number of petals
        draw_petal(flower, "yellow", "orange", 250)  # Pétalos con borde amarillo oscuro
        flower.left(18)  # Adjust angle for more petals

    # Draw the center of the sunflower
    draw_circle(flower, "brown", 80, 0, 50)  # Smaller center size

    # Write "Te quiero" with a border
    draw_text(flower, "Te quiero", (0, 250), "red", 48, "bold")  # Main text
    flower.pensize(2)  # Border thickness
    flower.penup()
    flower.goto(0, 255)  # Position for border
    flower.pendown()
    flower.color("darkred")
    flower.write("Te quiero", align="center", font=("Arial", 48, "bold"))  # Border text

    # Hide the turtle
    flower.hideturtle()

    t.done()

if __name__ == "__main__":
    draw_sunflower()