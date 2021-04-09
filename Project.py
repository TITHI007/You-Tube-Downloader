from pytube import YouTube
import tkinter as tk

root=tk.Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Downloader")

tk.Label(root,text="YouTube Video Downloader",font='arial 20 bold').pack()


link = tk.StringVar()
tk.Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = tk.Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

path = tk.StringVar()
tk.Label(root, text = 'Paste path Here:', font = 'arial 15 bold').place(x= 160 , y = 130)
link_enter = tk.Entry(root, width = 70,textvariable = path).place(x = 32, y = 160)

def Download():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download(str(path.get()))
    tk.Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)
    

tk.Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Download).place(x=180 ,y = 210)
root.mainloop()


