import tkinter as tk

window = tk.Tk()

## LABEL

# label = tkinter.Label(text ='Python', background = 'black', foreground = 'red', width = 123, height = 200)
# label.pack()

## BUTTON

# button = tk.Button(text = 'press meh', bg = 'red', fg = 'black', width = 100, height = 200)
# button.pack()

## CANVAS

canvas = tk.Canvas(window, bg = 'white', width = 400, height = 400)

canvas.create_line((0, 0), (400, 400), fill = 'red', width = 50)
canvas.create_line((0, 200), (400, 200), fill = 'red', width = 50)
canvas.create_line((200, 400), (200, 0), fill = 'red', width = 50)
canvas.create_line((0, 400), (400, 0), fill = 'red', width = 50)
canvas.create_rectangle((1, 1), (400, 400), width = 15)

canvas.pack()

window.mainloop()

