import tkinter as tk
from pynput import keyboard
import threading

root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)

width, height = 10, 10

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

x = (screen_w // 2) - (width // 2)
y = (screen_h // 2) - (height // 2)

root.geometry(f"{width}x{height}+{x}+{y}")

canvas = tk.Canvas(root, width=width, height=height,
                   bg="#222222", highlightthickness=0)
canvas.pack()

canvas.create_rectangle(4, 4, 6, 6, fill="white", outline="")

# -------------------
# Hot Key
# -------------------
visible = True

def toggle():
    global visible
    if visible:
        root.withdraw()
    else:
        root.deiconify()
    visible = not visible

def listen_keys():
    def on_press(key):
        try:
            if key == keyboard.Key.f8:
                root.after(0, toggle)
        except:
            pass

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

threading.Thread(target=listen_keys, daemon=True).start()

root.mainloop()
