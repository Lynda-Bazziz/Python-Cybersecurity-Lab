from pynput import keyboard
import pyautogui
import os
from datetime import datetime

# Dossier de sauvegarde
SAVE_DIR = "screenshots"
os.makedirs(SAVE_DIR, exist_ok=True)

# Fonction de capture d’écran
def take_screenshot():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(SAVE_DIR, filename)
    pyautogui.screenshot(filepath)
    print(f"[+] Capture écran sauvegardée : {filepath}")

# Fonction appelée à chaque pression de touche
def on_press(key):
    try:
        if key == keyboard.Key.enter:
            take_screenshot()
    except Exception as e:
        print(f"Erreur lors de la capture d’écran : {e}")

# Démarrage du listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
