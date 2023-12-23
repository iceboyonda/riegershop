from tkinter import Tk, Canvas, PhotoImage, Label


def create_root():
    root = Tk()

    root.title("RiegerShop")
    root.resizable(False, False)
    root.geometry("801x800")
    bg = PhotoImage(file="backrieger.png")

    return root


def create_frame():
    frame = Canvas(root, width=801, height=800,)
    frame.grid(row=0, column=0)
    bg = PhotoImage(file="backrieger.png")
    return frame


root = create_root()
frame = create_frame()