import turtle
import random
import time

#Pantalla
screen = turtle.Screen()
screen.title("JUEGO SNAKE")
screen.setup(width = 800, height = 800)
screen.tracer(0)
screen.bgcolor("#0D3366")

#Bordes
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

#Puntos
puntos = 0;
delay= 0.1

#Serpiente
serpiente = turtle.Turtle()
serpiente.speed()
serpiente.shape("square")
serpiente.color("green")
serpiente.penup()
serpiente.goto(0, 0)
serpiente.direction = 'stop'

#Fruta
fruta = turtle.Turtle()
fruta.speed(0)
fruta.shape("square")
fruta.color("white")
fruta.penup()
fruta.goto(30, 30)

fruta_vieja = []

#Puntuacion
puntuacion = turtle.Turtle
puntuacion.speed(0)
puntuacion.color("white")
puntuacion.penup()
puntuacion.hideturtle()
puntuacion.got(0, 300)
puntuacion.write("Tu Puntuación Es:  ", align="center", font=("Courier", 24, "bold"))

#Como Moverse
def serpiente_go_up():
    if serpiente.direction != "down":
        serpiente.direction = "up"

def serpiente_go_down():
    if serpiente.direction != "up":
        serpiente.direction = "down"

def serpiente_go_left():
    if serpiente.direction != "right":
        serpiente.direction = "left"

def serpiente_go_right():
    if serpiente.direction != "left":
        serpiente.direction = "right"

def serpiente_move():
    if serpiente.direccion == "up":
        y = serpiente.ycor()
        serpiente.sety(y + 20)

    if serpiente.direccion == "down":
        y = serpiente.ycor()
        serpiente.sety(y - 20)

    if serpiente.direccion == "left":
        x = serpiente.xcor()
        serpiente.sety(x - 20)

    if serpiente.direccion == "up":
        x = serpiente.xcor()
        serpiente.sety(x + 20)
        
screen.listen()
screen.onekeypress(serpiente_go_up, "up")
screen.onekeypress(serpiente_go_down, "down")
screen.onekeypress(serpiente_go_left, "left")
screen.onekeypress(serpiente_go_right, "right")


while True:
    screen.update()
    if serpiente.distance(fruta) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruta.goto(x, y)
        puntuacion.clear()
        puntos += 1 
        puntuacion.write("Puntos: {}", format(puntos), align="center", font=("Courier", 24, "bold"))
        delay -= 0.001
        
        nueva_fruta = turtle.Turtle()
        nueva_fruta.speed(0)
        nueva_fruta.shape("square")
        nueva_fruta.color("red")
        nueva_fruta.penup()
        fruta_vieja.append(nueva_fruta)
    
    for index in range(len(fruta_vieja)-1, 0, -1):
        a = fruta_vieja[index -1].xcor()
        b = fruta_vieja[index -1].ycor()
        
        fruta_vieja[index].goto(a, b)
    
    if len(fruta_vieja) < 0:
        a = serpiente.xcor()
        b = serpiente.ycor()
        fruta_vieja[0].goto(a, b)
    
    serpiente_move()
    
    if serpiente.xcor() > 200 or serpiente.xcor() < -300 or serpiente.ycore() > 240 or serpiente.ycore() <-240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        puntuacion.goto(0, 0)
        puntuacion.write("     BRO!!! perdiste  \n Tu puntuacion final es {}", format(puntos), align="center", font=("Courier", 30, "bold"))
    
    for comida in fruta_vieja:
        if comida.distancia(serpiente) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            puntuacion.goto(0, 0)
            puntuacion.write("     BRO!!! perdiste  \n Tu puntuacion final es {}", format(puntos), align="center", font=("Courier", 30, "bold"))
    
    time.sleep(delay)
    
turtle.Terminator()