import tkinter as tk
import math


# ---------------------------
# ONA Sphere AI v0.1
# 360도 방향 구슬 시뮬레이션
# ---------------------------

window = tk.Tk()
window.title("ONA Sphere AI 🌌")
window.geometry("500x500")


canvas = tk.Canvas(window, width=500, height=500, bg="black")
canvas.pack()


center_x = 250
center_y = 250

radius = 120

angle = 0


# 중심 코어
canvas.create_oval(
    center_x-25,
    center_y-25,
    center_x+25,
    center_y+25,
    fill="white"
)


# 원형 구조
canvas.create_oval(
    center_x-radius,
    center_y-radius,
    center_x+radius,
    center_y+radius,
    outline="gray",
    width=2
)


# 방향 표시
for deg in range(0, 360, 30):
    x = center_x + math.cos(math.radians(deg)) * radius
    y = center_y + math.sin(math.radians(deg)) * radius

    canvas.create_oval(
        x-5,
        y-5,
        x+5,
        y+5,
        fill="gray"
    )


# 움직이는 구슬
ball = canvas.create_oval(
    center_x-10,
    center_y-radius-10,
    center_x+10,
    center_y-radius+10,
    fill="cyan"
)


def move_ball():
    global angle

    angle += 2

    x = center_x + math.cos(math.radians(angle)) * radius
    y = center_y + math.sin(math.radians(angle)) * radius

    canvas.coords(
        ball,
        x-10,
        y-10,
        x+10,
        y+10
    )

    window.after(30, move_ball)


move_ball()

window.mainloop()