import time
from pynput.keyboard import Key, Controller, Listener

keyboard = Controller()
running = True

def press_space():
    while running:
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        time.sleep(0.1)

def on_press(key):
    global running
    if key == Key.esc:  # Pressione 'esc' para parar o loop
        running = False
        return False

# Inicie a thread para pressionar a barra de espaço
import threading
space_thread = threading.Thread(target=press_space)
space_thread.start()

# Inicie o listener de teclado
with Listener(on_press=on_press) as listener:
    listener.join()
