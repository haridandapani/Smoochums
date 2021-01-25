from PIL import Image
import random

base_hair = (0, 0, 0, 255)
base_eyes = (237, 28, 36, 255)
base_bg = (255, 255, 255, 255)
base_lips = (181, 230, 29, 255)
base_iris = (255, 201, 14, 255)
base_skin = (185, 122, 87, 255)
base_shadow = (209, 163, 121, 255)
base_eye_shadow = (191, 192, 186, 255)
base_eye_whites = (153, 217, 234, 255)

def smoochummaker(hair, eyes, bg, lips, iris, skin, shadow, eye_shadow, eye_whites, other, filename):
    im = Image.open('basesmoochum.png') # Can be many different formats.
    pix = im.load()
    width, height = im.size  # Get the width and hight of the image for iterating over
    for x in range(0, width):
        for y in range(0, height):
            curr = pix[x, y]
            if curr == base_hair:
                pix[x, y] = hair
            elif curr == base_eyes:
                pix[x, y] = eyes
            elif curr == base_bg:
                pix[x, y] = bg
            elif curr == base_lips:
                pix[x, y] = lips
            elif curr == base_iris:
                pix[x, y] = iris
            elif curr == base_skin:
                pix[x, y] = skin
            elif curr == base_shadow:
                pix[x, y] = shadow
            elif curr == base_eye_shadow:
                pix[x, y] = eye_shadow
            elif curr == base_eye_whites:
                pix[x, y] = eye_whites
            else:
                pix[x, y] = other
                

    im.save(filename)

def randomcolor():
    return(randomnumber(), randomnumber(), randomnumber(), 255)

def randomnumber():
    return int(random.random() * 256)

def createrandomsmoochum(filename):
    smoochummaker(randomcolor(), randomcolor(), randomcolor(), randomcolor(), randomcolor(), randomcolor(), randomcolor(), randomcolor(), randomcolor(), randomcolor(), filename)
#print(randomcolor())
#print(randomcolor())
#print(randomcolor())
#print(randomcolor())
