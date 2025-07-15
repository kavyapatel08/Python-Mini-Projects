from tkinter import *
from tkinter import ttk,messagebox

menu = {
    "Pizza":40,
    "Pasta":30,
    "Juice":20,
    "Sandwich":120,
    "Burger":60,
    "Coffee":50,
    "MilkTea":10,
    "Espresso":180
}
orders=[]

def add_to_cart():
    item = item_var.get()
    try:
        qty=int(qty_var.get())
        if qty<=0:
            raise ValueError
        orders.append((item,qty,menu[item]))
        update_details()
    except:
        messagebox.showerror("Please Enter a valid Quantity")


def update_details():
    text.delete("1.0", END)
    text.insert(END, "Your Order Summary\n")
    text.insert(END, "-----------------------\n")
    
    total = 0 

    for item, qty, price in orders:
        item_total = price * qty
        total += item_total
        text.insert(END, f"{item} x {qty} = ₹{item_total}\n")

    text.insert(END, "-----------------------\n")
    text.insert(END, f"Your Total Pay is: ₹{total}")


#Note : We use END because--> "Before printing a new order summary each time, the old content is cleared. Otherwise, the new orders would keep getting appended below the previous ones."
def checkout():
    if not orders:
        messagebox.showinfo("No Orders","You have not Added Anything yet!")
    else:
        messagebox.showinfo("Thank You","Your Order has been Placed. Visit Again!!!")    

def clear_cart():
    orders.clear()
    text.delete("1.0",END)
    text.insert(END,"Your Cart is Empty")
#---------For GUI using Tkinter---------#

root = Tk()   #Create Object of Tk() class
root.geometry("400x550")
root.title("Cafe Management System")
root.configure(background="#E0D1DF") #Windows Background

#Label 
l = Label(root,text="Welcome To Sip Glitz Cafe",font=("arial",17,"bold"),fg = "#5D139E",bg="#E0D1DF").pack(pady=5)

frame = Frame(root,bg="#E0D1DF")
frame.pack()

#DropDown menu
item_var =StringVar()
dd = ttk.Combobox(frame,textvariable=item_var,values=list(menu.keys()),width = 20,height=5)
dd.set("Select Item")
dd.grid(row=0,column=0,padx=5,pady=10)

#Quantity
qty_var = StringVar() 
entry = Entry(frame,textvariable=qty_var,width=10)
entry.grid(row=0,column=1,padx=5,pady=10)
qty_var.set("1")

#Add to Cart
bt = Button(frame,text="Add to Cart",bg="#C45EBD",fg = "white",font=("arial",10,"bold"),command=add_to_cart)
bt.grid(row=0,column=2,padx=5,pady=10)

text_frame = Frame(root)
text_frame.pack()

scroll = Scrollbar(text_frame)
scroll.pack(side=RIGHT, fill=Y)

#Text Area to display Total Order Summary
text = Text(text_frame,height=15,width=45,bg="white",font=("arial",13))
text.pack(pady = 20)

#Checkout
bt2 = Button(root,text="Checkout",fg="white",bg="#AE43A7",command=checkout,font=("arial",15,"bold"))
bt2.pack(pady= 10)

bt3 = Button(root, text="Clear Cart", fg="white", bg="#BA58B4", command=clear_cart, font=("arial", 12, "bold"))
bt3.pack(pady=5)
root.mainloop()