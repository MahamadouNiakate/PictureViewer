from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("viewer")


my_img1 = ImageTk.PhotoImage(Image.open("images/desert.jpg"))


my_img2 = ImageTk.PhotoImage(Image.open("images/beach.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/calle.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/children.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/conemara.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("images/lion.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("images/maison.jpg"))
my_img8 = ImageTk.PhotoImage(Image.open("images/mar.jpg"))
my_img9 = ImageTk.PhotoImage(Image.open("images/moher.jpg"))
my_img10 = ImageTk.PhotoImage(Image.open("images/mountain.jpg"))
my_img11 = ImageTk.PhotoImage(Image.open("images/place.jpg"))
my_img12 = ImageTk.PhotoImage(Image.open("images/plage.jpg"))
my_img13 = ImageTk.PhotoImage(Image.open("images/ruisseau.jpg"))
my_img14 = ImageTk.PhotoImage(Image.open("images/snow.jpg"))
my_img15 = ImageTk.PhotoImage(Image.open("images/sun.jpg"))
my_img16 = ImageTk.PhotoImage(Image.open("images/trees.jpg"))

image_list = [my_img1,
              my_img2,
              my_img3,
              my_img4,
              my_img5,
              my_img6,
              my_img7,
              my_img8,
              my_img9,
              my_img10,
              my_img11,
              my_img12,
              my_img13,
              my_img14,
              my_img15,
              my_img16]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


button_back = Button(root, text="<<")
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>")


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()
