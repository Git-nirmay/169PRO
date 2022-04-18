from tkinter import*

root=Tk()
root.title("Clases")
root.geometry("500x500")

class A:
    def __init__(self):
        print("This is a CreateElementClass")
    def Abc(self):
        AbCd=Label(root,text="New anime charecter created ",fg="purple")
        AbCd.pack()
        
        class_bts = Button(root, text =".", command = self.message)
        class_bts.pack()
        
    def message(self): 
        messagebox.showinfo("showinfo", "You clicked the button created using class")
        
obg=A()
btsisgood=Button(root, text ="Make New Anime Charecter", command =obg.Abc)
btsisgood.pack(padx=20,pady=10)

root.mainloop()