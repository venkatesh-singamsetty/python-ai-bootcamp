import matplotlib.pyplot as plt

# Data
languages = ['Java', 'Python', 'C++', 'JavaScript']
usage = [20, 30, 15, 25]

# Create a bar chart
plt.bar(languages, usage)

# Label and title
plt.xlabel('Programming Languages')
plt.ylabel('Usage Percentage')
plt.title('Programming Language Popularity')

# Show plot
plt.show()
