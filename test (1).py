import time
import threading
from gpiozero import LED, Button
from RPLCD.i2c import CharLCD
from statemachine import StateMachine, State

# GPIO pin setup
red_led = LED(18)     # Dot
blue_led = LED(23)    # Dash
button = Button(24)
lcd = CharLCD('PCF8574', 0x27)

# Morse Code dictionary
MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.',  'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--', 'N': '-.',   'O': '---',  'P': '.--.',
    'Q': '--.-','R': '.-.', 'S': '...',  'T': '-',
    'U': '..-','V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--','Z': '--..', ' ':' '
}

# Timing
DOT = 0.5
DASH = 1.5
INTRA = 0.25
LETTER = 0.75
WORD = 3

# Messages
messages = ["HELLO WORLD", "SOS DANGER"]
message_index = 0
running = True

# Convert text to Morse
def text_to_morse(text):
    return ' '.join(MORSE_DICT.get(c.upper(), '') for c in text)

# Morse blinker
def blink_morse_loop():
    global message_index, running
    while running:
        msg = messages[message_index]
        morse_code = text_to_morse(msg)
        lcd.clear()
        lcd.write_string("Sending:\n" + msg[:16])

        for symbol in morse_code:
            if not running:
                break
            if symbol == '.':
                red_led.on()
                time.sleep(DOT)
                red_led.off()
                time.sleep(INTRA)
            elif symbol == '-':
                blue_led.on()
                time.sleep(DASH)
                blue_led.off()
                time.sleep(INTRA)
            elif symbol == ' ':
                time.sleep(LETTER)
        time.sleep(WORD)

# Button press logic
def switch_message():
    global message_index
    message_index = (message_index + 1) % len(messages)
    lcd.clear()
    lcd.write_string("Next message:\n" + messages[message_index][:16])

button.when_pressed = switch_message

# State Machine
class MorseStateMachine(StateMachine):
    off = State('Off', initial=True)
    sending = State('Sending')

    start = off.to(sending)
    stop = sending.to(off)

    def on_start(self):
        self.thread = threading.Thread(target=blink_morse_loop)
        self.thread.start()

    def on_stop(self):
        global running
        running = False
        red_led.off()
        blue_led.off()
        lcd.clear()

# Run the program
if __name__ == "__main__":
    try:
        sm = MorseStateMachine()
        sm.start()
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        sm.stop()
        print("\nProgram stopped. GPIO cleaned.")
