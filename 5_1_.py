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

def select_led(led_pin):
    turn_on(led_pin)

def exit_program():
    GPIO.cleanup()
    root.destroy()

root = tk.Tk()
root.title("LED Controller")

def radio_clicked(led):
    select_led(led)

canvas = tk.Canvas(root, width=200, height=150)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relwidth=1, relheight=1)

selected_var = tk.IntVar()

blue_radio = tk.Radiobutton(root, text="Blue", bg='#80c1ff', activebackground='blue', font=('Arial', 12), variable=selected_var, value=BLUE_LED, command=lambda: radio_clicked(BLUE_LED))
blue_radio.pack(anchor=tk.W)

red_radio = tk.Radiobutton(root, text="Red", bg='#80c1ff', activebackground='red', font=('Arial', 12), variable=selected_var, value=RED_LED, command=lambda: radio_clicked(RED_LED))
red_radio.pack(anchor=tk.W)

green_radio = tk.Radiobutton(root, text="Green", bg='#80c1ff', activebackground='green', font=('Arial', 12), variable=selected_var, value=GREEN_LED, command=lambda: radio_clicked(GREEN_LED))
green_radio.pack(anchor=tk.W)

no_light_radio = tk.Radiobutton(root, text="No Lights", bg='#80c1ff', font=('Arial', 12), variable=selected_var, value=None, command=lambda: radio_clicked(None))
no_light_radio.pack(anchor=tk.W)

no_light_radio.select()

exit_button = tk.Button(root, text="Exit", bg='#f08080', font=('Arial', 12), command=exit_program)
exit_button.pack()

root.mainloop()
