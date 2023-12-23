from json import load, dump
from tkinter import Button
from PIL import Image, ImageTk
from canvas import frame, root
from helpers import clean_screen


def display_products():
    clean_screen()
    display_stock()


def display_stock():
    global info

    with open("db/products_data.json", "r") as stock:
        info = load(stock)

    x, y = 150, 50

    for item_name, item_info in info.items():
        item_img = ImageTk.PhotoImage(Image.open(item_info["image"]))
        images.append(item_img)

        frame.create_text(x + 60, y, text=item_name, font=("Montserrat", 15))
        frame.create_image(x + 60, y + 100, image=item_img)

        if item_info["quantity"] > 0:
            color = "grey"
            font = ("Montserrat", 12),
            text = f"In stock: {item_info['quantity']}"

            item_btn = Button(
                root,
                text="Buy",
                font=("Montserrat", 12),
                bg="grey",
                fg="white",
                width=5,
                command=lambda x=item_name: buy_product(x),
            )

            frame.create_window(x + 60, y + 230, window=item_btn)
        else:
            color = "red"
            font = ("Montserrat", 12),
            text = "Sold Out :("

        frame.create_text(x + 60, y + 180, text=text, font=("Montserrat", 12), fill=color)

        x += 400
        if x > 550:
            x = 150
            y += 300


def buy_product(product):
    info[product]["quantity"] -= 1

    with open("db/products_data.json", "w") as stock:
        dump(info, stock)

    display_products()


images = []
info = {}
