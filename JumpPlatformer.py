#Import Section
from tkinter import Tk, Canvas, Label

#Function Factory
def jump(event):
    global jumping
    global mc
    global jumpcounter
    jumping = True
    play_area.delete(mc)
    mc = play_area.create_rectangle(20, 70, 60, 95, fill="orange", outline="orange")
    jumpcounter+=1
    score.config(text=jumpcounter)
    if running:
        window.after(1000,resetmc)

def resetmc():
    global mc
    global jumping
    play_area.delete(mc)
    mc = play_area.create_rectangle(20, 100, 60, 125, fill="orange", outline="orange")
    jumping = False

def gamestatus():
    global jumping
    global running
    global mc
    global obstacle
    global x1
    global x2
    global y1
    global y2
    if (x1 <= 20) :#checks when the obstacle passes the player in order to reset the cords
        x1, x2 = 450, 470
    x1-=20
    x2-=20
    if ((x1>=5 and x1<=40) and not(jumping)):
        running = False
        score.config(text="You Lost!")
    else:
        running = True
        

def managingobstacles():
    global running
    global obstacle
    global x1
    global x2
    global y1
    global y2
    play_area.delete(obstacle)
    obstacle = play_area.create_rectangle(x1, y1, x2, y2, fill="red", outline="red")
    gamestatus()
    if running:
        window.after(100, managingobstacles)

#Declaration of variables
x1 = 450
x2 = 470
y1 = 110
y2 = 125
jumpcounter = 0
running = True
jumping = False

#Construction of the Widgets
window = Tk()
window.title("JumpPlatformer")

play_area = Canvas(window, width=500, height=140)
#Frame of the area
play_area.create_line(15, 15, 480, 15)#Top Side
play_area.create_line(480, 15, 480, 130)#Right Side
play_area.create_line(15, 15, 15, 130)#Left Side
play_area.create_line(15, 130, 480, 130)#Bottom Side

#Main Character
mc = play_area.create_rectangle(20, 100, 60, 125, fill="orange", outline="orange")
#Make the Character Jump
keys = ["<Up>", "<w>", "<space>"]  # List of keys to bind
for key in keys:
    play_area.bind(key, jump)

play_area.pack()
play_area.focus_set()

score = Label(window, text=jumpcounter, font=("Aerial", 25, "bold"))
score.pack()

obstacle = play_area.create_rectangle(x1, y1, x2, y2, fill="red", outline="red")
managingobstacles()

window.mainloop()