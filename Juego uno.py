import turtle

na = turtle.Screen()
na.title("(~‾▿‾)~ MI PRIMER JUEGO ヽ(*≧ω≦)ﾉ")
na.bgcolor("black")
na.setup(width=800, height=600)
na.tracer(0)

marcadorA = 0
marcadorB = 0


keroro = turtle.Turtle()
keroro.speed(0)
keroro.shape("square")
keroro.color("white")
keroro.penup()
keroro.goto(-350, 0)
keroro.shapesize(stretch_wid=5, stretch_len=1)

tamama = turtle.Turtle()
tamama.speed(0)
tamama.shape("square")
tamama.color("white")
tamama.penup()
tamama.goto(350, 0)
tamama.shapesize(stretch_wid=5, stretch_len=1)

kerobola = turtle.Turtle()
kerobola.speed(0)
kerobola.shape("square")
kerobola.color("white")
kerobola.penup()
kerobola.goto(0,0)

#velocidad de la pelota
kerobola.dx = .5
kerobola.dy = .5


#dibujar el marcador.
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("keroro: 0		tamama: 0", align="center", font=("Courier", 25, "normal"))


def keroro_up():
	y = keroro.ycor()
	y += 20
	keroro.sety(y)

def keroro_down():
	y = keroro.ycor()
	y -= 20
	keroro.sety(y)

def tamama_up():
	y = tamama.ycor()
	y += 20
	tamama.sety(y)

def tamama_down():
	y = tamama.ycor()
	y -= 20
	tamama.sety(y)

na.listen()
na.onkeypress(keroro_up, "s")
na.onkeypress(keroro_down, "x")
na.onkeypress(tamama_up, "Up")
na.onkeypress(tamama_down, "Down")



while True:
	na.update()

	kerobola.setx(kerobola.xcor() + kerobola.dx)
	kerobola.sety(kerobola.ycor() + kerobola.dy)

	#colisiones bordes 
	if kerobola.ycor() > 290:
		kerobola.dy *= -1
	if kerobola.ycor() < -290:
		kerobola.dy *= -1

	# izq o derecha
	if kerobola.xcor() > 390:
		kerobola.goto(0,0)
		kerobola.dx *= -1
		marcadorA += 1
		pen.clear()
		pen.write(f"keroro: {marcadorA}		tamama: {marcadorB}", align="center", font=("Courier", 25, "normal"))

	if kerobola.xcor() < -390:
		kerobola.goto(0,0)
		kerobola.dx *= -1
		marcadorB += 1
		pen.clear()
		
		pen.write(f"keroro: {marcadorA}		tamama: {marcadorB}", align="center", font=("Courier", 25, "normal"))


	# colisiones
	if ((kerobola.xcor() > 340 and kerobola.xcor() < 350)
			and (kerobola.ycor() < tamama.ycor() + 50
			and kerobola.ycor() > tamama.ycor() - 50)):
		kerobola.dx *= -1

	if ((kerobola.xcor() < -340 and kerobola.xcor() > -350)
			and (kerobola.ycor() < keroro.ycor() + 50
			and kerobola.ycor() > keroro.ycor() - 50)):
		kerobola.dx *= -1
