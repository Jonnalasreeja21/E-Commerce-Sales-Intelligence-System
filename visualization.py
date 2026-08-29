import pandas as pd
import matplotlib.pyplot as plt


class SalesVisualization:

    def __init__(self, file):
        self.file = file
        self.df = pd.read_csv(file)

        self.df["Total"] = (
            self.df["Price"] * self.df["Quantity"]
        )

    def bar_chart(self):
        print("\n========== BAR CHART ==========")

        result = (
            self.df.groupby("Product")["Total"]
            .sum()
            .sort_values(ascending=False)
        )

        plt.figure(figsize=(10, 6))

        plt.bar(
            result.index,
            result.values
        )

        plt.xlabel("Product")
        plt.ylabel("Sales")
        plt.title("Product Wise Sales")

        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()