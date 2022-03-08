# import required modules
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps


# contrast border thumbnail
main = Tk()
main.title("Woro Photo Editor")
main.geometry("1000x1000")
# create functions
def selected():
    global img1, img_path
    img_path = filedialog.askopenfilenames(initialdir=os.getcwd())
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    # imgg = img.filter(ImageFilter.BoxBlur(0))
    img1 = ImageTk.PhotoImage(img)
    Woro2.create_image(300, 210, image=img1)
    Woro2.image = img1


def blur():
    global img1 , img_path, img0
    for m in range(0, v1.get() + 1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        img0 = img.filter(ImageFilter.BoxBlur(m))
        img1 = ImageTk.PhotoImage(img0)
        Woro2.create_image(300, 210, image=img1)
        Woro2.image = img1


def brightness(event):
    global img_path, img2, img3
    for m in range(0, v2.get() + 1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = ImageEnhance.Brightness(img)
        img2 = imgg.enhance(m)
        img3 = ImageTk.PhotoImage(img2)
        Woro2.create_image(300, 210, image=img3)
        Woro2.image = img3


def contrast(event):
    global img_path, img4, img5
    for m in range(0, v3.get() + 1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = ImageEnhance.Contrast(img)
        img4 = imgg.enhance(m)
        img5 = ImageTk.PhotoImage(img4)
        Woro2.create_image(300, 210, image=img5)
        Woro2.image = img5


def rotate_image(event):
    global img_path, img6, img7
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img6 = img.rotate(int(rotate_combo.get()))
    img7 = ImageTk.PhotoImage(img6)
    Woro2.create_image(300, 210, image=img7)
    Woro2.image = img7


def flip_image(event):
    global img_path, img8, img9
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    if flip_combo.get() == "FLIP LEFT TO RIGHT":
        img8 = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif flip_combo.get() == "FLIP TOP TO BOTTOM":
        img8 = img.transpose(Image.FLIP_TOP_BOTTOM)
    img9 = ImageTk.PhotoImage(img8)
    Woro2.create_image(300, 210, image=img9)
    Woro2.image = img9


def image_border(event):
    global img_path, img10, img11
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img10 = ImageOps.expand(img, border=int(border_combo.get()), fill=95)
    img11 = ImageTk.PhotoImage(img10)
    Woro2.create_image(300, 210, image=img11)
    Woro2.image = img11

img1 = None
img3 = None
img5 = None
img7 = None
img9 = None
img11 = None


def save():
    global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11
    # file=None
    ext = img_path.split(".")[-1]
    file = asksaveasfilename(defaultextension=f".{ext}",
                             filetypes=[("All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
    if file:
        if Woro2.image == img1:
            imgg.save(file)
        elif Woro2.image == img3:
            img2.save(file)
        elif Woro2.image == img5:
            img4.save(file)
        elif Woro2.image == img7:
            img6.save(file)
        elif Woro2.image == img9:
            img8.save(file)
        elif Woro2.image == img11:
            img10.save(file)


        # create labels, scales and comboboxes


blurr = Label(main, text="Blur:", font=("ariel 17 bold"), width=9, anchor='e')
blurr.place(x=15, y=8)
v1 = IntVar()
scale1 = ttk.Scale(main, from_=0, to=10, variable=v1, orient=HORIZONTAL, command=blur)
scale1.place(x=150, y=10)

bright = Label(main, text="Brightness:", font=("ariel 17 bold"))
bright.place(x=8, y=50)
v2 = IntVar()
scale2 = ttk.Scale(main, from_=0, to=10, variable=v2, orient=HORIZONTAL, command=brightness)
scale2.place(x=150, y=55)

con = Label(main, text="Contrast:", font=("ariel 17 bold"))
con.place(x=35, y=92)
v3 = IntVar()
scale3 = ttk.Scale(main, from_=0, to=10, variable=v3, orient=HORIZONTAL,command=contrast)
scale3.place(x=150, y=100)


rotate = Label(main, text="Rotate:", font=("ariel 17 bold"))
rotate.place(x=370, y=8)
value0 = [0, 90, 180, 270, 360]
rotate_combo = ttk.Combobox(main, values=value0, font=('ariel 10 bold'))
rotate_combo.place(x=460, y=15)
rotate_combo.bind("<<ComboboxSelected>>", rotate_image)
flip = Label(main, text="Flip:", font=("ariel 17 bold"))
flip.place(x=400, y=50)
values1 = ["FLIP LEFT TO RIGHT", "FLIP TOP TO BOTTOM"]
flip_combo = ttk.Combobox(main, values=values1, font=('ariel 10 bold'))
flip_combo.place(x=460, y=57)
flip_combo.bind("<<ComboboxSelected>>", flip_image)

border = Label(main, text="Add border:", font=("ariel 17 bold"))
border.place(x=320, y=92)
value2 = [(i for i in range(10, 45, 5))]
border_combo = ttk.Combobox(main, values=value2, font=("ariel 10 bold"))
border_combo.place(x=460, y=99)
border_combo.bind("<<ComboboxSelected>>", image_border)




# create woro to display image
Woro2 = Canvas(main, width="600", height="420", relief=RIDGE, bd=2)
Woro2.place(x=15, y=150)
# create buttons
btn1 = Button(main, text="Open Image", bg='silver', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=selected)
btn1.place(x=100, y=595)
btn2 = Button(main, text="Save", width=12, bg='green', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=save)
btn2.place(x=280, y=595)
btn3 = Button(main, text="Exit", width=12, bg='red', fg='gold', font=('ariel 15 bold'), relief=GROOVE,
              command=main.destroy)
btn3.place(x=480, y=595)
main.mainloop()