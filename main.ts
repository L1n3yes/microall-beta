input.onButtonPressed(Button.A, function () {
	
})
input.onButtonPressed(Button.B, function () {
    sprite.move(1)
})
let sprite: game.LedSprite = null
sprite = game.createSprite(2, 5)
basic.forever(function () {
    if (sprite.get(LedSpriteProperty.X) == 4) {
        sprite.set(LedSpriteProperty.X, 0)
    }
})
