from PIL import Image, ImageDraw

# Создаем новый холст для рисования
width, height = 800, 400
im = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(im)

# ----- Рисуем букву К -----
# Вертикальная линия
draw.line((50, 50, 50, 250), fill="blue", width=20)
# Верхняя косая линия
draw.line((50, 50, 150, 150), fill="blue", width=20)
# Нижняя косая линия
draw.line((50, 250, 150, 150), fill="blue", width=20)

# ----- Рисуем букву И -----
# Вертикальная линия
draw.line((200, 50, 200, 250), fill="red", width=20)
# Верхняя горизонтальная линия
draw.line((175, 50, 225, 50), fill="red", width=20)
# Нижняя горизонтальная линия
draw.line((175, 250, 225, 250), fill="red", width=20)

# ----- Рисуем букву Р -----
# Вертикальная линия
draw.line((275, 50, 275, 250), fill="green", width=20)
# Верхняя горизонтальная линия
draw.line((275, 50, 375, 50), fill="green", width=20)
# Правая вертикальная линия
draw.line((375, 50, 375, 150), fill="green", width=20)
# Дуга
draw.arc((275, 100, 375, 200), 0, 180, fill="green", width=20)

# ----- Рисуем букву И -----
# Вертикальная линия
draw.line((425, 50, 425, 250), fill="orange", width=20)
# Верхняя горизонтальная линия
draw.line((400, 50, 450, 50), fill="orange", width=20)
# Нижняя горизонтальная линия
draw.line((400, 250, 450, 250), fill="orange", width=20)

# ----- Рисуем букву Л -----
# Вертикальная линия
draw.line((500, 50, 500, 250), fill="purple", width=20)
# Нижняя горизонтальная линия
draw.line((500, 250, 600, 250), fill="purple", width=20)

# ----- Рисуем букву Л -----
# Вертикальная линия
draw.line((650, 50, 650, 250), fill="blue", width=20)
# Нижняя горизонтальная линия
draw.line((650, 250, 750, 250), fill="blue", width=20)

# Сохраняем рисунок в файл
im.save("кирилл.png")
