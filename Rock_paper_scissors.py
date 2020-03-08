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
<<<<<<< HEAD
    canvas.delete(left_fist)
=======
    canvas.delete('all')
>>>>>>> 6ebfc2e8945924a59858453d10f8a62e4a76acb5
    if height==200:
        vel*=-1
    elif height==50:
        vel*=-1
