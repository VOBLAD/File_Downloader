from tkinter import *
import wget

def downloader():
   try:
      url = tx.get("1.0", END)
      wget.download(url)
      lbl.config(text="Готово")
   except:
      lbl.config(text="Не верный URL")



root = Tk()
root.title("FileDownloader")
root.resizable(False, False)
root.config(bg="black")
root.geometry("250x500")

icon = PhotoImage(file="1.png")


btn = Button(root, image=icon, relief=FLAT, bg="black", command=downloader)
btn.pack(side=BOTTOM, pady=30)

tx = Text(root, width=25, height=3, fg="red")
tx.pack(pady=50)

lbl = Label(root, text="Введите URL", fg="white", bg="black", font="Arial 15 bold")
lbl.pack(pady=80)



root.mainloop()