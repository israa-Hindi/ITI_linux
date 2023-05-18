import tkinter as tk

# Create a new Tkinter window
win = tk.Tk()

# Create a label widget and add it to the window
label = tk.Label(win, text="Hello, Tkinter!")
label.pack()

# Run the Tkinter event loop
win.mainloop()