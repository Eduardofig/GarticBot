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

row_vec = [1, 0, -1, 0]
col_vec = [0, -1, 0, 1]
visited = []
for i in range(width):
    col = []
    for j in range(height):
        col.append(False)
    visited.append(col)

def is_valid(x, y):
    return imagem_gray.getpixel((x, y)) < VALOR_MINIMO and not visited[x][y] and x < width and y < height and x >= 0 and y >= 0

def draw_dfs(x, y, pressed = False):
    visited[x][y] = True
    m.move(x + UPPER_LEFT[0], y + UPPER_LEFT[1])
    if(not pressed): 
        m.press(x, y)
        pressed = True
    backtrack = False
    for i in range(4):
        if(backtrack):
            m.release(x + UPPER_LEFT[0], y + UPPER_LEFT[1])
            pressed = False
        if(is_valid(x + row_vec[i], y + col_vec[i])): 
            draw_dfs(x + row_vec[i], y + col_vec[i], pressed)
            backtrack = True

for x in range(width):
    for y in range(height):
        if(is_valid(x, y)):
            draw_dfs(x, y)
            time.sleep(0.0083)

