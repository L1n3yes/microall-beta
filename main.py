dice = 0
def NOUSE():
    # this version will only show beta stuff and NOT STUFF FROM MICRO:ALL
    basic.show_string("read comment")

def on_forever():
    pass
basic.forever(on_forever)

def on_forever2():
    global dice
    dice = randint(1, 6)
    if dice == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    elif dice == 2:
        basic.show_leds("""
            . . . . .
            . . . . .
            . # . # .
            . . . . .
            . . . . .
            """)
    elif dice == 3:
        basic.show_leds("""
            . . . . .
            . . . . .
            # . # . #
            . . . . .
            . . . . .
            """)
    elif dice == 4:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . . . .
            . . . . .
            # . . . #
            """)
    elif dice == 5:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . #
            """)
    elif dice == 6:
        basic.show_leds("""
            # . . . #
            . . . . .
            # . . . #
            . . . . .
            # . . . #
            """)
    else:
        pass
basic.forever(on_forever2)
