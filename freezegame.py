import pyglet

win = pyglet.window.Window()

water= pyglet.image.load('images/assets/ground/graphics-tiles-waterflow.png')
spr1 = pyglet.sprite.Sprite(water, x=0, y =0)
spr1.scale = 4

land= pyglet.image.load('images/assets/ground/snow_stones.png')
spr2 = pyglet.sprite.Sprite(land, x=135, y =55)
spr2.scale = 1.5

talltree= pyglet.image.load('images/assets/ground/tall_snow_tree.png')
spr3 = pyglet.sprite.Sprite(talltree, x=380, y =310)
spr3.scale = 1

shorttree= pyglet.image.load('images/assets/ground/short_snow_tree.png')
spr4 = pyglet.sprite.Sprite(shorttree, x=160, y =95)
spr4.scale = 0.8

fire= pyglet.image.load('images/assets/ground/litfire.png')
spr5 = pyglet.sprite.Sprite(fire, x=300, y =235)
spr5.scale = 0.8

player= pyglet.image.load('images/assets/girl/girl_stand.png')
playerleft= pyglet.image.load('images/assets/girl/girl_walk_left.png')
playerright= pyglet.image.load('images/assets/girl/girl_walk_right.png')
playerup= pyglet.image.load('images/assets/girl/girl_walk_up.png')
playerdown= pyglet.image.load('images/assets/girl/girl_walk_down.png')
spr6 = pyglet.sprite.Sprite(player, x=285, y =235)
spr6.scale = 1

# Get the key state handler object
keys = pyglet.window.key.KeyStateHandler()

def update(dt):
    win.push_handlers(keys) # update the key object
    spr6.image = player
    if keys[pyglet.window.key.UP]:
        print("Up key pressed!")
        spr6.image = playerup
        spr6.y+=2
    if keys[pyglet.window.key.DOWN]:
        print("Down key pressed!")
        spr6.image = playerdown
        spr6.y-=2
    if keys[pyglet.window.key.LEFT]:
        print("Left key pressed!")
        spr6.image = playerleft
        spr6.x-=2
    if keys[pyglet.window.key.RIGHT]:
        print("Right key pressed!")
        spr6.image = playerright
        spr6.x+=2


@win.event
def on_draw():
    win.clear()
    #img.blit(200, 100)
    spr1.draw()
    spr2.draw()
    spr3.draw()
    spr4.draw()
    spr5.draw()
    spr6.draw()

pyglet.clock.schedule(update)
pyglet.app.run()