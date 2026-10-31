from machine import Pin, SPI
from time import sleep_ms
from ili9341 import Display, color565

touch_cs = Pin(22, Pin.OUT, value=1)
screen_cs = Pin(17, Pin.OUT, value=1)

spi = SPI(
    0,
    baudrate=10_000_000,
    polarity=0,
    phase=0,
    sck=Pin(18),
    mosi=Pin(19),
    miso=Pin(16)
)

screen = Display(
    spi,
    cs=screen_cs,
    dc=Pin(21),
    rst=Pin(20),
    width=240,
    height=320,
    rotation=0
)

button1 = Pin(0, Pin.IN, Pin.PULL_UP)
button2 = Pin(1, Pin.IN, Pin.PULL_UP)
button3 = Pin(2, Pin.IN, Pin.PULL_UP)
button4 = Pin(3, Pin.IN, Pin.PULL_UP)
button5 = Pin(4, Pin.IN, Pin.PULL_UP)
button6 = Pin(5, Pin.IN, Pin.PULL_UP)

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0

last1 = 1
last2 = 1
last3 = 1
last4 = 1
last5 = 1
last6 = 1

black = color565(0, 0, 0)
red = color565(255, 70, 70)
orange = color565(255, 170, 40)
yellow = color565(255, 230, 60)
green = color565(60, 230, 100)
blue = color565(60, 180, 255)
purple = color565(210, 100, 255)

screen.clear(black)

screen.fill_rectangle(8, 10, 5, 36, red)
screen.draw_text8x8(23, 13, "Button 1", red)
screen.draw_text8x8(23, 32, "Count: 0", red)

screen.fill_rectangle(8, 60, 5, 36, orange)
screen.draw_text8x8(23, 63, "Button 2", orange)
screen.draw_text8x8(23, 82, "Count: 0", orange)

screen.fill_rectangle(8, 110, 5, 36, yellow)
screen.draw_text8x8(23, 113, "Button 3", yellow)
screen.draw_text8x8(23, 132, "Count: 0", yellow)

screen.fill_rectangle(8, 160, 5, 36, green)
screen.draw_text8x8(23, 163, "Button 4", green)
screen.draw_text8x8(23, 182, "Count: 0", green)

screen.fill_rectangle(8, 210, 5, 36, blue)
screen.draw_text8x8(23, 213, "Button 5", blue)
screen.draw_text8x8(23, 232, "Count: 0", blue)

screen.fill_rectangle(8, 260, 5, 36, purple)
screen.draw_text8x8(23, 263, "Button 6", purple)
screen.draw_text8x8(23, 282, "Count: 0", purple)

while True:
    state1 = button1.value()
    if state1 != last1:
        sleep_ms(25)
        state1 = button1.value()
        if state1 != last1:
            last1 = state1
            if state1 == 0:
                count1 += 1
                screen.fill_rectangle(23, 32, 210, 8, black)
                screen.draw_text8x8(23, 32, "Count: " + str(count1), red)

    state2 = button2.value()
    if state2 != last2:
        sleep_ms(25)
        state2 = button2.value()
        if state2 != last2:
            last2 = state2
            if state2 == 0:
                count2 += 1
                screen.fill_rectangle(23, 82, 210, 8, black)
                screen.draw_text8x8(23, 82, "Count: " + str(count2), orange)

    state3 = button3.value()
    if state3 != last3:
        sleep_ms(25)
        state3 = button3.value()
        if state3 != last3:
            last3 = state3
            if state3 == 0:
                count3 += 1
                screen.fill_rectangle(23, 132, 210, 8, black)
                screen.draw_text8x8(23, 132, "Count: " + str(count3), yellow)

    state4 = button4.value()
    if state4 != last4:
        sleep_ms(25)
        state4 = button4.value()
        if state4 != last4:
            last4 = state4
            if state4 == 0:
                count4 += 1
                screen.fill_rectangle(23, 182, 210, 8, black)
                screen.draw_text8x8(23, 182, "Count: " + str(count4), green)

    state5 = button5.value()
    if state5 != last5:
        sleep_ms(25)
        state5 = button5.value()
        if state5 != last5:
            last5 = state5
            if state5 == 0:
                count5 += 1
                screen.fill_rectangle(23, 232, 210, 8, black)
                screen.draw_text8x8(23, 232, "Count: " + str(count5), blue)

    state6 = button6.value()
    if state6 != last6:
        sleep_ms(25)
        state6 = button6.value()
        if state6 != last6:
            last6 = state6
            if state6 == 0:
                count6 += 1
                screen.fill_rectangle(23, 282, 210, 8, black)
                screen.draw_text8x8(23, 282, "Count: " + str(count6), purple)

    sleep_ms(5)