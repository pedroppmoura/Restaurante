from tkinter import *


t = Tk()



canvas = Canvas(frame, bg="black", width=500, height=500)
canvas.pack()

photoimage = PhotoImage(file="Refrigerante de Cola.png")
canvas.create_image(150, 150, image=photoimage)

t.mainloop()
