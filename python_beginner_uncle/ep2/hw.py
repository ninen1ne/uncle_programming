# 28 Dec 2024 - Nine
# Homework instruction: draw 10 square in a random position
import turtle as tao, random

class Shape:
    def __init__(self):
        self.color_range = "0123456789abcdef"
        self.colors = ['red', 'green', 'blue', 'yellow', 'pink', 'violet', 'black']

    def create_hex_color(self):
        hex_color = "#"
        for i in range(6):
            hex_color += self.color_range[random.randint(0, 15)]
        return hex_color

    def random_pos(self, rand_range=(-200, 200)):
        x_pos = random.randint(*rand_range)
        y_pos = random.randint(*rand_range)
        pos = (x_pos, y_pos)
        return pos

    def draw_circles(self, random_radius=False ,radius=100, random_pos=False, count=10, speed=5):
        print(f"Draw {count} circles" if count > 1 else "Draw a circle.")
        angle = 360 / count
        tao.speed(speed)
        tao.pensize(3)
        for i in range(count):
            if random_radius:
                radius = random.randint(10, 100)
            if random_pos:
                position = self.random_pos()
                tao.penup()
                tao.goto(*position)
                tao.pendown()
            # color = random.choice(self.colors)
            color = self.create_hex_color()
            tao.color(color)
            tao.circle(radius=radius)
            tao.left(angle) # หันหน้าเอียงทีละกี่องศา
            print(f"วาดครั้งที่: {i + 1} || color: {color}")
        print("END")
        # tao.Screen().exitonclick()

    def draw_squares(self, random_pos=False, random_length=False, length=100, count=10, speed=5):
        print(f"Draw {count} squares" if count > 1 else "Draw a square.")
        tao.speed(speed)
        tao.pensize(3)
        for i in range(count):
            if random_pos:
                position = self.random_pos()
                tao.penup()
                tao.goto(*position)
                tao.pendown()
            if random_length:
                length = random.randint(25, 150)
            # color = random.choice(self.colors)
            color = self.create_hex_color()
            tao.color(color)
            for j in range(4):
                tao.forward(length)
                tao.left(90)
            print(f"วาดครั้งที่ {i + 1} || color: {color}")
        print("END")
        # tao.Screen().exitonclick()


c1 = Shape()
c1.draw_circles(random_radius=True, random_pos=True, count=10)
c1.draw_squares(random_pos=True, random_length=True, count=15)
tao.Screen().exitonclick()