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
    Label(300,500, 'Consideremos el siguiente experimento')
    Label(330, 450, 'Las bolas se mezclan bien en la caja y una persona')
    Label(300, 420, 'mete la mano en la caja y saca una bola.')
    Label(300, 390, 'Se anota el número de la bola y se devuelve la bola a la caja.')
    Label(300, 360, 'El resultado del experimento es el número de la bola seleccionado.')

pyglet.app.run()

