import tkinter as tk

# Create a new Tkinter window
win = tk.Tk()

# Create a label widget and add it to the window
win.geometry('100x200')
label = tk.Label(win, text="  isro  ")
label.pack()

B  =tk.Button(win , text = "LOL",command=win.destroy)
B.pack(side = tk.TOP)

BB  =tk.Button(win , text = "LOL",command=win.destroy)
BB.pack(side = tk.LEFT)

BBB  =tk.Button(win , text = "LOL",command=win.destroy)
BBB.pack(side = tk.RIGHT)
BBB  =tk.Button(win , text = "LOL",command=win.destroy)
BBB.pack(side = tk.BOTTOM)
# Run the Tkinter event loop
win.mainloop()