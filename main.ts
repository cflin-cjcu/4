input.onGesture(Gesture.Shake, function () {
    time = randint(200, 400)
    t = 1
})
function show (num: number, t: number) {
    if (num == 0) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `, t)
    }
    if (num == 1) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . # . # .
            . . . . .
            . . . . .
            `, t)
    }
    if (num == 2) {
        basic.showLeds(`
            . . . . .
            . . . # .
            . . # . .
            . # . . .
            . . . . .
            `, t)
    }
    if (num == 3) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            `, t)
    }
    if (num == 4) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . # . .
            . # . # .
            . . . . .
            `, t)
    }
    if (num == 5) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . . . . .
            . # # # .
            . . . . .
            `, t)
    }
}
let index = 0
let time = 0
let t = 0
basic.forever(function () {
    if (time > 0) {
        show(index, t)
        music.playTone(262, 2)
        index += 1
        index = index % 6
        time += -10
        t += 5
    }
})
