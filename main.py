val = 0
led.enable(False)

def on_forever():
    global val
    for index in range(2):
        pins.digital_write_pin(DigitalPin.P0, 1)
        basic.pause(1000)
        pins.digital_write_pin(DigitalPin.P0, 0)
        basic.pause(1000)
    for index2 in range(2):
        while val < 1024:
            val = val + 4
            pins.analog_write_pin(AnalogPin.P0, val)
            basic.pause(5)
        while val > 0:
            val = val - 4
            pins.analog_write_pin(AnalogPin.P0, val)
            basic.pause(5)
basic.forever(on_forever)
