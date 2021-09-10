import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import *
import cv2
import os

filepath = ""

def select_file():
    filetypes = (('JPG Files', '*.jpg'),('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
    print(filename)
    #reading img
    img = cv2.imread(r'{}'.format(filename))

    dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
    savepath = "C:\\Sketches"

    cv2.imwrite(os.path.join(savepath ,"sketch.jpg"), dst_gray)
    cv2.waitKey(0)




# Creating Root1

root = tk.Tk()
root.title('InSketch')

window_width = 1280
window_height = 720

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.attributes('-alpha',0.9)
root.iconbitmap('app_icon.ico')

# labelling

label = ttk.Label(root,text='Select File for the Sketch',font=("Century Gothic", 32))

label.pack(ipadx=10, ipady=100)



open_button = ttk.Button(root,text='Browse',command=select_file)


open_button.pack(expand=True)



root.mainloop()

