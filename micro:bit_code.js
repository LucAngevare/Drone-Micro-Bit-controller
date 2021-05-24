input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . # . .
        . # . # .
        . # # # .
        . # . # .
        . # . # .
        `)
    sendQueue.push("DRONE: takeoff;")
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . # # . .
        . # . # .
        . # # # .
        . # . # .
        . # # . .
        `)
    sendQueue.push("DRONE: land;")
})
let sendQueue: string[] = []
serial.redirect(
SerialPin.USB_TX,
SerialPin.USB_RX,
BaudRate.BaudRate19200
)
basic.forever(function () {
    while (sendQueue.length > 0) {
        serial.writeLine("" + (sendQueue.shift()))
        basic.showNumber(sendQueue.length)
    }
})
