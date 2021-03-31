bug: game.LedSprite = None
angle = 0

def on_forever():
    global bug, angle
    bug = game.create_sprite(2, 2)
    while True:
        angle = randint(0, 360)
        bug.turn(Direction.RIGHT, angle)
        bug.move(1)
        basic.pause(100)
basic.forever(on_forever)
