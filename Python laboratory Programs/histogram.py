from collections import Counter
import matplotlib.pyplot as plt

grades = [83, 95, 91, 87, 0, 85, 82, 100, 67, 73, 77, 0]
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)
plt.bar([x + 5 for x in histogram.keys()], histogram.values(), 10, edgecolor=(0, 0, 0.1))
plt.axis([0, 105, 0, 5])
plt.xticks([10*i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of students")
plt.title("Distribution of exam 1 grades")
plt.show()
