# firts import the package as an abreviature
import tkinter as tk
from tkinter.filedialog import askdirectory
import os

# then set-up a variable for the window with the class buil-in in the package Tk()
window = tk.Tk()

# in the next codes we set-up certain caracteristics of the window
window.title("L1")
window.iconbitmap(default= "icons8-compare-50.ico")
window.minsize(width= 650, height= 600)

# in the next codes we create the canvas that hold our image an the img class of tkinter
canvas = tk.Canvas(width= 150, height=200)
img = tk.PhotoImage(file="L1_cmix.png")
img = img.subsample(8,8) # here we resize the img
canvas.create_image(75,100, image= img)
canvas.pack()


def get_source():
    path = askdirectory()
    print(path)
    
    t_path = path.replace("/", '\\')
    print(t_path)
    # for relPath,dirs,files in os.walk(path):
    #     print(files)


button = tk.Button(text="Source 📁", command= get_source)
button.pack()






# in here we mantain a loop that listen for the window continue open this may go in the finish of our script
window.mainloop() 