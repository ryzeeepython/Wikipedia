from turtle import width
import wikipedia 
import tkinter as tk

def main():
    get = Entry.get()
    get  = get.replace(' ','')
    info = wikipedia.summary(get)
    text_box.insert(1.0, info)

window = tk.Tk()
window.geometry('700x600')
window.resizable(False,False)
greeting = tk.Label(text="Dekstop Wikipedia")
Entry = tk.Entry(width=70)
Button = tk.Button(
    window,
    text = 'OK',
    width = 10,
    height= 2,
    command=main
)
greeting.pack()
Entry.pack()
Button.pack()
Button.place(x = 500, y = 500)
text_box = tk.Text(width = 65)
text_box.pack()
text_box.place(x =100, y = 90 )





window.mainloop()