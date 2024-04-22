import RPi.GPIO as GPIO
import tkinter as tk

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
BLUE_LED = 2
RED_LED = 3
GREEN_LED = 4
GPIO.setup(BLUE_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)

def turn_off_all():
    GPIO.output(BLUE_LED, GPIO.LOW)
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.LOW)

def turn_on(led_pin):
    turn_off_all()
    if led_pin is not None:
        GPIO.output(led_pin, GPIO.HIGH)

def select_led(led_color):
    if led_color.lower() in color_pin_mapping:
        turn_on(color_pin_mapping[led_color.lower()])
    else:
        turn_off_all()

def exit_program():
    GPIO.cleanup()
    root.destroy()

root = tk.Tk()
root.title("LED Controller")

def set_color():
    color = color_entry.get()
    select_led(color)

canvas = tk.Canvas(root, width=200, height=150)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relwidth=1, relheight=1)

color_label = tk.Label(root, text="Enter LED Color:", bg='#80c1ff', font=('Arial', 12))
color_label.pack(anchor=tk.W)

color_entry = tk.Entry(root, font=('Arial', 12))
color_entry.pack(anchor=tk.W)

set_color_button = tk.Button(root, text="Set Color", bg='#80c1ff', font=('Arial', 12), command=set_color)
set_color_button.pack(anchor=tk.W)

exit_button = tk.Button(root, text="Exit", bg='#f08080', font=('Arial', 12), command=exit_program)
exit_button.pack()

root.mainloop()
