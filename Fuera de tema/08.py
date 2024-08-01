import turtle as t

def draw_text(turtle, text, position, color, font_size, font_style):
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()
    turtle.color(color)
    turtle.write(text, align="center", font=("Arial", font_size, font_style))

def draw_text_with_outline(turtle, text, position, text_color, outline_color, font_size, font_style, outline_width):
    # Draw the outline
    turtle.penup()
    turtle.goto(position[0] - outline_width, position[1] - outline_width)
    turtle.pendown()
    turtle.color(outline_color)
    turtle.pensize(outline_width)
    turtle.write(text, align="center", font=("Arial", font_size, font_style))
    
    # Draw the text on top
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()
    turtle.color(text_color)
    turtle.pensize(1)
    turtle.write(text, align="center", font=("Arial", font_size, font_style))

def draw_message():
    screen = t.Screen()
    screen.bgcolor("lightblue")
    screen.title("Mensaje Especial")

    writer = t.Turtle()
    writer.speed(2)
    writer.hideturtle()

    # Draw "Para mi gran y único amor" with an outline
    draw_text_with_outline(
        writer, 
        "Para mi gran y único amor", 
        (0, 0), 
        "purple",        # Text color
        "darkviolet",    # Outline color
        36,              # Font size
        "bold",          # Font style
        4                # Outline width
    )

    t.done()

if __name__ == "__main__":
    draw_message()
