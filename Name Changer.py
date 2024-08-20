import os
import pyautogui
import win32gui
import time
from pynput import keyboard, mouse
import threading
from colorama import init, Fore, Style

# Initialize colorama
init()

# Global variable to block input
input_blocked = False

def on_press(key):
    global input_blocked
    if input_blocked:
        return False  # Block keyboard input

def on_move(x, y):
    global input_blocked
    if input_blocked:
        return False  # Block mouse movement

def on_click(x, y, button, pressed):
    global input_blocked
    if input_blocked:
        return False  # Block mouse clicks

def block_input():
    global input_blocked
    input_blocked = True
    with keyboard.Listener(on_press=on_press) as keyboard_listener, mouse.Listener(on_move=on_move, on_click=on_click) as mouse_listener:
        time.sleep(5)  # Block input for 5 seconds
        input_blocked = False
        keyboard_listener.stop()
        mouse_listener.stop()

def get_window_handle(title):
    hwnd = win32gui.FindWindow(None, title)
    if hwnd == 0:
        print(f"Window with title '{title}' not found.")
        return None
    return hwnd

def send_commands_to_window(hwnd, commands):
    if hwnd:
        try:
            original_hwnd = win32gui.GetForegroundWindow()
            win32gui.SetForegroundWindow(hwnd)
            time.sleep(0.1)
            
            for command in commands:
                # Start blocking input
                input_block_thread = threading.Thread(target=block_input)
                input_block_thread.start()
                
                pyautogui.typewrite(command, interval=0.05)
                pyautogui.press('enter')
                time.sleep(0.5)
            
            win32gui.SetForegroundWindow(original_hwnd)
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("No window handle provided.")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    title = "H2M-Mod: 03361cd0-dirty"
    hwnd = get_window_handle(title)
    
    if hwnd:
        while True:
            # Clear the console
            clear_console()

            # Display color options
            print("=-------------------------------------= CORNS NAME CHANGER =-------------------------------------=")
            print(f"{Fore.RED}^1 = red{Style.RESET_ALL}")
            print(f"{Fore.GREEN}^2 = green{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}^3 = yellow{Style.RESET_ALL}")
            print(f"{Fore.BLUE}^4 = blue{Style.RESET_ALL}")
            print(f"{Fore.CYAN}^5 = light blue{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}^6 = purple{Style.RESET_ALL}")
            print(f"{Fore.WHITE}^7 = white{Style.RESET_ALL}")
            print(f"{Fore.GREEN}^8 = team color{Style.RESET_ALL}")
            print(f"{Fore.WHITE}^9 = grey{Style.RESET_ALL}")
            print(f"{Fore.WHITE}^: = rainbow{Style.RESET_ALL}")
            
            # Example with color codes
            print(f"{Fore.CYAN}Example: {Fore.LIGHTCYAN_EX}^5Your {Fore.LIGHTGREEN_EX}^8Username{Style.RESET_ALL}")
            
            # Get user input for the name
            name_to_set = input("Enter the name you want: ")
            
            # Prepare the command
            commands = [
                f'seta 0xCE3A6324 "{name_to_set}"'  # Use the actual command with the provided name
            ]
            
            # Send commands to the window
            send_commands_to_window(hwnd, commands)

    else:
        print(f"Window with the title '{title}' not found.")

if __name__ == "__main__":
    main()
