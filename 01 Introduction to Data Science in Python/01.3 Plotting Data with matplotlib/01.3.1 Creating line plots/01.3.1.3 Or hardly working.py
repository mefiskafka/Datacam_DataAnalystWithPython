"""
Or hardly working?
Two other officers have been working with Deshaun to help find Bayes. Their names are Officer Mengfei and Officer Aditya. Deshaun used their time cards to create two more DataFrames: mengfei and aditya. In this exercise, we'll plot all three lines together to see who was working hard each day.

We've already loaded matplotlib under the alias plt.

"""

# Plot Officer Deshaun's hours_worked vs. day_of_week
plt.plot(deshaun.day_of_week, deshaun.hours_worked)

# Plot Officer Aditya's hours_worked vs. day_of_week
plt.plot(aditya.day_of_week, aditya.hours_worked)

# Plot Officer Mengfei's hours_worked vs. day_of_week
plt.plot(mengfei.day_of_week, mengfei.hours_worked)

# Display all three line plots
plt.show()