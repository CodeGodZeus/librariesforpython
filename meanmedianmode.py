
import numpy as np
import pandas as pd

# Import matplotlib pyplot
from matplotlib import pyplot as plt

# Read in transactions data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Save transaction times to a separate numpy array
author_ages = greatest_books['Ages']

# Use plt.hist() below
plt.hist(author_ages, range=(10, 80), bins=14,  edgecolor='black')
plt.title("Age of Top 100 Authors at Publication")
plt.xlabel("Age")
plt.ylabel("Count")

plt.show()


# Import packages
import numpy as np
import pandas as pd

# Read author data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Set author ages to a NumPy array
author_ages = greatest_books['Ages']

# Use numpy to calculate the average age of the top 100 authors
average_age = np.average(author_ages)

print("The average age of the 100 greatest authors, according to a survey by Le Monde, is: " + str(average_age))












# Import packages
import numpy as np
import pandas as pd

# Read in author data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Save author ages to author_ages
author_ages = greatest_books['Ages']

# Use numpy to calculate the median age of the top 100 authors
median_age = np.median(author_ages)

print("The median age of the 100 greatest authors, according to a survey by Le Monde is: " + str(median_age))




# Import packages
import codecademylib
import numpy as np
import pandas as pd

# Import matplotlib pyplot
from matplotlib import pyplot as plt

# Read in transactions data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Save transaction times to a separate numpy array
author_ages = greatest_books['Ages']

# Use numpy to calculate the average age of the top 100 authors
average_age = np.average(author_ages)


print("The average age of the 100 greatest authors, according to Le Monde is: " + str(average_age))

# Plot the figure
plt.hist(author_ages, range=(10, 80), bins=14,  edgecolor='black')
plt.title("Age of Top 100 Novel Authors at Publication")
plt.xlabel("Publication Age")
plt.ylabel("Count")
plt.axvline(average_age, color='r', linestyle='solid', linewidth=2, label="Mean")
plt.legend()

plt.show()






import numpy as np

# Array of the first five author ages
five_author_ages = np.array([29, 49, 42, 43, 32])

# Fill in the empty array with the values sorted
sorted_author_ages = np.array(sorted(five_author_ages))

# Save the median value to median_value
median_age = np.median(sorted_author_ages)

# Print the sorted array and median value
print("The sorted array is: " + str(sorted_author_ages))
print("The median of the array is: " + str(median_age))







from matplotlib import pyplot as plt

# Read in transactions data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Save transaction times to a separate numpy array
author_ages = greatest_books['Ages']

# Use numpy to calculate the average age of the top 100 authors
average_age = np.average(author_ages)

median_age = np.median(author_ages)

# Plot the figure
plt.hist(author_ages, range=(10, 80), bins=14,  edgecolor='black')
plt.title("Age of Top 100 Novel Authors at Publication")
plt.xlabel("Publication Age")
plt.ylabel("Count")
plt.axvline(average_age, color='r', linestyle='solid', linewidth=2, label="Mean")
plt.axvline(median_age, color='y', linestyle='solid', linewidth=2, label="Median")
plt.legend()

plt.show()
