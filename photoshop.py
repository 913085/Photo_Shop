#Import libarary

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps, ImageDraw, ImageFont
import os
# contast border of thumbnail
root = Tk()
root.titile("Simple Photot Editor")
root.geometry("640*640")
def selected():
    Image_path = askopenfilename(initialdir=os.getcwd())
    Img = Image.open(Image_path)
    img.thumbnail((350,350))

    # image filter
    image.Image1


# Chose an Image
my_image = open("a1.jpg")
#Font selection
title_font = ImageFont.truetype('playfair/playfair-font.ttf', 200)

#Rendered the text
title_text = "The Beauty of Nature"
# Secondly, we will use the ImageDraw function to convert our image into an editable format.
image_editable = ImageDraw.Draw(my_image)
#
image_editable.text((15,15), title_text, (237, 230, 211), font=title_font)



