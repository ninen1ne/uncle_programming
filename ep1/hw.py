# 28 Dec 2024 - Nine
# Homework instruction: draw 10 square in a random position
import turtle as tao, random

class Shape:
    def __init__(self):
        pass

    def random_pos(self, rand_range=(-200, 200)):
        x_pos = random.randint(*rand_range)
        y_pos = random.randint(*rand_range)
        pos = (x_pos, y_pos)
        return pos

    def draw_circles(self, random_radius=False ,radius=100, random_pos=False, count=10, speed=5):
        angle = 360 / count
        colors = ['red', 'green', 'blue']
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
            color = random.choice(colors)
            tao.color(color)
            tao.circle(radius=radius)
            tao.left(angle) # หันหน้าเอียงทีละกี่องศา
            print(f"หมุนครั้งที่: {i + 1}")
        print("END")
        tao.Screen().exitonclick()

c1 = Shape()
c1.draw_circles(random_radius=False, random_pos=True)