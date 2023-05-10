import matplotlib.pyplot as plt
import random

secret = random.randint(1, 100)
green_count = 0
yellow_count = 0



# Set up initial data for the plot
colors = ['#00FF00', '#FFFF00']  # Green and Yellow colors
sizes = [50, 50]  # Equal sizes to start with

# Create the plot window and plot the initial data
fig, ax = plt.subplots()
ax.pie(sizes, colors=colors, autopct='', startangle=90)
# ax.set_title('Color Distribution')

# Prompt message
print("This program displays a pie chart of color distribution based on the percentage of green color.\n")
# value = input("Enter the percentage of green color (0-100), or type 'q' to quit: ")

while True:
    if random.randint(1, 100) <= secret:
        green_count += 1
    else:
        yellow_count += 1
        
    print("Green Count:", green_count)
    print("Yellow Count:", yellow_count)
    
    if green_count + yellow_count == 5000:
        print("The secret is:", secret)
        break
    
    # # User input
    # value = input("Enter the percentage of green color (0-100), or type 'q' to quit: ")


    sizes = [green_count, yellow_count]
    ax.pie(sizes, colors=colors, autopct='', startangle=90)

        # Update the plot window
    plt.draw()
    plt.pause(0.001)

  