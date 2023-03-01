import tkinter as Y
calculation = ""
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    print(calculation)
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")

root = Y.Tk()
root.title("CALCULATOR")
root.geometry("275x275")

text_result = Y.Text(root,height=1.5,width=15,font=("Arial",24),bg="gray")
text_result.grid(columnspan=5)
b_1=Y.Button(root,text="1",command=lambda: add_to_calculation(1),width=5,font=("Arial",14))
b_1.grid(row=3,column=1)
b_2=Y.Button(root,text="2",command=lambda: add_to_calculation(2),width=5,font=("Arial",14))
b_2.grid(row=3,column=2)
b_3=Y.Button(root,text="3",command=lambda: add_to_calculation(3),width=5,font=("Arial",14))
b_3.grid(row=3,column=3)
b_4=Y.Button(root,text="4",command=lambda: add_to_calculation(4),width=5,font=("Arial",14))
b_4.grid(row=4,column=1)
b_5=Y.Button(root,text="5",command=lambda: add_to_calculation(5),width=5,font=("Arial",14))
b_5.grid(row=4,column=2)
b_6=Y.Button(root,text="6",command=lambda: add_to_calculation(6),width=5,font=("Arial",14))
b_6.grid(row=4,column=3)
b_7=Y.Button(root,text="7",command=lambda: add_to_calculation(7),width=5,font=("Arial",14))
b_7.grid(row=5,column=1)
b_8=Y.Button(root,text="8",command=lambda: add_to_calculation(8),width=5,font=("Arial",14))
b_8.grid(row=5,column=2)
b_9=Y.Button(root,text="9",command=lambda: add_to_calculation(9),width=5,font=("Arial",14))
b_9.grid(row=5,column=3)
b_0=Y.Button(root,text="0",command=lambda: add_to_calculation(0),width=5,font=("Arial",14))
b_0.grid(row=6,column=2)
b_dot=Y.Button(root,text=".",command=lambda: add_to_calculation("."),width=5,font=("Arial",14))
b_dot.grid(row=6,column=1)
b_plus=Y.Button(root,text="+",command=lambda: add_to_calculation("+"),width=5,font=("Arial",14))
b_plus.grid(row=2,column=4)
b_minus=Y.Button(root,text="-",command=lambda: add_to_calculation("-"),width=5,font=("Arial",14))
b_minus.grid(row=3,column=4)
b_mul=Y.Button(root,text="*",command=lambda: add_to_calculation("*"),width=5,font=("Arial",14))
b_mul.grid(row=4,column=4)
b_div=Y.Button(root,text="/",command=lambda: add_to_calculation("/"),width=5,font=("Arial",14))
b_div.grid(row=5,column=4)
b_open=Y.Button(root,text="(",command=lambda: add_to_calculation("("),width=5,font=("Arial",14))
b_open.grid(row=2,column=2)
b_close=Y.Button(root,text=")",command=lambda: add_to_calculation(")"),width=5,font=("Arial",14))
b_close.grid(row=2,column=3)
b_equals=Y.Button(root,text="=",command= evaluate_calculation,width=11,font=("Arial",14))
b_equals.grid(row=6,column=3,columnspan=2)
b_clear=Y.Button(root,text="C",command= clear_field,width=5,font=("Arial",14))
b_clear.grid(row=2,column=1)

root.mainloop()
