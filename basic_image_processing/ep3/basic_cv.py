# 22/03/2025 - Nine
import os, cv2

PATH = os.getcwd() # get current working directory

img_path = os.path.join(PATH, "imgs", "aba_char01.png")
sabusa_img = cv2.imread(img_path, cv2.IMREAD_COLOR) # read file and return in matrix form

# print(sabusa_img) 
# print('\n', sabusa_img.shape) # // (height, width, size of matrix column)

#-- resize --
# resized_img = cv2.resize(sabusa_img, (400, 300))
# resized_img = cv2.resize(sabusa_img, (0, 0), fx=0.5, fy=0.5)

#-- crop --
cropped_img = sabusa_img[150:500, 300:800]

#-- save file --
# save_loc = os.path.join(PATH, 'imgs', 'sabusa_cropped.png')
# cv2.imwrite(save_loc, cropped_img) # save cropped img to specific folder

def save_file(filename, img_to_save):
    save_loc = os.path.join(PATH, 'imgs', filename + '.png')
    cv2.imwrite(save_loc, img_to_save)
    print("file already saved.")

save_file('sabusa_cropped_001', cropped_img)

#-- display --
# cv2.imshow('image', cropped_img) # show file
# cv2.waitKey(0)
# cv2.destroyAllWindows()