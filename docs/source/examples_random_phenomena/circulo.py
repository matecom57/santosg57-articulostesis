#https://pyglet-readthedocs-io.translate.goog/en/latest/modules/shapes.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

import pyglet
from pyglet import shapes

window = pyglet.window.Window(800, 600)

batch = pyglet.graphics.Batch()

x0 = 100
y0 = 200
radio = 20

def Circulo(x0=0, y0=0):
  circle = shapes.Circle(x0, y0, radio, color=(50, 225, 30), batch=batch)
  batch.draw()

label = pyglet.text.Label(
    '1',
    font_name='Times New Roman',
    font_size=24,
    x= x0, y= y0,
    anchor_x='center', anchor_y='center'
)

@window.event

def on_draw():
    window.clear()
    Circulo(200,300)
    label.draw()

pyglet.app.run()

