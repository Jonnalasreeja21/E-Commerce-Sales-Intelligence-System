from record import RecordManager
from visualization import SalesVisualization

# Create Objects
obj = RecordManager("sales_data.csv")
chart = SalesVisualization("sales_data.csv")

while True:

    print("\n" + "=" * 55)
    print("     E-COMMERCE SALES INTELLIGENCE SYSTEM")
    print("=" * 55)

    print("1. View Sales Data")
    print("2. Total Sales")
    print("3. Total Quantity Sold")
    print("4. Best Selling Product")
    print("5. Category Wise Sales")
    print("6. Region Wise Sales")
    print("7. Monthly Sales")
    print("8. Bar Chart")
    print("9. Add Record")
    print("10. Update Record")
    print("11. Delete Record")
    print("12. Search Record")
    print("13. Exit")

    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if choice == 1:
        obj.view_data()

    elif choice == 2:
        obj.total_sales()

    elif choice == 3:
        obj.total_quantity()

    elif choice == 4:
        obj.best_selling_product()

    elif choice == 5:
        obj.category_sales()

    elif choice == 6:
        obj.region_sales()

    elif choice == 7:
        obj.monthly_sales()

    elif choice == 8:
        chart.bar_chart()

    elif choice == 9:
        obj.add_record()

    elif choice == 10:
        obj.update_record()

    elif choice == 11:
        obj.delete_record()

    elif choice == 12:
        obj.search_record()

    elif choice == 13:
        print("\n===================================")
        print(" Thank You for Using the System ")
        print("===================================")
        break

    else:
        print("Invalid Choice! Please try again.")