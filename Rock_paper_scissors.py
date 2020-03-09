from tkinter import *
from random import randint
import time
start=time.time()
root = Tk()
root.title('Rock Paper Scissors')
canvas=Canvas()
canvas.pack()
width=800
height=600
canvas.config(width=width,height=height)
left_hand=PhotoImage(file='left_fist.png')
right_hand=PhotoImage(file='right_fist.png')
rock=PhotoImage(file='rock.png')
paper=PhotoImage(file='paper.png')
scissors=PhotoImage(file='scissors.png')
height=100
vel=1
x=0
countdown=3
rand=randint(0,2)
playerchoice=2

while True:
    canvas.create_text(width-100, 50, fill='black', text='You', font=("Purisa", 30))
    canvas.create_text(100, 50, fill='black', text='Robot', font=("Purisa", 30))
    if countdown>0:
        left_fist=canvas.create_image(0, height, anchor=NW, image=left_hand)
        right_fist=canvas.create_image(width-348,height,anchor=NW,image=right_hand)
        canvas.create_text(400, 100, fill='black', text=countdown,font=("Purisa", 30))
        height+=vel
    if (x+1)%333==0:
        countdown-=1
    if countdown<=0 and rand==0:
        if playerchoice==0:
            canvas.create_image(width-200,100,anchor=NW, image=rock)
            canvas.create_image(0,100,anchor=NW, image=rock)
            canvas.create_text(400, 100, fill='black', text='You tied', font=("Purisa", 30))
        elif playerchoice==1:
            canvas.create_image(width-200,100,anchor=NW, image=paper)
            canvas.create_image(0,100,anchor=NW, image=rock)
            canvas.create_text(400, 100, fill='black', text='You won', font=("Purisa", 30))
        elif playerchoice==2:
            canvas.create_image(width-200,100,anchor=NW, image=scissors)
            canvas.create_image(0,100,anchor=NW, image=rock)
            canvas.create_text(400, 100, fill='black', text='You lost', font=("Purisa", 30))
    elif countdown<=0 and rand==1:
        if playerchoice==0:
            canvas.create_image(width-200,100,anchor=NW, image=rock)
            canvas.create_image(0,100,anchor=NW, image=paper)
            canvas.create_text(400, 100, fill='black', text='You lost', font=("Purisa", 30))
        elif playerchoice==1:
            canvas.create_image(width-200,100,anchor=NW, image=paper)
            canvas.create_image(0,100,anchor=NW, image=paper)
            canvas.create_text(400, 100, fill='black', text='You tied', font=("Purisa", 30))
        elif playerchoice==2:
            canvas.create_image(width-200,100,anchor=NW, image=scissors)
            canvas.create_image(0,100,anchor=NW, image=paper)
            canvas.create_text(400, 100, fill='black', text='You won', font=("Purisa", 30))
    elif countdown<=0 and rand==2:
        if playerchoice==0:
            canvas.create_image(width-200,100,anchor=NW, image=rock)
            canvas.create_image(0,100,anchor=NW, image=scissors)
            canvas.create_text(400, 100, fill='black', text='You won', font=("Purisa", 30))
        elif playerchoice==1:
            canvas.create_image(width-200,100,anchor=NW, image=paper)
            canvas.create_image(0,100,anchor=NW, image=scissors)
            canvas.create_text(400, 100, fill='black', text='You lost', font=("Purisa", 30))
        elif playerchoice==2:
            canvas.create_image(width-200,100,anchor=NW, image=scissors)
            canvas.create_image(0,100,anchor=NW, image=scissors)
            canvas.create_text(400, 100, fill='black', text='You tied', font=("Purisa", 30))

    canvas.update()
    canvas.after(1)
    x+=1
    canvas.delete('all')
    if height==200:
        vel*=-1
    elif height==50:
        vel*=-1
