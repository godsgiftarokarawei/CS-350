#!/usr/bin/env python3
"""
CS 350 Final Project - Thermostat Controller
Author: Godsgift Arokarawei
Date: 2025-08-11
Description:
    Raspberry Pi thermostat controller using:
    - AHT20 temp/humidity sensor (I2C)
    - 3 pushbuttons: Mode toggle, Temp Up, Temp Down
    - 2 LEDs: Heating (Red), Cooling (Blue)
    - 16x2 LCD via I2C
    - UART for telemetry output
"""

import time
import serial
from datetime import datetime
from gpiozero import Button, PWMLED
import board
import adafruit_ahtx0
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# ------------------ CONFIGURATION ------------------
# GPIO Pins for LEDs and Buttons
HEAT_LED_PIN = 17
COOL_LED_PIN = 27
BTN_MODE_PIN = 5
BTN_UP_PIN = 6
BTN_DOWN_PIN = 13

# Setpoint Defaults
DEFAULT_SETPOINT = 24.0  # Celsius
TEMP_STEP = 0.5          # Step for up/down

# UART Settings
UART_PORT = "/dev/serial0"
UART_BAUD = 9600

# LCD Settings
LCD_COLUMNS = 16
LCD_ROWS = 2

# ------------------ HARDWARE INIT ------------------
# LEDs
heat_led = PWMLED(HEAT_LED_PIN)
cool_led = PWMLED(COOL_LED_PIN)

# Buttons
btn_mode = Button(BTN_MODE_PIN, bounce_time=0.2)
btn_up = Button(BTN_UP_PIN, bounce_time=0.2)
btn_down = Button(BTN_DOWN_PIN, bounce_time=0.2)

# I2C Bus & Sensors
i2c = board.I2C()
aht20 = adafruit_ahtx0.AHTx0(i2c)
lcd = character_lcd.Character_LCD_I2C(i2c, LCD_COLUMNS, LCD_ROWS)

# UART Serial
uart = serial.Serial(UART_PORT, UART_BAUD, timeout=1)

# ------------------ STATE MACHINE ------------------
class ThermostatState:
    OFF = "OFF"
    HEATING = "HEATING"
    COOLING = "COOLING"

current_state = ThermostatState.OFF
setpoint = DEFAULT_SETPOINT

# ------------------ EVENT HANDLERS ------------------
def handle_mode():
    global current_state
    if current_state == ThermostatState.OFF:
        current_state = ThermostatState.HEATING
    elif current_state == ThermostatState.HEATING:
        current_state = ThermostatState.COOLING
    else:
        current_state = ThermostatState.OFF
    print(f"[DEBUG] Mode changed to: {current_state}")

def handle_up():
    global setpoint
    setpoint += TEMP_STEP
    print(f"[DEBUG] Setpoint increased to: {setpoint:.1f}°C")

def handle_down():
    global setpoint
    setpoint -= TEMP_STEP
    print(f"[DEBUG] Setpoint decreased to: {setpoint:.1f}°C")

btn_mode.when_pressed = handle_mode
btn_up.when_pressed = handle_up
btn_down.when_pressed = handle_down

# ------------------ HELPER FUNCTIONS ------------------
def update_lcd(temp):
    lcd.clear()
    lcd.message = f"T:{temp:.1f}C S:{setpoint:.1f}C\n{current_state}"

def send_uart(temp):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"{timestamp},{temp:.2f},{setpoint:.2f},{current_state}\n"
    uart.write(message.encode())

def control_leds(temp):
    heat_led.value = 0
    cool_led.value = 0
    if current_state == ThermostatState.HEATING:
        if temp < setpoint:
            heat_led.pulse(fade_in_time=1, fade_out_time=1)
        else:
            heat_led.value = 1
    elif current_state == ThermostatState.COOLING:
        if temp > setpoint:
            cool_led.pulse(fade_in_time=1, fade_out_time=1)
        else:
            cool_led.value = 1

# ------------------ MAIN LOOP ------------------
def main():
    print("[INFO] Thermostat starting...")
    while True:
        try:
            temp = aht20.temperature
            update_lcd(temp)
            send_uart(temp)
            control_leds(temp)
            time.sleep(5)
        except KeyboardInterrupt:
            lcd.clear()
            heat_led.off()
            cool_led.off()
            print("\n[INFO] Exiting program.")
            break

if __name__ == "__main__":
    main()