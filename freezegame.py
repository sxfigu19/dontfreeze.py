import pyglet
import util
win = pyglet.window.Window()

title = pyglet.text.Label('Do Not Freeze!', font_size=35, x = 250, y = 450)


# Get the key state handler object
keys = pyglet.window.key.KeyStateHandler()

def update(dt):
    win.push_handlers(keys) # update the key object
    if keys[pyglet.window.key.UP]:
        print("Up key pressed!")
    if keys[pyglet.window.key.DOWN]:
        print("Down key pressed!")
    if keys[pyglet.window.key.LEFT]:
        print("Left key pressed!")
    if keys[pyglet.window.key.RIGHT]:
        print("Right key pressed!")

@win.event
def on_draw():
    util.pixelScale()
    win.clear()
    #img.blit(200, 100)
    title.draw()


pyglet.clock.schedule(update)
pyglet.app.run()