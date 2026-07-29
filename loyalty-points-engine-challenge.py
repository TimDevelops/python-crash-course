# ☕️ Loyalty Points Engine Challenge
#
# RULES:
# • Each whole dollar spent earns 3 points
# • Tiers:
#     < 100 pts   →  Bronze
#     100-499 pts → Silver
#     ≥ 500 pts   →  Gold
#
# STEPS:
# 1. Define earn_points(price) → returns points for one purchase
# 2. Define tier_label(points) → returns "Bronze" / "Silver" / "Gold"
# 3. Given the hard-coded list `purchases`,
#    loop through it, call earn_points() for each amount,
#    and add the result to total_points.
# 4. After the loop, call tier_label(total_points)
# 5. Print 'Loyalty Summary':
#       • Total dollars spent
#       • Total points earned
#       • Final tier

# Purchase history (e.g., 3.75, 7.20, etc.)
purchases = [3.70, 7.20, 12.50, 45.00, 3.25, 110.00]

def earn_points(price):
    return(int(price) * 3)

def tier_label(points):
    if points < 100:
        return("Bronze")
    elif points <= 499:
        return("Silver")
    else:
        return("Gold")

total_points = 0
total_price = 0.00

for purchase in purchases:
    total_points += earn_points(purchase) 
    total_price += purchase    

print(f"====== LOYALTY SUMMARY =======")
print(f"Total dollar spent: ${total_price:.2f}")
print(f"Total points earned: {total_points}")
print(f"Final Tier: {tier_label(total_points)}")