# 28 Dec 2024 - Nine
import turtle as tao, random

def create_circle(random_radius=False ,radius=100, count=10, speed=5):
    angle = 360 / count
    colors = ['red', 'green', 'blue']
    tao.speed(speed)
    tao.pensize(3)
    if random_radius:
        print('hello')
        for i in range(count):
            radius = random.randint(10, 100)
            color = random.choice(colors)
            tao.color(color)
            tao.circle(radius=radius)
            tao.left(angle) # หันหน้าเอียงทีละกี่องศา
            print(f"หมุนครั้งที่: {i + 1}")
        print("END")
        tao.Screen().exitonclick()
    else:
        print('yolle')
        for i in range(count):
            color = random.choice(colors)
            tao.color(color)
            tao.circle(radius=radius)
            tao.left(angle)
            print(f"หมุนครั้งที่: {i + 1}")
        print("END")
        tao.Screen().exitonclick()

create_circle(random_radius=True, radius=25, count=3) 