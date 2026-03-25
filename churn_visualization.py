import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

print("Script started")

churn_yes = 0
churn_no = 0

with open("bigdata.csv") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        if row[16].strip() == "TRUE":
            churn_yes += 1
        else:
            churn_no += 1

print("Churn:", churn_yes)
print("No Churn:", churn_no)

labels = ["Churn", "No Churn"]
values = [churn_yes, churn_no]

plt.bar(labels, values)
plt.title("Customer Churn Distribution")
plt.ylabel("Number of Customers")

plt.savefig("churn_analysis.png")

print("Graph saved as churn_analysis.png")
