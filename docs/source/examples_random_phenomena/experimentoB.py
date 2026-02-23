#https://pyglet-readthedocs-io.translate.goog/en/latest/modules/shapes.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

import pyglet
from pyglet import shapes

window = pyglet.window.Window(800, 600)

batch = pyglet.graphics.Batch()

x0 = 100
y0 = 200
radio = 20

# color=(50, 225, 30)

ll = ['Supongamos que repetimos el experimento anterior n veces',
'Sea Nn(k) el número de veces que se extrajo la bola etiquetada',
'como k durante estos n ensayos del experimento.',
'Supongamos que tuviéramos, digamos, s=3 bolas y n=20 ensayos',
'Un resultado tipico podría ser',
'1, 1, 3,2,1,2,2,3,2,3,3,2,1,2,3,3,1,3,2,2']


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
    del1 = 40
    y0 = 500
    delx = 100
    x0=300
    n = len(ll)
    for i in range(n):
      Label
    Label(x0+delx,y0, 'Supongamos que repetimos el experimento anterior n veces')
    Label(x0+delx,y0-del1, 'Sea Nn(k) el número de veces que se extrajo la bola etiquetada')
    Label(x0+delx,y0-2*del1, 'como k durante estos n ensayos del experimento.')
    Label(x0+delx,y0 - 3*del1, 'Supongamos que tuviéramos, digamos, s=3 bolas y n=20 ensayos')
    Label(x0+delx, y0 - 4*del1, 'Un resultado tipico podría ser')
    Label(x0+delx, y0 - 5*del1, '1, 1, 3,2,1,2,2,3,2,3,3,2,1,2,3,3,1,3,2,2')
    Label(x0+delx, y0 - 6*del1, r"some fancy label and $a < \gamma$")

pyglet.app.run()

