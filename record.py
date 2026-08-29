import pandas as pd
from analysis import SalesAnalysis


class RecordManager(SalesAnalysis):

    def __init__(self, file):
        super().__init__(file)

    def save_data(self):
        self.df.to_csv(self.file, index=False)

    def add_record(self):

        order = int(input("Order ID : "))

        if order in self.df["Order_ID"].values:
            print("Order ID Already Exists!")
            return

        product = input("Product : ")
        category = input("Category : ")
        price = float(input("Price : "))
        quantity = int(input("Quantity : "))
        region = input("Region : ")
        date = input("Date (YYYY-MM-DD) : ")

        total = price * quantity

        new_record = {
            "Order_ID": order,
            "Product": product,
            "Category": category,
            "Price": price,
            "Quantity": quantity,
            "Region": region,
            "Date": date,
            "Total": total
        }

        self.df.loc[len(self.df)] = new_record

        self.save_data()

        print("Record Added Successfully.")

    def update_record(self):

        order = int(input("Enter Order ID : "))

        index = self.df[self.df["Order_ID"] == order].index

        if len(index) == 0:
            print("Record Not Found!")
            return

        print("\nLeave blank if you don't want to change a field.")

        product = input("New Product : ")
        category = input("New Category : ")
        price = input("New Price : ")
        quantity = input("New Quantity : ")
        region = input("New Region : ")
        date = input("New Date (YYYY-MM-DD) : ")

        if product:
            self.df.at[index[0], "Product"] = product

        if category:
            self.df.at[index[0], "Category"] = category

        if price:
            self.df.at[index[0], "Price"] = float(price)

        if quantity:
            self.df.at[index[0], "Quantity"] = int(quantity)

        if region:
            self.df.at[index[0], "Region"] = region

        if date:
            self.df.at[index[0], "Date"] = date

        self.df.at[index[0], "Total"] = (
            self.df.at[index[0], "Price"] *
            self.df.at[index[0], "Quantity"]
        )

        self.save_data()

        print("Record Updated Successfully.")

    def delete_record(self):

        order = int(input("Enter Order ID : "))

        if order not in self.df["Order_ID"].values:
            print("Record Not Found!")
            return

        self.df = self.df[self.df["Order_ID"] != order]

        self.save_data()

        print("Record Deleted Successfully.")

    def search_record(self):

        product = input("Enter Product Name : ")

        result = self.df[
            self.df["Product"].str.lower() == product.lower()
        ]

        if result.empty:
            print("No Record Found.")
        else:
            print(result.to_string(index=False))