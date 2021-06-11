from PIL import Image, ImageOps, ImageEnhance
from pymouse import PyMouse
import time
import sys

sys.setrecursionlimit(100000)

UPPER_LEFT = (50, 164)
LOWER_BOTTOM = (649, 594)
VALOR_MINIMO = 90

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

width, height = imagem_gray.size
m = PyMouse()

row_vec = [1, 0, -1, 0, 1, 1, -1, -1]
col_vec = [0, -1, 0, 1, 1, -1, -1, 1]

visited = []
pixels = []

for y in range(height):
    col_pix = []
    col = []
    for x in range(width):
        col.append(False)
        col_pix.append(imagem_gray.getpixel((x, y)))
    visited.append(col)
    pixels.append(col_pix)

pressed = False

def is_valid(x, y):
    if(x >= width or y >= height or x < 0 or y < 0): return False
    if(visited[y][x]): return False
    return int(pixels[y][x]) < int(VALOR_MINIMO)

def draw_dfs(x, y, recursion = 0):
    global pressed
    visited[y][x] = True
    m.move(x + UPPER_LEFT[0], y + UPPER_LEFT[1])
    if(not pressed): 
        m.press(x + UPPER_LEFT[0], y + UPPER_LEFT[1])
        pressed = True
    backtrack = False
    for i in range(8):
        if(backtrack):
            if(pressed):
                pos = m.position()
                m.release(pos[0], pos[1])
                pressed = False
        if(is_valid(x + row_vec[i], y + col_vec[i])): 
            time.sleep(0.0007)
            if(recursion > 14000): return
            recursion += 1
            draw_dfs(x + row_vec[i], y + col_vec[i], recursion)
            backtrack = True
    if(pressed):
        pos = m.position()
        m.release(pos[0], pos[1])
        pressed = False

for x in range(width):
    for y in range(height):
        if(is_valid(x, y)):
            draw_dfs(x, y)
