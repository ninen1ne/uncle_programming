# 22/03/2025 - Nine
import os

PATH = os.getcwd()

def save(filename):
    save_loc = os.path.join(PATH, 'imgs', filename +'.png')
    print(save_loc)

save('yolle')