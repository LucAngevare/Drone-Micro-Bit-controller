input.onLogoEvent(TouchButtonEvent.LongPressed, function () {
    sendQueue.push("DRONE: land;")
    takenoff = 0
    basic.showLeds(`
        . . # . .
        . . # . .
        . . # . .
        . . . . .
        . . # . .
        `)
})
input.onButtonPressed(Button.A, function () {
    if (takenoff) {
        sendQueue.push("DRONE: up 50;")
    } else {
        sendQueue.push("DRONE: takeoff;")
        takenoff = 1
    }
    basic.showLeds(`
        . . # . .
        . # # # .
        # . # . #
        . . # . .
        . . # . .
        `)
})
input.onButtonPressed(Button.B, function () {
    sendQueue.push("DRONE: down 50;")
    basic.showLeds(`
        . . # . .
        . . # . .
        # . # . #
        . # # # .
        . . # . .
        `)
})
let takenoff = 0
let sendQueue: string[] = []
serial.redirect(
SerialPin.USB_TX,
SerialPin.USB_RX,
BaudRate.BaudRate19200
)
basic.forever(function () {
	
})
basic.forever(function () {
    if (input.isGesture(Gesture.LogoUp)) {
        sendQueue.push("DRONE: back 40;")
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . # . # .
            . . # . .
            `)
    } else if (input.isGesture(Gesture.LogoDown)) {
        sendQueue.push("DRONE: forward 40;")
        basic.showLeds(`
            . . # . .
            . # . # .
            . . . . .
            . . . . .
            . . . . .
            `)
    } else if (input.isGesture(Gesture.TiltLeft)) {
        sendQueue.push("DRONE: ccw 45;")
        basic.showLeds(`
            . . . . .
            . # . . .
            # . . . .
            . # . . .
            . . . . .
            `)
    } else if (input.isGesture(Gesture.TiltRight)) {
        sendQueue.push("DRONE: cw 45;")
        basic.showLeds(`
            . . . . .
            . . . # .
            . . . . #
            . . . # .
            . . . . .
            `)
    } else {
    	
    }
})
basic.forever(function () {
    basic.showLeds(`
        . . . . .
        . . # . .
        . # # # .
        . . # . .
        . . . . .
        `)
    while (sendQueue.length > 0) {
        serial.writeLine("" + (sendQueue.shift()))
    }
})
