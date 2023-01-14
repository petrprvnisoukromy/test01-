from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True
pink = (255, 0, 221)
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
RED = (255, 0, 0)
bila = (255,255,255)
nothing = (0,0,0)
Oranzova = (255, 128, 0 )
Tmave_cervena = (204, 0, 0)
Svetle_modra = (102, 178, 255)
Tmave_modra = (0, 0, 204)



def trinket_logo():
    G = green
    Y = yellow
    B = blue
    a = nothing
    o = Oranzova
    C = Tmave_cervena
    m = Svetle_modra
    t = Tmave_modra
    W = bila
    R = RED
    p = pink 
    
    logo = [
    a, a, t, t, m, m, a, a,
    a, B, m, W, W, B, t, a,
    a, t, t, a, W, m, B, a,
    a, a, B, B, B, m, a, a,
    W, W, o, R, R, o, W, W,
    W, C, o, W, a, o, R, W,
    W, C, R, W, W, C, R, W,
    W, W, R, o, R, C, W, W
    ]
    return logo

def raspi_logo():
    G = green
    R = RED
    O = nothing
    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo

def plus():
    O = nothing
    W = bila
    logo = [
    O, O, O, O, O, O, O, O, 
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def equals():
    W = bila
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def heart():
    P = pink
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

images = [trinket_logo, plus, raspi_logo, equals,  heart]
count = 0
while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1