from tkinter import *
root = Tk()
root.title('Rock Paper Scissors')
canvas=Canvas()
canvas.pack()
canvas.config(width=800,height=600)
rock=PhotoImage(file='left_fist.png')
height=100
vel=1
while True:
    left_fist=canvas.create_image(0, height, anchor=NW, image=rock)
    height+=vel
    canvas.update()
    canvas.after(1)
    canvas.delete(left_fist)
    if height==200:
        vel*=-1
    elif height==50:
        vel*=-1
