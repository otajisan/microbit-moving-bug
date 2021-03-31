let bug: game.LedSprite = null
let angle = 0
basic.forever(function () {
    bug = game.createSprite(2, 2)
    while (true) {
        angle = randint(0, 360)
        bug.turn(Direction.Right, angle)
        bug.move(1)
        basic.pause(100)
    }
})
