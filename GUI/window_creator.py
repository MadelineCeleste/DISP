import tkinter as tk
from tkinter import ttk as ttk
from GUI import base_commands

def setup_menu_window(window = None):

    if window != None:
        window.destroy()

    setup_menu = tk.Tk()
    setup_menu.minsize(int(setup_menu.winfo_screenwidth()/2),int(setup_menu.winfo_screenheight()/2))
    ttk.Label(setup_menu, text="DISP: Data Interpreter for Stelum and Pulse codes").place(in_=setup_menu, relx=0.5, rely=0,anchor='n')
    setup_menu.title("DISP")
    ttk.Button(setup_menu, text="Graph maker", command=lambda: graph_maker_window(setup_menu)).place(in_=setup_menu, relx=0.25, rely=0.5,anchor='center')
    ttk.Button(setup_menu, text="Movie maker", command=lambda: base_commands.self_destruct(setup_menu)).place(in_=setup_menu, relx=0.75, rely=0.5,anchor='center')
    return(setup_menu)

def graph_maker_window(window: tk.Tk):

    window.destroy()
    graph_maker = tk.Tk()
    graph_maker.minsize(int(graph_maker.winfo_screenwidth()/2),int(graph_maker.winfo_screenheight()/2))
    ttk.Button(graph_maker, text="Graph maker", command=lambda: setup_menu_window(graph_maker)).place(in_=graph_maker, relx=0.25, rely=0.5,anchor='center')
    ttk.Button(graph_maker, text="Movie maker", command=lambda: base_commands.self_destruct(graph_maker)).place(in_=graph_maker, relx=0.75, rely=0.5,anchor='center')
    graph_maker.title("DISP")
    return(graph_maker)
