print("Welcome to our Restaurant. Here's the Menu:")
menu_dict = {"Pizza":50,"Pasta":30,"Burger":80,"Coffee":90,"Salad":10,"Sandwich":120,"Juice":40}

print("---------Menu---------")
for i,j in menu_dict.items():
    print(f"- {i}: Rs {j}")
print("----------------------")
order_total = 0
orders = []

while True:
    order = input("Enter an iten you want to order:").title()
    if order in menu_dict:
        qty= int(input(f"Enter Quantity of {order}: "))
        orders.append((order,menu_dict[order],qty))
        order_total += menu_dict[order] * qty
        print(f"Order of {order} has been added")
    else:
        print("Sorry item is not Available")
    
    ask = input("Do you Want to order anything else?(Yes/No): ")
    if (ask.lower()!="yes"):
        break
print("----------------------------------------")
for ord,price,qtyy in orders:
    total = price * qtyy
    print(f"{ord} x {qtyy} = {total}")
print("----------------------------------------")    
print(f"The Total Price to Pay is: {order_total}\n")     
print("Thank You For Visiting!!!")