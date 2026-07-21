# 🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost
#    - games available

name="Alex"
passes=5
tokens_per_pass=5
price_per_pass=5.00
tokens_requred=3

total_tokens=passes * tokens_per_pass
cost=passes * price_per_pass
availabe_games=total_tokens // tokens_requred

print(f"Dear {name},\nYou recently purchased {passes} passes for ${cost:.2f}, giving you {total_tokens} total tokens to use.\nYou can play up to {availabe_games} games with your purchase.\n{name}, Thank you for being a valuable customer.")