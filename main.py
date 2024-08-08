from tkinter import  *


window = Tk()
window.geometry("600x600")
window.maxsize(800,800)
window.minsize(300,300)
window.title("Profile downloader")
#label
label = Label(window, text ="Hello And Welcome" ,fg="blue",bg="black")
label.pack()
#button
def hello():
    print(input.get())
    button.config(text="hello python GUI")
button =Button(window,text="Click Here",fg="red" ,bg="yellow",command=hello)
button.place(x=30,y=70)
#input
input =Entry(window)
input.pack()

window.mainloop()
window.mainloop()