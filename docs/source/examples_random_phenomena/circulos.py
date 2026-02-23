#https://pyglet-readthedocs-io.translate.goog/en/latest/modules/shapes.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

import pyglet
from pyglet import shapes

window = pyglet.window.Window(800, 600)

batch = pyglet.graphics.Batch()

x0 = 100
y0 = 200
radio = 20

# color=(50, 225, 30)

def Label(x0=0, y0=0, let=''):
  label = pyglet.text.Label(
    let,
    font_name='Times New Roman',
    font_size=24,
    color=(255, 255, 255),
    x= x0, y= y0,
    anchor_x='center', anchor_y='center'
  )
  label.draw()


def Circulo(x0=0, y0=0, let=''):
  circle = shapes.Circle(x0, y0, radio, color=(50, 225, 30), batch=batch)

  label = pyglet.text.Label(
    let,
    font_name='Times New Roman',
    font_size=24,
    color=(0, 0, 0),
    x= x0, y= y0,
    anchor_x='center', anchor_y='center'
  )
  batch.draw()
  label.draw()

  
@window.event

def on_draw():
    window.clear()
    Label(400,500, 'Una caja tiene s bolas')
    for i in range(5):
      j=i+1
      let = str(j)
      Circulo(100+i*100,300, let)

    Label(550,300, '...')
    Circulo(600,300, 's')

pyglet.app.run()

