"""
CS 1.1 Problem Statement
Welcome to your first project. As a creator, you always like to imagine the
final product in advance. Here I want you to develop a company catalog.
Assume that this company sells three different dry fruits-Apricot, Dates, and
Almond. The seller can sell individual items or a combination of these items.
A gift pack is a special combination that contains all three items. Here are
some special considerations:
If a customer purchases individual items, he does not
receive any discount.
If a customer purchases a combo pack with two unique
items, he gets a 10% discount.
If the customer purchases a gift pack, he gets a 25%
discount.
"""
companyName = "Virgo Alpha's Retail Store"
Apricots = 300
Dates = 400
Almonds = 500
dryFruits = ["Apricots", "Dates", "Almonds", "combo_1", "combo_2", "combo_3", "GiftBox"]
combo_1 = int(0.9*(Apricots + Dates))
combo_2 = int(0.9*(Almonds + Dates))
combo_3 = int(0.9*(Apricots + Almonds))
GiftBox = int(0.75*(Apricots + Dates + Almonds))

print("-"*45)
print(companyName)
print("136, Garia Station Road,")
print("Pamplemousses: 70084")
print("-"*45)
print("Product(s)\tPrice(per pack)")
print(dryFruits[0],  " "*5,  Apricots)
print(dryFruits[1],  " "*7,   Dates)
print(dryFruits[2],   " "*5, Almonds)
print(dryFruits[3],  " "*5,  combo_1)
print(dryFruits[4],  " "*5,  combo_2)
print(dryFruits[5],   " "*5, combo_3)
print(dryFruits[6],   " "*5, GiftBox)
print("*"*45)
print("For free delivery contact: 123-456-789")
print("*"*45)
