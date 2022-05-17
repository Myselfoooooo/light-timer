def on_button_pressed_b():
    global minutes, displaying
    minutes = totaltime / 60000
    if timing:
        minutes += (input.running_time() - starttime) / 60000
    displaying = False
    basic.clear_screen()
    basic.show_number(minutes)
    basic.pause(500)
    displaying = True
input.on_button_pressed(Button.B, on_button_pressed_b)

endtime = 0
starttime = 0
timing = False
totaltime = 0
minutes = 0
displaying = False
basic.show_string("L")
LIGHT = 253
HYSTERESIS = 8
LIGHT += HYSTERESIS / 2
DARK = LIGHT - HYSTERESIS
reading = input.light_level()
basic.pause(1000)
displaying = True

def on_forever():
    global reading, endtime, totaltime, timing, starttime
    reading = input.light_level()
    if reading < DARK:
        if timing:
            endtime = input.running_time()
            totaltime += endtime - starttime
            timing = False
    elif reading >= LIGHT:
        if not (timing):
            starttime = input.running_time()
            timing = True
basic.forever(on_forever)

def on_forever2():
    if displaying:
        if timing:
            basic.show_leds("""
                # # # # #
                                # # # # #
                                # # # # #
                                # # # # #
                                # # # # #
            """)
        else:
            basic.show_leds("""
                . . . . .
                                . . # . .
                                . # # # .
                                . . # . .
                                . . . . .
            """)
basic.forever(on_forever2)
