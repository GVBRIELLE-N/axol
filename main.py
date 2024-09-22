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

#=======Functions=======
def viewEmail():
    email_bg.pack(side=TOP, fill='both', expand=True)
    axl_bg.pack_forget()
    
def hideEmail():
    axl_bg.pack (side=TOP, fill='both', expand=True)
    email_bg.pack_forget()

def viewChips():
    chip_bg.pack(side=TOP, fill='both', expand=True)
    axl_bg.pack_forget()
    
def hideChips():
    axl_bg.pack(side=TOP, fill='both', expand=True)
    chip_bg.pack_forget()

def viewLibrary():
    lib_bg.pack(side=TOP, fill='both', expand=True)
    axl_bg.pack_forget()
    
def hideLibrary():
    axl_bg.pack(side=TOP, fill='both', expand=True)
    lib_bg.pack_forget()

def viewNavi():
    nav_bg.pack(side=TOP, fill='both', expand=True)
    axl_bg.pack_forget()

def hideNavi():
    axl_bg.pack(side=TOP, fill='both', expand=True)
    nav_bg.pack_forget()

def viewSettings():
    set_bg.pack(side=TOP, fill='both', expand=True)
    axl_bg.pack_forget()

def hideSettings():
    axl_bg.pack(side=TOP, fill='both', expand=True)
    set_bg.pack_forget()

def updateTime():
    time = dt.now()
    pet_time.config(text=f"{str(time)[11:19]}")
    axl_main.after(100, updateTime)

def changeOnHover(button):
    button.bind("<Enter>", func=lambda e: button.config(background=pgt.pet_button_hover, width='13'))
    button.bind("<Leave>", func=lambda e: button.config(background=pgt.pet_button_colour, width='9'))

axl_main        = tk.Tk()
width,height    = 480,360

screen_width    = axl_main.winfo_screenwidth()
screen_height   = axl_main.winfo_screenheight()

x               = (screen_width/2)  - (width/2)
y               = (screen_height/2) - (height/2)

axl_main.title         ("Axol Terminal")
axl_main.geometry      ('%dx%d+%d+%d' % (width, height, x, y))
axl_main.resizable     (False, False)
axl_main.option_add    ('*tearOff', False)

# app_icon   = PhotoImage(file='Icon.png')
# axl_main.iconphoto     (True, app_icon)

pet_themes = {0:default_theme, 1:default_dark, 2:matra_os, 
                    3:matra_os_b, 4:retro_95}

cur_theme  = 4
pgt = pet_themes[cur_theme]

#==========Frames=================
axl_bg      = Frame    (axl_main, background=pgt.pet_bg_colour)
axl_bg.pack            (side=TOP, fill=BOTH, expand=True)

pet_edgeb   = Frame    (axl_bg, background=pgt.pet_button_colour, height='15')
pet_edgeb.pack         (side=BOTTOM, fill='x')

#==========Email Elements==========
email_bg     = Frame   (axl_main, background=pgt.pet_bg_colour)

email_label  = Label   (email_bg, text="E-Mail", font=("Arial", 12))
email_label.configure  (foreground="white", background=pgt.pet_button_colour)
email_label.pack       (anchor=NE, fill='x')

email_footer = Frame   (email_bg, background=pgt.pet_button_colour, height='20')
email_footer.pack      (side=BOTTOM, fill='x')

email_exit   = Button(email_bg, text="RETURN", command=hideEmail)
email_exit.pack(side=BOTTOM, anchor=SW, pady='10')

email_main   = Button(email_bg, text="Regular Mail")
email_main.pack(side=TOP, anchor=NW, pady='5')

email_missions = Button(email_bg, text="Official\nMissions")
email_missions.pack(side=TOP, anchor=NW, pady='5')

email_tour = Button(email_bg, text="Tournament\nEntires")
email_tour.pack(side=TOP, anchor=NW, pady='5')

#==========Battle Chips Elements==========
chip_bg = Frame(axl_main, background=pgt.pet_bg_colour)

chip_label   = Label(chip_bg, text="Combat Data Folder", font=("Arial", 12))
chip_label.configure(foreground="white", background=pgt.pet_button_colour)
chip_label.pack(anchor=NE, fill='x')

chip_footer  = Frame(chip_bg, background=pgt.pet_button_colour, height='20')
chip_footer.pack(side=BOTTOM, fill='x')

chip_exit    = Button(chip_bg, text="RETURN", command=hideChips)
chip_exit.pack(side=BOTTOM, anchor=S, fill='x')

chip_scroll = Scrollbar(chip_bg, orient='vertical', troughcolor=pgt.pet_bg_colour, background=pgt.pet_button_colour, 
    borderwidth='0', activebackground=pgt.pet_button_hover)
chip_scroll.pack(side='left', fill='y')

chip_list = Listbox(chip_bg, yscrollcommand=chip_scroll.set, background=pgt.pet_button_colour, 
    foreground='white', borderwidth=0, height=20, width=14, selectbackground=pgt.pet_button_hover,
    selectforeground='white', relief='flat')
chip_list.pack(anchor=NW, fill='y')

for c in range(1,51):
    chip_list.insert(END, "ComData  #"+str(c))

chip_scroll.config(command=chip_list.yview)

#==========Chip Library Elements==========
lib_bg = Frame(axl_main, background=pgt.pet_bg_colour)

lib_label    = Label(lib_bg, text="Combat Data Library", font=("Arial", 12))
lib_label.configure(foreground="white", background=pgt.pet_button_colour)
lib_label.pack(anchor=NE, fill='x')

lib_footer   = Frame(lib_bg, background=pgt.pet_button_colour, height='20')
lib_footer.pack(side=BOTTOM, fill='x')

lib_exit     = Button(lib_bg, text="RETURN", command=hideLibrary)
lib_exit.pack(side=BOTTOM, anchor=SE, pady='10')

#==========Settings Elements==========
set_bg = Frame(axl_main, background=pgt.pet_bg_colour)

set_label   = Label(set_bg, text="AxT Settings", font=("Arial", 12))
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

#==========Navi Elements==========
nav_bg      = Frame(axl_main, background=pgt.pet_bg_colour)

nav_label   = Label(nav_bg, text="Axol Manager", font=("Arial", 12))
nav_label.configure(foreground="white", background=pgt.pet_button_colour)
nav_label.pack(anchor=NE, fill='x')

nav_footer  = Frame(nav_bg, background=pgt.pet_button_colour, height='20')
nav_footer.pack(side=BOTTOM, fill='x')

nav_exit    = Button(nav_bg, text="EXIT", command=hideNavi)
nav_exit.pack(side=BOTTOM, anchor=SE, pady='10')

#=======Labels=======
pet_zenny = Label(axl_bg, text="Axol Terminal", font=("Arial", 12))
pet_zenny.pack(anchor=NE, fill='x')

pet_time = Label(axl_bg, text="00:00", font=("Arial", 16))
pet_time.pack(side=BOTTOM, anchor=SW)

#=======Buttons=======
button_email    = Button(axl_bg, text="E-MAIL", command=viewEmail)
button_email.pack(anchor=NE, pady='5')

button_chips    = Button(axl_bg, text="CHIP\nFOLDER", command=viewChips)
button_chips.pack(anchor=NE, pady='5')

button_library  = Button(axl_bg, text="CHIP\nLIBRARY", command=viewLibrary)
button_library.pack(anchor=NE, pady='5')

button_navi     = Button(axl_bg, text="AXOL", command=viewNavi)
button_navi.pack(anchor=NE, pady='5')

button_settings = Button(axl_bg, text="SETTINGS", command=viewSettings)
button_settings.pack(anchor=NE, pady='5')

#=======Styling Widgets=======
#List of PET Menus
panels = [axl_bg, lib_bg, chip_bg, email_bg, set_bg, nav_bg]

#Apply styles to Labels and Buttons
def configureObjects():
    for panel in panels:
        for wid in panel.winfo_children():
            if isinstance(wid, Label):
                wid.configure(foreground="white", background=pgt.pet_button_colour)
            elif isinstance(wid, Button):
                wid.configure(relief='flat' ,foreground="white", background=pgt.pet_button_colour,
                          activeforeground='white', activebackground=pgt.pet_button_pressed, 
                          borderwidth='0', height='2', width='9')
                changeOnHover(wid)


if __name__ == "__main__":
    print("Axol Terminal - Prototype Build")
    print("Developed by Leothera")
    configureObjects()
    updateTime()
    axl_main.mainloop()
