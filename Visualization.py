# Python program to plot a line chart showing the  Progress Report Chart
import matplotlib.pyplot as plt
X=["English","Maths","Hindi"]
Y=["88","90","94"]
plt.plot(X,Y,"r")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Progress Report Chart")
plt.show()


# Write a Python program to plot a line chart showing the Match Summary
import matplotlib.pyplot as plt

# First team's data
x1 = [6, 8, 10, 12, 14, 16, 18, 20]
y1 = [25, 50, 75, 100, 125, 150, 175, 200]
plt.plot(x1, y1, 'r', label='Team A')  # Red line

# Second team's data
x2 = [6, 8, 10, 12, 14, 16, 18, 20]
y2 = [25, 40, 73, 85, 95, 140, 185, 210]
plt.plot(x2, y2, 'y', label='Team B')  # Yellow line

# Labels and title
plt.xlabel("Overs")
plt.ylabel("Runs")
plt.title("Match Summary")

# Add grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()


# Write a Python program to compare the performance of students mark using histogram.
import matplotlib.pyplot as plt
from numpy.random import randint

v=randint(0,10,100)
plt.hist(v,bins=10,edgecolor='blue',facecolor='red')
plt.xlabel("Marks")
plt.ylabel("No of students")
plt.title("Histogram Plot")
plt.show()

# Write a Python program to plot the pie chart for Department analysis
import matplotlib.pyplot as plt
slices=[50,20,15,10,5]
dept=['Sales','HR','Finance','Production','Account'] 
cols=['magenta', 'cyan', 'green', 'red', 'blue']
exp=[0,0.2,0.3,0,0]
plt.pie(slices, labels=dept, colors=cols, startangle=90, explode=exp, shadow=True, autopct='%.1f') 
plt.title('KVS')
plt.legend()
plt.show()