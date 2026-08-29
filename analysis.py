import pandas as pd


class SalesAnalysis:

    def __init__(self, file):
        self.file = file
        self.df = pd.read_csv(file)

        # Calculate total sales for each record
        self.df["Total"] = self.df["Price"] * self.df["Quantity"]

    def view_data(self):
        print("\n========== SALES DATA ==========")
        print(self.df.to_string(index=False))

    def total_sales(self):
        print("\n========== TOTAL SALES ==========")
        print(f"₹{self.df['Total'].sum():,.2f}")

    def total_quantity(self):
        print("\n========== TOTAL QUANTITY SOLD ==========")
        print(self.df["Quantity"].sum())

    def product_list(self):
        print("\n========== PRODUCT LIST ==========")

        products = sorted(self.df["Product"].unique())

        for i, product in enumerate(products, start=1):
            print(f"{i}. {product}")

    def best_selling_product(self):
        print("\n========== BEST SELLING PRODUCT ==========")

        result = (
            self.df.groupby("Product")["Quantity"]
            .sum()
            .sort_values(ascending=False)
        )

        print(result)

    def category_sales(self):
        print("\n========== CATEGORY WISE SALES ==========")

        result = (
            self.df.groupby("Category")["Total"]
            .sum()
            .sort_values(ascending=False)
        )

        print(result)

    def region_sales(self):
        print("\n========== REGION WISE SALES ==========")

        result = (
            self.df.groupby("Region")["Total"]
            .sum()
            .sort_values(ascending=False)
        )

        print(result)

    def monthly_sales(self):
        print("\n========== MONTHLY SALES ==========")

        temp = self.df.copy()

        # Handle mixed date formats
        # Example: 21-07-2026 and 2026-01-10
        temp["Date"] = pd.to_datetime(
            temp["Date"],
            format="mixed",
            dayfirst=True
        )

        # Get month number and month name
        temp["Month_No"] = temp["Date"].dt.month
        temp["Month"] = temp["Date"].dt.month_name()

        # Calculate monthly sales
        result = (
            temp.groupby(["Month_No", "Month"])["Total"]
            .sum()
            .reset_index()
            .sort_values("Month_No")
        )

        # Display result
        print(
            result[["Month", "Total"]]
            .to_string(index=False)
        )