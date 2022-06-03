from tkinter import *

root = Tk()
root.title("ASCII NUMBERS")
root.geometry("400x400")
root.configure(background='snow')
  
enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.5,anchor=CENTER)

label = Label(root,text="NAME IN ASCII - ",bg="light yellow",fg="black")

def asciiconverter():
    input_word = enter_word.get()
    
    for letter in input_word:
        label["text"]+=str(ord(letter)) +" "
        
btn = Button(root,text="SHOW NAME IN ASCII",command=asciiconverter,bg='gold',fg='black')
btn.place(relx=0.5,rely=0.6,anchor=CENTER)
label.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()