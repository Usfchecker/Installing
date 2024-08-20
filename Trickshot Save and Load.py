import time
import webbrowser
from inputs import get_gamepad
from pynput.keyboard import Key, Controller
from threading import Thread, Event
import os

keyboard_controller = Controller()
enabled = True
action_event = Event()

def handle_gamepad_input():
    while True:
        events = get_gamepad()
        for event in events:
            if event.code == 'ABS_HAT0X':
                if not enabled:
                    continue
                if event.state == -1:  # Left D-Pad
                    perform_action('save')
                elif event.state == 1:  # Right D-Pad
                    perform_action('load')

def perform_action(action):
    if action == 'save':
        keyboard_controller.press('t')
        keyboard_controller.release('t')
        time.sleep(0.1)
        keyboard_controller.type(action)
        keyboard_controller.press(Key.enter)
        keyboard_controller.release(Key.enter)
        display_message("Saved Position")
        
    elif action == 'load':
        keyboard_controller.press('t')
        keyboard_controller.release('t')
        time.sleep(0.1)
        keyboard_controller.type(action)
        keyboard_controller.press(Key.enter)
        keyboard_controller.release(Key.enter)
        display_message("Loaded Position")

def display_message(message):
    if action_event.is_set():
        return
    action_event.set()
    print(message)
    time.sleep(2)
    action_event.clear()

def toggle_functionality():
    global enabled
    while True:
        user_input = input("1 To Toggle <3 : ").strip()
        if user_input == '1':
            enabled = not enabled
            status = "enabled" if enabled else "disabled"
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"=-------------------------------------= CORNS POS SAVER =-------------------------------------=")
            print(f"Left/Right D-Pad Bind {status}")

if __name__ == "__main__":
    webbrowser.open('https://discord.gg/SuDEAtyAWD')
    toggle_thread = Thread(target=toggle_functionality)
    toggle_thread.daemon = True
    toggle_thread.start()
    handle_gamepad_input()
