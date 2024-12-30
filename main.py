import tkinter as tk
import pyautogui
import time

def IntervalHoldsRight():
    try:
        option = float(Hold_entry_right.get())
        pyautogui.mouseDown(button='right')
        time.sleep(option)
        pyautogui.mouseUp(button='right')
    except ValueError:
        label.config(text="Please enter a valid hold duration.")

def ClickedFunc(x_position, y_position):
    pyautogui.click(x=x_position, y=y_position)

def set_cursor_position():
    try:
        x_position = int(x_entry.get())
        y_position = int(y_entry.get())
        pyautogui.moveTo(x_position, y_position)
    except ValueError:
        label.config(text="Please enter valid numbers for X and Y.")

def on_button_click():
    states = ["Loading.", "Loading..", "Loading...", "Loading....", "Loading.....", "Loading......"]
    current_state = 0
    active = True

    def animate_load():
        nonlocal current_state, active
        if active:
            label.config(text=states[current_state])
            current_state = (current_state + 1) % len(states)
            root.after(50, animate_load)

    def stop_anim():
        nonlocal active
        active = False
        label.config(text="Clicked!")
        try:
            x_position = int(x_entry.get())
            y_position = int(y_entry.get())
            ClickedFunc(x_position, y_position)
        except ValueError:
            label.config(text="Please enter valid numbers for X and Y.")

    animate_load()
    root.after(500, stop_anim)

root = tk.Tk()
root.title("Zap Macro + Best Auto Clicker for macOS")
root.geometry("350x600")

label = tk.Label(root, text="Zap Macro + Best Auto Clicker for macOS!", font=("Arial", 16))
label.pack(pady=15)

CoordinateClickLabel = tk.Label(root, text="Advanced Section", font=("Arial", 16))
CoordinateClickLabel.pack(pady=10)

x_label = tk.Label(root, text="X Coordinate:")
x_label.pack(pady=5)
x_entry = tk.Entry(root, relief="ridge")
x_entry.pack(pady=5)

y_label = tk.Label(root, text="Y Coordinate:")
y_label.pack(pady=5)
y_entry = tk.Entry(root, relief="ridge")
y_entry.pack(pady=5)

button = tk.Button(
    root,
    text="Click At This Position",
    command=on_button_click,
    width=22,
    height=2,
    font="Arial"
)
button.pack(pady=10)

Hold_Mouse_label_right = tk.Label(root, text="How Long do you want to Hold Clicks For? (Right Click)")
Hold_Mouse_label_right.pack(pady=5)
Hold_entry_right = tk.Entry(root, relief="ridge")
Hold_entry_right.pack(pady=5)

Hold_Mouse = tk.Label(root, text="Delayed Click (Hold Click)")
Hold_Mouse.pack(pady=10)

Hold_Mouse_Intervals_2 = tk.Button(
    root,
    text="Hold Right Click",
    command=IntervalHoldsRight,
    width=22,
    height=2,
    font="Arial"
)

Hold_Mouse_Intervals_2.pack(pady=10)

root.mainloop()
