
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My first Robot")
window.geometry("400x450")

# Robot starting position
x = 170
y = 170

# Draw the robot
canvas = tk.Canvas(window, width=350, height=300, bg="white")
canvas.pack(pady=10)

robot = canvas.create_rectangle(
    x, y, x + 40, y + 40, fill="blue"
)
