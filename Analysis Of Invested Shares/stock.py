import re

''' NOTE : THE PRINT() STATEMENTS WHICH ARE COMMENTED CAN BE UNCOMMENTED TO PRINT THE SHARES '''

# Buy
fname = open("stk_trade_2020a.txt")
count = 0
sum = 0
for line in fname:
    line = line.strip()
    source = re.findall(("(^[0-9]+-Jun-2020\s[A-Z]+\sSell+\s[A-Z]+\s[0-9]+\s[0-9]+.[0-9]+.[0-9]+)"),line)
    if not len(source)<1:
        count = count+1
        source = source[0]
        #print(source)
        source = source.split()
        month = source[0]
        month = month.split("-")
        month = month[1]
        amount = source[int(5)]
        amount = float(amount)
        sum = sum + amount
print("Total shares Sold = ", count)
print("The total amount of shares sold in", month, "=", round(sum), "Rupees")

print()

# Sell
fh = open("stk_trade_2020a.txt")
count2 = 0
sum2 = 0
for lines in fh:
    lines.strip()
    source2 = re.findall(("(^[0-9]+-Jun-2020\s[A-Z]+\sBuy+\s[A-Z]+\s[0-9]+\s[0-9]+.[0-9]+.[0-9]+)"),lines)
    if not len(source2)<1:
        count2 = count2+1
        source2 = source2[0]
        #print(source2)
        source2 = source2.split()
        month2 = source2[0]
        month2 = month2.split("-")
        month2 = month2[1]
        amount2 = source2[5]
        amount2 = float(amount2)
        sum2 = sum2 + amount2
print("Total Shares Bought = ", count2)
print("The total amount of shares bought in", month2, "=", round(sum2), "Rupees")

# Profit/Loss
print()

tot_shares = count + count2
print("Total share interaction = ", tot_shares)

total = round(sum-sum2)
if total > 1:
    print("Total Profit = ", total, "Rupees")
    profit_per = (total/(sum+sum2))*100
    print("Profit percentage = ", round(profit_per), "%")
elif total < 1:
    print("Total Loss = ", -total, "Rupees")
    loss_per = (total/(sum+sum2))*100
    print("Loss percentage = ", round(-loss_per), "%")
