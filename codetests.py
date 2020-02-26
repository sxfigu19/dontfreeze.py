import pyglet
win = pyglet.window.Window()

def draw_rect(x, y, width, height):
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
        ('v2f', [x, y, x + width, y, x + width, y + height, x, y + height]))

@win.event
def on_draw():
        win.clear()
        draw_rect(50, 50, 30, 10)

pyglet.app.run()
# "hp" : 100,