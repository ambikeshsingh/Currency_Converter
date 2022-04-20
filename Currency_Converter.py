from tkinter import *

class Converter:
    def __init__(self):
        window=Tk()
        window.title("Currency_Converter")
        window.config(bg="Blue")

        Label(window,font="Helvetica 12 bold",bg="red",text="Amount to convert").grid(row=1,column=1,sticky=E)
        Label(window,font="Helvetica 12 bold",bg="red",text="Conversion Rate").grid(row=2,column=1,sticky=E)
        Label(window,font="Helvetica 12 bold",bg="red",text="Converted Amount").grid(row=3,column=1,sticky=E)

        self.amount_to_convert=StringVar()
        Entry(window,textvariable=self.amount_to_convert,justify=RIGHT).grid(row=1,column=2)
        self.Conversion_rate=StringVar()
        Entry(window,textvariable=self.Conversion_rate,justify=RIGHT).grid(row=2,column=2)
        self.Converted_amount=StringVar()
        lblconverteamount=Label(window,font="Helvetica 12 bold",bg="yellow",fg="white",textvariable=self.Converted_amount).grid(row=3,column=2,sticky=E)

        btconverteamount=Button(window,font="Helvetica 12 bold",text="Convert",bg="blue", fg="white",command=self.ConvertedAmount).grid(row=4,column=2,sticky=E)
        #self.delete_all=StringVar()
        btdelete=Button(window,font="Helvetica 12 bold",text="clear",bg="red",fg="white",command=self.delete_all).grid(row=4,column=6,padx=25,pady=25,sticky=E)

        window.mainloop()

    def ConvertedAmount(self):
        amt=float(self.Conversion_rate.get())
        Converted_amount=float(self.amount_to_convert.get())*amt
        self.Converted_amount.set(format(Converted_amount,'10.2f'))

    def delete_all(self):
        self.amount_to_convert.set("")
        self.Conversion_rate.set("")
        self.Converted_amount.set("")

Converter()
