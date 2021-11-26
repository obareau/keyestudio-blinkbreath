let val = 0
led.enable(false)
basic.forever(function () {
    for (let index = 0; index < 2; index++) {
        pins.digitalWritePin(DigitalPin.P0, 1)
        basic.pause(1000)
        pins.digitalWritePin(DigitalPin.P0, 0)
        basic.pause(1000)
        for (let index = 0; index < 2; index++) {
            while (val > 1024) {
                val = val + 1
                basic.pause(5)
            }
            while (val > 0) {
                val = val - 1
                basic.pause(5)
            }
        }
    }
})
