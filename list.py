





mood_options = ["bad", "awful", "meh", "good", "amazing"]
weekly_scores = [2, 3, 4, 2, 1, 1, 4]

# Using list comprehension to map scores to moods
mood_per_day = [mood_options[score - 1] for score in weekly_scores]

# Displaying moods for each day
for day, mood in enumerate(mood_per_day, start=1):
    print(f"Day {day}: {mood}")