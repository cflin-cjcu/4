def on_gesture_shake():
    global time, t
    time = randint(200, 400)
    t = 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def show(num: number, t: number):
    if num == 0:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """,
            t)
    if num == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . # . # .
            . . . . .
            . . . . .
            """,
            t)
    if num == 2:
        basic.show_leds("""
            . . . . .
            . . . # .
            . . # . .
            . # . . .
            . . . . .
            """,
            t)
    if num == 3:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            """,
            t)
    if num == 4:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . # . .
            . # . # .
            . . . . .
            """,
            t)
    if num == 5:
        basic.show_leds("""
            . . . . .
            . # # # .
            . . . . .
            . # # # .
            . . . . .
            """,
            t)
index = 0
time = 0
t = 0

def on_forever():
    global index, time, t
    if time > 0:
        show(index, t)
        music.play_tone(262, 2)
        index += 1
        index = index % 6
        time += -10
        t += 5
basic.forever(on_forever)
