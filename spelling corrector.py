from tkinter import*
from textblob import TextBlob
def clearAll():
    word_field1.delete(0,END)
    word_field2.delete(0,END)

def correction():
    input_word=word_field1.get()
    blob_obj=TextBlob(input_word)
    corrected_word=str(blob_obj.correct())
    word_field2.insert(10,corrected_word)



if __name__=="__main__":
    root=Tk()
    root.title("Spelling Correction")
    root.configure(background='light green')
    root.geometry("400x300")
    headlabel=Label(root,text="Welcome To Spelling Corrector",fg='black',bg='light green',font=('times new roman',20)).place(x=5,y=7)
    label1=Label(root,text="Input Word",bg='light green')
    label1.place(x=5,y=70)
    word_field1=Entry(root,bg='light grey')
    word_field1.place(x=85,y=70)
    button1=Button(root,text="correction",bg='red',font=(1),command=correction)
    button1.place(x=90,y=100)
    label2=Label(root,text='Corrected word',bg='light green')
    label2.place(x=6,y=150)
    word_field2=Entry(root,bg='light grey')
    word_field2.place(x=120,y=150)
    button2=Button(root,text='Clear',font=(1),bg='light grey',command=clearAll)
    button2.place(x=95,y=190)

    root.mainloop()




