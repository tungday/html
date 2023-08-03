import turtle
import random

# Khởi tạo cửa sổ
window = turtle.Screen()
window.title("Trò chơi đá bóng sử dụng Turtle Python")
window.bgcolor("white")
window.setup(width=800, height=600)

# Khởi tạo cầu môn
goal = turtle.Turtle()
goal.penup()
goal.goto(250, 200)
goal.pendown()
goal.forward(100)
goal.right(90)
goal.forward(400)
goal.right(90)
goal.forward(100)

# Khởi tạo quả bóng
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(-350, 0)

# khoi tao text
text_display = turtle.Turtle()
text_display.hideturtle()
text_display.penup()
text_display.color("black")
text_display.goto(0, 260)
# Hàm di chuyển bóng đến vị trí ngẫu nhiên
def move_ball():
    ball.goto(300,random.randint(-290, 290))

# Hàm kiểm tra xem quả bóng có vào cầu môn hay không
def check_goal():
    if  ball.xcor() >= 250 and -200 < ball.ycor() < 200:
        text_display.write("Goal!", align="center", font=("Arial", 30, "bold"))
    else:
        text_display.write("Miss!", align="center", font=("Arial", 30, "bold"))

# Thiết lập sự kiện khi ấn phím Space
def on_space():
    move_ball()
    check_goal()
def on_enter():
    prepare_restart()

# Hàm chuẩn bị chơi lại trò chơi
def prepare_restart():
    ball.goto(-350, 0)
    text_display.clear()

# Kết nối sự kiện với phím Space
window.listen()
window.onkeypress(on_space, "space")
window.onkeypress(on_enter, "Return")

# Khởi chạy chương trình
window.mainloop()
