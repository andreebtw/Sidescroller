from cmu_graphics import *

import math 
import os

app.stepsPerSecond = 60
app.gravity = 0.2

thisFolder = os.path.dirname(os.path.realpath(__file__))
bg1 = Image(thisFolder + '/bg1.png', 0, 0)
bg2 = Image(thisFolder + '/bg2.png', 400, 0)

pf = Image(thisFolder + '/pf.png', 800, 150, width=250)

cr = Image(thisFolder + '/cr.png', 600, 237, width=50, height=50)


b1 = Image(thisFolder + '/b1.png', 50, 197, width=50, height=90)

b2 = Image(thisFolder + '/b2.png', 50, 197, width=50, height=90)
b2.visible=False

b3 = Image(thisFolder + '/b3.png', 50, 197, width=50, height=90)
b3.visible=False

b4 = Image(thisFolder + '/b4.png', 50, 197, width=53, height=90)
b4.visible=False

p = Group(
b1, b2, b3, b4
)

p.vx = 0
p.vy = 0
p.grounded = False
app.counter = 0
speed = 15

def onStep():

    checkCollision(pf)

    bg1.centerX -= 1
    bg2.centerX -= 1
    pf.centerX -= 1.5
    cr.centerX -= 1

    if pf.centerX <= -800:
        pf.centerX = 800

    if cr.centerX <= -600:
        cr.centerX = 600

    if bg2.centerX <= -200:
        bg2.centerX = 600

    if bg1.centerX <= -200:
        bg1.centerX = 600
    
    if p.grounded == True:
        app.counter += 1
        

    if app.counter == speed:
        app.counter = 0
        if b1.visible == True:
            b2.visible = True
            b1.visible = False
        
        elif b2.visible == True:
            b3.visible = True
            b2.visible = False
        
        elif b3.visible == True:
            b4.visible = True
            b3.visible = False
        
        elif b4.visible == True:
            b1.visible = True
            b4.visible = False
    
    p.centerX += p.vx
    p.centerY += p.vy
    p.vy += app.gravity
    
    if p.bottom >= 287:
        p.vy = 0
        p.bottom = 287
        p.grounded = True
     
def onKeyPress(keys):
    if ('space' in keys) and (p.grounded):
        p.vy -= 8
        p.grounded = False
        b1.visible = True
        b2.visible = False
        b3.visible = False
        b4.visible = False

def checkCollision(ground):
    x1, y1 = getPointInDir(p.centerX + 45, p.bottom, 180, 1)
    x2, y2 = getPointInDir(p.centerX - 45, p.bottom, 180, 1)
    
    if((ground.contains(x1, y1) or ground.contains(x2, y2)) and p.vy > 0):
        p.vy = 0
        p.bottom = ground.top
        p.grounded = True

cmu_graphics.run()