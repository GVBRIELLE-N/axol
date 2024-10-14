from tkinter import messagebox, filedialog
from axol.axol import axol as ax
from datetime import datetime as dt
from PIL import ImageTk, Image
from config.theme import *
from tkinter import ttk
from tkinter import *

import time as tm
import random as r
import tkinter as tk
import calendar as cal

#=======Functions=======
def viewTask():
    task_bg.pack(side=TOP, fill='both', expand=True)
    axl_bg.pack_forget()
    
def hideTask():
    axl_bg.pack (side=TOP, fill='both', expand=True)
    task_bg.pack_forget()

def viewCalendar():
    cal_bg.pack(side=TOP, fill='both', expand=True)
    axl_bg.pack_forget()
    
def hideCalendar():
    axl_bg.pack(side=TOP, fill='both', expand=True)
    cal_bg.pack_forget()

def viewNotes():
    note_bg.pack(side=TOP, fill='both', expand=True)
    axl_bg.pack_forget()
    
def hideNotes():
    axl_bg.pack(side=TOP, fill='both', expand=True)
    note_bg.pack_forget()

def viewComm():
    com_bg.pack(side=TOP, fill='both', expand=True)
    axl_bg.pack_forget()

def hideComm():
    axl_bg.pack(side=TOP, fill='both', expand=True)
    com_bg.pack_forget()

def viewSettings():
    set_bg.pack(side=TOP, fill='both', expand=True)
    axl_bg.pack_forget()

def hideSettings():
    axl_bg.pack(side=TOP, fill='both', expand=True)
    set_bg.pack_forget()

def updateTime():
    time = dt.now()
    app_time.config(text=f"{str(time)[11:19]}")
    axl_main.after(100, updateTime)

def changeOnHover(button):
    button.bind("<Enter>", func=lambda e: button.config(background=pgt.pet_button_hover, width=pgt.pet_hover))
    button.bind("<Leave>", func=lambda e: button.config(background=pgt.pet_button_colour, width='9'))

axl_main        = tk.Tk()
width,height    = 480,360

screen_width    = axl_main.winfo_screenwidth()
screen_height   = axl_main.winfo_screenheight()

x               = (screen_width/2)  - (width/2)
y               = (screen_height/2) - (height/2)

axl_main.title         ("Espee | Alpha Version")
axl_main.geometry      ('%dx%d+%d+%d' % (width, height, x, y))
axl_main.resizable     (False, False)
axl_main.option_add    ('*tearOff', False)

# app_icon   = PhotoImage(file='Icon.png')
# axl_main.iconphoto     (True, app_icon)

pet_themes = {0:default_theme, 1:default_dark, 2:matra_os, 
              3:matra_os_b, 4:retro_95, 5: puppypoppy}

cur_theme  = 5
pgt = pet_themes[cur_theme]

#==========Frames=================
axl_bg      = Frame    (axl_main, background=pgt.pet_bg_colour)
axl_bg.pack            (side=TOP, fill=BOTH, expand=True)

pet_edgeb   = Frame    (axl_bg, background=pgt.pet_button_colour, height='15')
pet_edgeb.pack         (side=BOTTOM, fill='x')

#==========Tasks Elements==========
task_bg     = Frame   (axl_main, background=pgt.pet_bg_colour)

task_label  = Label   (task_bg, text="Tasks", font=("Arial", 12))
task_label.configure  (foreground="white", background=pgt.pet_button_colour)
task_label.pack       (anchor=NE, fill='x')

task_footer = Frame   (task_bg, background=pgt.pet_button_colour, height='20')
task_footer.pack      (side=BOTTOM, fill='x')

task_exit   = Button(task_bg, text="RETURN", command=hideTask)

task_exit.pack(side=BOTTOM, anchor=SE, pady='10')

task_done   = Button(task_bg, text="COMPLETED")
task_done.pack(side=TOP, anchor=NE, pady='5')

task_progress = Button(task_bg, text="IN PROGRESS")
task_progress.pack(side=TOP, anchor=NE, pady='5')

task_todo   = Button(task_bg, text="TODO")
task_todo.pack(side=TOP, anchor=NE, pady='5')

#==========Calendar Elements==========
cal_bg = Frame(axl_main, background=pgt.pet_button_colour)

cal_label   = Label(cal_bg, text="Calendar", font=("Arial", 12))
cal_label.configure(foreground="white", background=pgt.pet_button_colour)
cal_label.pack(anchor=NE, fill='x')

cal_content = str(dt.now())[0:10]
cal_text    = Label(cal_bg, text = cal_content, justify="left")
cal_text.pack(anchor=N, fill='x')

cal_tasks   = "No tasks today"
cal_t_list  = Label(cal_bg, text=cal_tasks)
cal_t_list.pack(anchor=N, fill='both')

cal_footer  = Frame(cal_bg, background=pgt.pet_button_colour, height='20')
cal_footer.pack(side=BOTTOM, fill='x')

cal_exit    = Button(cal_bg, text="RETURN", command=hideCalendar)
cal_exit.pack(side=BOTTOM, anchor=SE, pady='10')

#==========Notes Elements==========
note_bg = Frame(axl_main, background=pgt.pet_bg_colour)

note_label    = Label(note_bg, text="Notes", font=("Arial", 12))
note_label.configure(foreground="white", background=pgt.pet_button_colour)
note_label.pack(anchor=NE, fill='x')

note_footer   = Frame(note_bg, background=pgt.pet_button_colour, height='20')
note_footer.pack(side=BOTTOM, fill='x')

note_exit     = Button(note_bg, text="RETURN", command=hideNotes)
note_exit.pack(side=BOTTOM, anchor=SE, pady='10')

#==========Settings Elements==========
set_bg = Frame(axl_main, background=pgt.pet_bg_colour)

set_label   = Label(set_bg, text="Settings", font=("Arial", 12))
set_label.configure(foreground="white", background=pgt.pet_button_colour)
set_label.pack(anchor=NE, fill='x')

set_footer  = Frame(set_bg, background=pgt.pet_button_colour, height='20')
set_footer.pack(side=BOTTOM, fill='x')

set_exit    = Button(set_bg, text="EXIT", command=hideSettings)
set_exit.pack(side=BOTTOM, anchor=SE, pady='10')

set_theme    = Button(set_bg, text="THEME")
set_theme.pack(side=BOTTOM, anchor=SE, pady='5')

set_layout = Button(set_bg, text="LAYOUT")
set_layout.pack(side=BOTTOM, anchor=SE, pady='5')

#==========Command Elements==========
com_bg      = Frame(axl_main, background=pgt.pet_bg_colour)

com_label   = Label(com_bg, text="Command Panel", font=("Arial", 12))
com_label.configure(foreground="white", background=pgt.pet_button_colour)
com_label.pack(anchor=NE, fill='x')

com_footer  = Frame(com_bg, background=pgt.pet_button_colour, height='20')
com_footer.pack(side=BOTTOM, fill='x')

com_exit    = Button(com_bg, text="EXIT", command=hideComm)
com_exit.pack(side=BOTTOM, anchor=SE, pady='10')

#=======Labels=======
app_title = Label(axl_bg, text="Espee Alpha Build", font=("Arial", 12))
app_title.pack(anchor=NE, fill='x')

app_time = Label(axl_bg, text="00:00", font=("Arial", 16))
app_time.pack(side=BOTTOM, anchor=SW)

#=======Buttons=======
button_cal    = Button(axl_bg, text="CALENDAR", command=viewCalendar)
button_cal.pack(anchor=NE, pady='5')

button_notes    = Button(axl_bg, text="NOTES", command=viewNotes)
button_notes.pack(anchor=NE, pady='5')

button_tasks  = Button(axl_bg, text="TASKS", command=viewTask)
button_tasks.pack(anchor=NE, pady='5')

button_comm     = Button(axl_bg, text="COMMAND\nPANEL", command=viewComm)
button_comm.pack(anchor=NE, pady='5')

button_settings = Button(axl_bg, text="SETTINGS", command=viewSettings)
button_settings.pack(anchor=NE, pady='5')

#=======Styling Widgets=======
#List of Interface Menus
panels = [axl_bg, note_bg, cal_bg, task_bg, set_bg, com_bg]

#Apply styles to Labels and Buttons
def configureObjects():
    for panel in panels:
        for wid in panel.winfo_children():
            if isinstance(wid, Label):
                wid.configure(foreground=pgt.pet_text_colour, background=pgt.pet_button_colour)
            elif isinstance(wid, Button):
                wid.configure(relief=pgt.pet_button_relief ,foreground=pgt.pet_text_colour, background=pgt.pet_button_colour,
                          activeforeground=pgt.pet_text_colour, activebackground=pgt.pet_button_pressed, 
                          borderwidth=pgt.pet_border, height='2', width='9')
                changeOnHover(wid)
