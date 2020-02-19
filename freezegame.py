import pyglet

win = pyglet.window.Window()

water= pyglet.image.load('images/assets/graphics-tiles-waterflow.png')
spr1 = pyglet.sprite.Sprite(water, x=0, y =0)
spr1.scale = 4
fire= pyglet.image.load('images/assets/litfire.png')
spr2 = pyglet.sprite.Sprite(fire, x=300, y =200)
spr2.scale = 0.7

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
    win.clear()
    #img.blit(200, 100)
    spr1.draw()
    spr2.draw()

pyglet.clock.schedule(update)
pyglet.app.run()