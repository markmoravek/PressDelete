from pynput.keyboard import Key, Controller
from pynput import keyboard
import time

keyboard = Controller()
active = True

print("Deleting...")
print("Press 'ctrl + c' in cmd or terminal to quit")
try:
	while True:
		time.sleep(2)
		keyboard.press(Key.delete)
		keyboard.release(Key.delete)
except KeyboardInterrupt:
	pass

print("Process stopped")