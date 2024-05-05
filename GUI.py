from tkinter import *
root = Tk()
root.title("Canvas Example")

root.geometry("1000x700",min("1000x700"),max(1000x700))

canvas = Canvas(root, width=500, height=400, bg="lightblue")

canvas.pack(fill=BOTH, expand=True)

root.mainloop()