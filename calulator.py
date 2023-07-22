from tkinter import *


root = Tk()
root.title("Simple Calculator")

calulator_screen = Entry(root, borderwidth=5, width=25,font="15" )
calulator_screen.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = calulator_screen.get()
    calulator_screen.delete(0, END)
    calulator_screen.insert(0, str(current)+str(number))

def button_clear():
    calulator_screen.delete(0,END)

def button_add():
    first_number = calulator_screen.get()
    global f_num
    global process
    process = 'addition'
    f_num=int(first_number)
    calulator_screen.delete(0, END)

def button_sub():
    first_number = calulator_screen.get()
    global f_num
    global process
    process = 'subraction'
    f_num = int(first_number)
    calulator_screen.delete(0, END)

def button_multiply():
    first_number = calulator_screen.get()
    global f_num
    global process
    process = 'multiply'
    f_num = int(first_number)
    calulator_screen.delete(0, END)

def button_division():
    first_number = calulator_screen.get()
    global f_num
    global process
    process = 'division'
    f_num = int(first_number)
    calulator_screen.delete(0, END)
def button_answer():
    if process=='addition':
        second_number = calulator_screen.get()
        calulator_screen.delete(0, END)
        calulator_screen.insert(0, f_num + int(second_number))

    elif process=='subraction':
        second_number = calulator_screen.get()
        calulator_screen.delete(0, END)
        calulator_screen.insert(0, f_num - int(second_number))

    elif process=='multiply':
        second_number = calulator_screen.get()
        calulator_screen.delete(0, END)
        calulator_screen.insert(0, f_num * int(second_number))

    else:
        second_number = calulator_screen.get()
        calulator_screen.delete(0, END)
        calulator_screen.insert(0, f_num / int(second_number))


button1 = Button(root, text='1', padx=35, pady=15,font= ('15'), command=lambda : button_click(1)).grid(row=1, column=0)
button2 = Button(root, text='2', padx=35, pady=15,font= ('15'), command=lambda : button_click(2)).grid(row=1, column=1)
button3 = Button(root, text='3', padx=35 , pady=15,font= ('15'), command=lambda : button_click(3)).grid(row=1, column=2)
button4 = Button(root, text='4', padx=35, pady=15,font= ('15'), command=lambda : button_click(4)).grid(row=2, column=0)
button5 = Button(root, text='5', padx=35, pady=15,font= ('15'), command=lambda : button_click(5)).grid(row=2, column=1)
button6 = Button(root, text='6', padx=35, pady=15,font= ('15'), command=lambda : button_click(6)).grid(row=2, column=2)
button7 = Button(root, text='7', padx=35, pady=15,font= ('15'), command=lambda : button_click(7)).grid(row=3, column=0)
button8 = Button(root, text='8', padx=35, pady=15,font= ('15'), command=lambda : button_click(8)).grid(row=3, column=1)
button9 = Button(root, text='9', padx=35, pady=15,font= ('15') ,command=lambda : button_click(9)).grid(row=3, column=2)
button0 = Button(root, text='0', padx=35, pady=15,font= ('15') ,command=lambda : button_click(0)).grid(row=4, column=0)
button_addition = Button(root, text='+', padx=34, pady=20,font= ('15'), command= button_add).grid(row=5, column=0)
button_subraction = Button(root, text='-', padx=36, pady=20,font= ('15'), command= button_sub).grid(row=6, column=0)
button_multiply = Button(root, text='*', padx=40, pady=20,font= ('15'), command= button_multiply).grid(row=6, column=1)
button_division = Button(root, text='/', padx=40, pady=20, font= ('15'),command= button_division).grid(row=6, column=2)
button_clear = Button(root, text='Clear', padx=70, pady=15,font= ('15') ,command=button_clear).grid(row=4, column=1, columnspan=2)
button_answer = Button(root, text='=', padx=85, pady=20,font= ('15'), command= button_answer).grid(row=5, column=1, columnspan=2)

root.mainloop()
