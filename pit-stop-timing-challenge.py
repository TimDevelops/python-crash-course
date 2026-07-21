# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"

race_time_seconds = float(input("What was the total race time in seconds? "))
pit_stops = float(input("How many pit stops were made? "))
pit_stop_duration = float(input("What was the average pit stop duration in seconds? "))

pit_stop_time = pit_stops * pit_stop_duration
time_spent_in_pits = round(pit_stop_time / race_time_seconds * 100, 2)

print(f"Total Pit Stop Time: {pit_stop_time} seconds\nPercentage of Race Spent in Pits: {time_spent_in_pits}%")

if time_spent_in_pits > 5.0:
    print("You need a new pit crew! 🛠️")