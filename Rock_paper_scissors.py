from tkinter import *
root = Tk()
root.title('Rock Paper Scissors')
canvas=Canvas()
canvas.pack()
canvas.config(width=800,height=600)
left_hand=PhotoImage(file='left_fist.png')
right_hand=PhotoImage(file='right_fist.png')
height=100
vel=1
while True:
    left_fist=canvas.create_image(0, height, anchor=NW, image=left_hand)
    right_fist=canvas.create_image(452,height,anchor=NW,image=right_hand)
    height+=vel
    canvas.update()
    canvas.after(1)
    canvas.delete(left_fist)
    canvas.delete('all')
    if height==200:
        vel*=-1
    elif height==50:
        vel*=-1
