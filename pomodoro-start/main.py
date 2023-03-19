
# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import END, Button, Canvas, Label, PhotoImage, Text, Tk
import time
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"

current_checkmark = ""
work_sessions = 0
reps_short_pauses = [2,4,6]
reps_long_pauses = 8
timer = None


reps = 1
#count = WORK_MIN*60
count = 10

def reset_timer(window, label_timer, canvas_timer_text, label_checked):
    global timer, current_checkmark, reps
    window.after_cancel(timer)
    label_timer.config(text="Timer", fg="green")
    canvas.itemconfig(canvas_timer_text, text=f"00:00")
    reps = 1
    current_checkmark = ""
    label_checked.config(text=current_checkmark)
    



def start_timer(window, count, canvas, label_timer, label_checkmark):
    global reps,work_sessions

    work_sec = WORK_MIN*60
    short_brek_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    
    if(reps == 8): 
        label_timer.config(fg=PINK, text="Break")
        reps = 1
        counting_down(window,long_break_sec, canvas, label_timer,label_checkmark)
        
        
    elif(reps in reps_short_pauses): 
        label_timer.config(fg=RED, text="Break")
        reps += 1
        counting_down(window, short_brek_sec, canvas, label_timer,label_checkmark)

    else: 
        reps += 1
        label_timer.config(fg="green", text="Work")
        work_sessions += 1
        counting_down(window, work_sec, canvas, label_timer,label_checkmark)


def counting_down(window, count, canvas, label_timer, label_checkmark):
    global reps, current_checkmark, work_sessions, reps_long_pauses
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if(count_sec < 10):
        #count_sec = "0"+str(count_sec)
        count_sec = f"0{count_sec}"
    
    if count >= 0:
        global timer
        canvas.itemconfig(canvas_timer_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, counting_down, window,count-1,canvas, label_timer, label_checkmark)
        
    else: 
        print(f'REPS:{reps}')
        if (((reps+1) not in reps_short_pauses) and (reps+1) != reps_long_pauses and reps != 7):
            current_checkmark += CHECKMARK
            label_checkmark.config(text=current_checkmark)
            
        
        start_timer(window, count, canvas, label_timer, label_checkmark)
            
      
            
        #TIMER, FUNCTION TO BE CALLED, ARGUMENTS PASSED TO THE FUNCTION
    #count = 5
    #label_timer.config(text=count)
    #while True:
    #    time.sleep(1)
    #    count -= 1
    


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #




if __name__ == '__main__':
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=100, background="#CCD5AE")
    window.resizable(False,False)
    
    
    #def say_something():
        #print("SOMETHING")
    
    
    canvas = Canvas(width=200, height=224, background="#0E8388", bg="#CCD5AE", highlightthickness=0)
    my_image = PhotoImage(file="tomato.png")
    
    canvas.create_image(100,100,image=my_image)
    #canvas.create_text(103,130,text="00:00", font=(FONT_NAME, 35, 'bold'), fill='white')
    canvas_timer_text = canvas.create_text(103,130,text="00:00", font=(FONT_NAME, 35, 'bold'), fill='white')
    canvas.grid(column=2, row=2)
    
    label_timer = Label(text="Timer", font=(FONT_NAME, 35, 'bold'), fg="green", background="#CCD5AE")
    label_timer.grid(column=2, row=1)

    
    label_checked = Label(text="", fg="green", bg="#CCD5AE", font=(FONT_NAME, 12, 'bold'))
    label_checked.grid(row=4, column=2)
    
    start_button = Button(window,text="Start", command=lambda: start_timer(window, count, canvas, label_timer, label_checked))
    start_button.grid(row=3, column=1)
    
    reset_button = Button(window,text="Reset", command=lambda: reset_timer(window, label_timer, canvas_timer_text, label_checked))
    reset_button.grid(row=3, column=3) 
       

    
    window.mainloop()