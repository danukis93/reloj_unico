a = 0
b = 0
c = 0
def setup ():
    size (350, 350)
def draw():
    global a
    global b
    global c
    square(a, 20, 55)
    if a > height:
       a = 0
    else:
       a = map(second(), 0, 59, 0, height)
    square(b, 140, 55)
    if b > height:
       b = 0
    else:
       b = map(minute(), 0, 59, 0, height)
    square(c, 280, 55)
    if c > height:
       c = 0
    else:
       c = map(hour(), 0, 59, 0, height)
