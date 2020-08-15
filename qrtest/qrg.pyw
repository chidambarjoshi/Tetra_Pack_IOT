from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import qrcode
root = Tk()
def genrator(*args):
    qrid= username.get()
    if(qrid==""):
        messagebox.showinfo("MESSAGE","Enter Packet ID")
        username.delete(first=0,last=100)
    else:
        x='qrcodes/'+qrid+'.png'
        z='https://tetrapack.herokuapp.com/datadisplay_user/'+qrid
        qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
                    )
        qr.add_data(z)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(x)
        messagebox.showinfo("MESSAGE","QR code is Generated")
        
    
    

root.title("QR code genrator")
root.geometry("200x200")
mainframe = ttk.Frame(root, padding="3 3 12 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

username=StringVar()

ttk.Label(mainframe, text="QR code genrator",font='times 14 bold').grid(row=0, column=0, columnspan=3)

username = ttk.Entry(mainframe, width=15, textvariable=username)
ttk.Label(mainframe, text="Packet ID").grid(column=1, row=4)
username.grid(column=2, row=4)

x=ttk.Button(mainframe, text="Genrate QRcode", command=genrator)
x.grid(row=6, column=0, columnspan=3)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.mainloop()
