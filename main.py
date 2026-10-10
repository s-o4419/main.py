
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

# Movement functions
def forward():
    canvas.move(robot, 0, -20)

    def backward():
        canvas.move(robot, 0, 20)
        
        def left():
            canvas.move(robot, -20, 0)

        def right():
            canvas.move(obot, 20, 0)

            # Movement buttons
tk.Button(window, text="Forward ", command=forward).pack()
tk.Button(window, text="left ", command=left).pack(side="left", padx=65)
tk.Button(window, text="Right ", command=right).pack(side="right", padx=65)
tk.Button(window, text="Backward , command=backward").pack()

# Run the application 
window.mainloop() 

            
