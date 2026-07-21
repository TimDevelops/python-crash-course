# each lemonade is $1.50
# add another day to week 2
# combine the 2 lists into the sales list
# calculate/print how much earned on best day, worst day, separately, and in total


sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

sales_w2.append(8)

sales = sales_w1 + sales_w2
earned_best_day = max(sales) * 1.5
earned_worst_day = min(sales) * 1.5
earned_week1 = sum(sales_w1) * 1.5
earned_week2 = sum(sales_w2) * 1.5
earned_total = sum(sales) * 1.5

print(f"Best Sales Day: ${earned_best_day:.2f}")
print(f"Worse Sales Day: ${earned_worst_day:.2f}")
print(f"Week 1 Sales: ${earned_week1:.2f}\nWeek 2 Sales: ${earned_week2:.2f}\nTotal Sales: ${earned_total:.2f}")