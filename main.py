from PIL import Image, ImageOps
from pymouse import PyMouse

UPPER_LEFT = (359, 488)
LOWER_BOTTOM = (452, 576)
VALOR_MINIMO = 220

imagem = Image.open('anime.jpeg')
resize_image = imagem.resize((LOWER_BOTTOM[0] - UPPER_LEFT[0], LOWER_BOTTOM[1] - UPPER_LEFT[1]))

imagem_gray = ImageOps.grayscale(resize_image)

pixels = imagem_gray.load()

width, height = imagem_gray.size

m = PyMouse()

for x in range(width):
    for y in range(height):
        if(imagem_gray.getpixel((x, y)) < VALOR_MINIMO):
            m.click(x + UPPER_LEFT[0], y + UPPER_LEFT[1])
        
