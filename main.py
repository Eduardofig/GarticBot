from PIL import Image, ImageOps,ImageEnhance
from pymouse import PyMouse
import time

UPPER_LEFT = (457, 226)
LOWER_BOTTOM = (731, 441)
VALOR_MINIMO = 73

m = PyMouse()
print(m.position())

nome_da_imagem = input("Qual o arquivo da imagem: ")

imagem = Image.open(nome_da_imagem)
resize_image = imagem.resize((LOWER_BOTTOM[0] - UPPER_LEFT[0], LOWER_BOTTOM[1] - UPPER_LEFT[1]))

contraste = (float)(input("Quanto você quer de constraste: "))
# Põe o contraste
enhancer = ImageEnhance.Contrast(resize_image)
imagem_contraste = enhancer.enhance(contraste)

imagem_gray = ImageOps.grayscale(imagem_contraste)

pixels = imagem_gray.load()

width, height = imagem_gray.size
m = PyMouse()

for x in range(width):
    for y in range(height):
        
        if(imagem_gray.getpixel((x, y)) < VALOR_MINIMO):
            m.click(x + UPPER_LEFT[0], y + UPPER_LEFT[1])
            time.sleep(0.0083)

