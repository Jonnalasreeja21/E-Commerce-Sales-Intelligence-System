import pandas as pd

data = {
    "Order_ID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015],
    "Product": ["Laptop","Mobile","Shoes","Watch","Headphones","Laptop","Shoes","Mobile","Watch","Headphones","Keyboard","Mouse","T-Shirt","Jeans","Bag"],
    "Category": ["Electronics","Electronics","Fashion","Accessories","Electronics","Electronics","Fashion","Electronics","Accessories","Electronics","Electronics","Electronics","Fashion","Fashion","Accessories"],
    "Price": [50000,20000,3000,2500,1500,50000,3000,20000,2500,1500,1200,800,900,1800,2200],
    "Quantity": [2,3,5,4,6,1,3,2,5,8,10,12,15,7,6],
    "Region": ["Hyderabad","Vizag","Warangal","Hyderabad","Vijayawada","Guntur","Vizag","Hyderabad","Warangal","Guntur","Hyderabad","Vijayawada","Vizag","Warangal","Hyderabad"],
    "Date": [
        "2026-01-10","2026-01-12","2026-02-10","2026-02-15","2026-03-10",
        "2026-03-18","2026-04-02","2026-04-11","2026-05-05","2026-05-15",
        "2026-06-05","2026-06-12","2026-07-08","2026-07-15","2026-08-01"
    ]
}

df = pd.DataFrame(data)

df.to_csv("sales_data.csv", index=False)

print("sales_data.csv created successfully!")