import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename

from PIL import Image, ImageTk, ImageFilter

from editFunctions import (sharpenPic, rotateCounter, rotateClock, cropPic, sketchPic, oilPic, pencilPic, foilPic,
                           negativePic)

# contrast border thumbnail
main = Tk()
main.title("Woro Photo Editor")
counter = 0
main.geometry("1000x505")
var = IntVar()
editingBox = Frame(main)

def changeImage(counter):
    global   img_path , img, image
    img_path = filedialog.askopenfilename(initialdir=os.getcwd())
    image= Image.open(img_path)
    img = ImageTk.PhotoImage(Image.open('image' + str(counter) ))
    # panel.configure(image=img)
    # panel.image = img
def selected(counter):
        global img_path, img
        img_path = filedialog.askopenfile(initialdir=os.getcwd())
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        # imgg = img.filter(ImageFilter.BoxBlur(0))
        img0 = ImageTk.PhotoImage(img)
        woro2.create_image(300, 210, image=img0)
        woro2.image = img0





def sharpenImgFunc():
    global counter , img , img1,img2
    img = Image.open(img_path)
    curImg = 'img' + str(counter)
    counter = counter + 1
    img1 = sharpenPic(curImg, counter)
    img2 = changeImage(counter)
    woro2.create_image(300, 210, image=img2)
    woro2.image = img2



def blur(event):
    global img_path, img3, img4
    for m in range(0, v1.get() + 1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        img3 = img.filter(ImageFilter.BoxBlur(m))
        img4 = ImageTk.PhotoImage(img3)
        woro2.create_image(300, 210, image=img4)
        woro2.image = img4


def rotateCounterFunc():
    global counter ,img,img5,img6 , img_path
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    curImg = "img" + (counter)
    counter = counter + 1
    img5 = rotateCounter(curImg, counter)
    img6 = changeImage(counter),img5
    woro2.create_image(300,210, image=img6 )
    woro2.image = img6

def rotateClockFunc():
    global counter,img,img7,img8
    img = Image.open(img_path)
    curImg = 'img' + str(counter)
    counter = counter + 1
    img7=rotateClock(curImg, counter)
    img8=changeImage(counter),img7
    woro2.create_image(300, 210, image=img8)
    woro2.image = img8


def cropImgFunc():
    global counter, img, img9 , img10
    img = Image.open(img_path)
    curImg = 'img' + str(counter)
    counter = counter + 1
    img9=cropPic(curImg, counter)
    img10=changeImage(counter)
    woro2.create_image(300, 210, image=img10)
    woro2.image = img10


def undoFunc():
    global counter
    if counter > 0:
        counter = counter - 1
    changeImage(counter)


def sketchImgFunc():
    global counter, img, img11, img12
    img = Image.open(img_path)
    curImg = 'img' + str(counter)
    counter = counter + 1
    img11=sketchPic(curImg, counter)
    img12=changeImage(counter)
    woro2.create_image(300, 210, image=img12)
    woro2.image = img12


def oilImgFunc():
    global counter , img, img13, img14
    img = Image.open(img_path)
    curImg = 'img' + str(counter)
    counter = counter + 1
    img13 = oilPic(curImg, counter)
    img14 =changeImage(counter)
    woro2.create_image(300, 210, image=img13)
    woro2.image = img14


def paintImgFunc():
    global counter , img, img15 , img16
    img = Image.open(img_path)
    curImg = 'img' + str(counter)
    counter = counter + 1
    img15=pencilPic(curImg, counter)
    img16=changeImage(counter)
    woro2.create_image(300, 210, image=img15)
    woro2.image = img16


def foilImgFunc():
    global counter , img
    img = Image.open(img_path)
    curImg = 'img' + str(counter)
    counter = counter + 1
    img17 = foilPic(curImg, counter)
    img18 = changeImage(counter),img17
    woro2.create_image(300, 210, image=img17)
    woro2.image = img18


def negativeImgFunc():
    global counter, img , img19 , img20
    curImg = 'img' + str(counter)
    counter = counter + 1
    img19 = negativePic(curImg, counter)
    img20 = changeImage(counter)
    woro2.create_image(300, 210, image=img19)
    woro2.image = img20

def formatfun():
    global  counter, img, img21, img22
    img = Image.open(img_path)
    curImg = 'img'+str(counter)
    counter = counter + 1
    img21 = format(curImg,counter)
    img22 = changeImage(counter)
    woro2.create_image(300, 210, image=img22)
    woro2.image = img22

img1 = None
img3 = None
img5 = None
img7 = None
img9 = None
img11 = None
img13 = None
img15 = None
img17 = None
img19 = None
img21 = None

def save():
    global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11 ,img12, img13, img14, img15, img16, img17,img18, img19, img20, img21, img22
    # file=None
    ext = img_path.split(".")[-1]
    file = asksaveasfilename(defaultextension=f".{ext}",
                             filetypes=[("All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
    if file:
        if woro2.image == img1:
            imgg.save(file)
        elif woro2.image == img3:
            img2.save(file)
        elif woro2.image == img5:
            img4.save(file)
        elif woro2.image == img7:
            img6.save(file)
        elif woro2.image == img9:
            img8.save(file)
        elif woro2.image == img11:
            img10.save(file)
        elif woro2.image == img13:
            img12.save(file)
        elif woro2.image == img15:
            img14.save(file)
        elif woro2.image == img17:
            img16.save(file)
        elif woro2.image == img19:
            img17.image(file)
        elif woro2.image == img21:
            img20.save(file)
# main = Tk()
# counter = 0
# main.title("Photo Editor")
# main.geometry("1000x505")
# var = IntVar()
# editingBox = Frame(main)

# create woro to display image
woro2 = Canvas(main, width="600", height="420", relief=RIDGE, bd=2)
woro2.place(x=15, y=150)

open = Button(main, text="Select Image", bg='green', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=selected)
open.place(x=100, y=595)

save = Button(main, text="Save", width=12, bg='red', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=save)
save.place(x=280, y=595)

Exit = Button(main, text="Exit", width=12, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE,
              command=main.destroy)
Exit.place(x=460, y=595)

formatLabel = Label(main, text = "Format", font=16)
formatLabel.pack(side = TOP, pady=10)

SharpenButton = Button(editingBox, text="Sharpen Image", command=sharpenImgFunc, width=20)
SharpenButton.pack(side = TOP)

# undoButton = Button(editingBox, text="Undo", command=undoFunc, font=20)
# undoButton.pack(side=BOTTOM, pady=10)


blurr = Label(main, text="Blur:", font=("ariel 17 bold"), width=9, anchor='e')
blurr.place(x=15, y=8)
v1 = IntVar()
scale1 = ttk.Scale(main, from_=0, to=10, variable=v1, orient=HORIZONTAL, command=blur)
scale1.place(x=150, y=10)


sharpness = Label(main, text="Brightness:", font=("ariel 17 bold"))
sharpness.place(x=8, y=50)
v2 = IntVar()
scale2 = ttk.Scale(main, from_=0, to=10, variable=v2, orient=HORIZONTAL, command=sharpenImgFunc)
scale2.place(x=150, y=55)


CropButton = Button(editingBox, text="Crop", command=cropImgFunc, width=20)
CropButton.pack(side = TOP)

rotateCounterButton = Button(editingBox, text="Rotate Counter Clockwise", command = rotateCounterFunc, width=20)
rotateCounterButton.pack(side = TOP)

rotateClockButton = Button(editingBox, text="Rotate Clockwise", command = rotateClockFunc, width=20)
rotateClockButton.pack(side = TOP)

negativeButton = Button(editingBox, text="Photo negative", command=negativeImgFunc, width=20)
negativeButton.pack(side = BOTTOM)

foilButton = Button(editingBox, text="Foil art", command=foilImgFunc, width=20)
foilButton.pack(side = BOTTOM)

pencilButton = Button(editingBox, text="Sharp paint", command=paintImgFunc, width=20)
pencilButton.pack(side = BOTTOM)

oilButton = Button(editingBox, text="Oil paint", command=oilImgFunc, width=20)
oilButton.pack(side = BOTTOM)
sketchButton = Button(editingBox, text="Sketch light", command=sketchImgFunc, width=20)
sketchButton.pack(side = BOTTOM)

filterLabel = Label(editingBox, text = "Filters", font=16)
filterLabel.pack(side = BOTTOM, pady=10)

img = ImageTk.PhotoImage
editingBox.pack()
main.mainloop()