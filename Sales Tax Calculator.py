#Item 1
item1Name = "Pizza"
item1Cost = 3.99
item1Amount = 2

#Item 2
item2Name = "Pie"
item2Cost = 4.99
item2Amount = 1

tax = 7.75

# multiplying cost and quantity
itemTotalCost1 = item1Cost * item1Amount
itemTotalCost2 = item2Cost * item2Amount

# sum total cost
totalCost = itemTotalCost1 + itemTotalCost2
CostAfterTax = totalCost * totalCost * tax * 0.01

#print receipt
print ("Receipt")
print ("--------------")
print ("Item 1: " + item1Name)
print ("Cost: $" + str(item1Cost))
print ("Amount:" + str(item1Amount))
print("Total Cost $" + str(itemTotalCost1))
print ("")
print ("Item 2: " + item2Name)
print ("Cost: $" + str(item2Cost))
print ("Amount:" + str(item2Amount))
print("Total Cost $" + str(itemTotalCost2))
print ("--------------")
print ("Sales Tax: " + str(tax) + "%")
print ("")
print ("SubTotal: $" + str(totalCost))
print ("Total: $" + str(CostAfterTax))