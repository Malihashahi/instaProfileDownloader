from  tkinter import *
import  instaloader
import  urllib
from  urllib.request import urlopen
from  PIL import ImageTk
import  io
def get_image():
    L = instaloader.Instaloader()
    profile =instaloader.profile.from_username(L.context,f"{username.get()}")
    a= urlopen(profile.get_profile_pic_url()
    data= a.read()
    a.close()
    image= Image.open(io.BytesIO(data))
    pic = ImageTk.PhotoImage(image)
    label.config(image=pic)
    label.image= pic
    label.pack()



window =Tk()
window.title("instagram profile downloader")
window.geometry("600x600")
Label(window,text="Enter your instagram username").pack()
username =Entry(window,width=50)
username.pack()
button= Button(window,text="start download")
button.pack()
button.config(command=get_image)
label= Label(window)



window.mainloop()
