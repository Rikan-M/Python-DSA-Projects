from Store_Management import Store
import os
store=Store()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main_menu():
    """Display the main menu options."""
    print("\n===== Welcome to Cake Store Management System =====")
    print("1. Add Cake")
    print("2. Change Cake Price")
    print("3. Remove Cake")
    print("4. View Cakes by Group")
    print("5. Show All Cakes")
    print("6. Place New Order")
    print("7. Remove Order")
    print("8. Complete Urgent Order")
    print("9. View Urgent Order")
    print("10. Save Data")
    print("11. View Orders")
    print("12. Exit")
    print("==================================================")

def handle_add_cake(store):
    """Handle adding a new cake."""
    clear_screen()
    print("===== Add New Cake =====")
    name = input("Enter cake name: ")
    try:
        price = float(input("Enter cake price: "))
        
    except:
        print("Invalid Price")
        return
    flavour = input("Enter cake flavour: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(",")
    store.add_cake(name, price, flavour, ingredients)
    print(f"Cake '{name}' added successfully!")

def handle_change_cake_price(store):
    """Handle changing the price of a cake."""
    clear_screen()
    print("===== Change Cake Price =====")
    name = input("Enter cake name: ")
    try:
        old_price = float(input("Enter old price: "))
        new_price = float(input("Enter new price: "))
    except:
        print("Invalid type of price!")
        return
    store.change_cake_price(name, old_price, new_price)
    print(f"Price for '{name}' updated successfully!")

def handle_remove_cake(store):
    """Handle removing a cake."""
    clear_screen()
    print("===== Remove Cake =====")
    name = input("Enter cake name: ")
    group_name = input("Enter group name (Pastry, Normal, Expensive): ")
    confirm=store.remove_cake(name, group_name)
    if confirm:
        print(f"Cake '{name}' removed successfully!")
    else:
        print(f"Failed to delete cake {name}!")

def handle_view_cakes_by_group(store):
    """Handle viewing cakes by group."""
    clear_screen()
    print("===== View Cakes by Group =====")
    group_name = input("Enter group name (Pastry, Normal, Expensive): ")
    if group_name in store.cake_groups:
        print(f"--- {group_name} Cakes ---")
        store.show(group_name)
    else:
        print("Invalid group name!")

def handle_show_all_cakes(store):
    """Handle displaying all cakes."""
    clear_screen()
    print("===== Show All Cakes =====")
    store.show_all_cakes()

def handle_place_order(store):
    """Handle placing a new order."""
    clear_screen()
    print("===== Place New Order =====")
    cust_name = input("Enter customer name: ")
    date = input("Enter order date (YYYY-MM-DD HH:MM:SS): ")
    if not date:
        print("Can't place order! invalid date format")
        return
    order = input("Enter cake name: ")
    try:
        quantity = int(input("Enter quantity: "))
        phone_num=int(input("Enter Customer's Phone Number: "))
    except:
        print("Invalid Information")
        return
    store.new_order(cust_name, date, order, quantity,phone_num)
    print(f"Order placed successfully!")

def handle_remove_order(store):
    """Handle removing an order."""
    clear_screen()
    print("===== Remove Order =====")
    try:
        order_phone_no = int(input("Enter order phone number: "))
    except:
        print("Invalid phone number!")
        return
    result = store.remove_order(order_phone_no)
    if result:
        print("Order removed successfully!")
    else:
        pass

def handle_complete_urgent_order(store):
    """Handle marking an urgent order as completed."""
    clear_screen()
    print("===== Complete Urgent Order =====")
    result = store.urgent_order_completed()
    if result:
        print(f"Urgent order '{result}' marked as completed!")
    else:
        print("No urgent orders found!")

def handle_view_urgent_order(store):
    """Handle viewing the most urgent order."""
    clear_screen()
    print("===== View Urgent Order =====")
    result = store.get_urgent_order()
    if result:
        print(f"Urgent Order: ")
        for i in result:
            print(i, " : ",result[i])
    else:
        print("No urgent orders found!")

def main():
    store = Store()
    while True:
        clear_screen()
        main_menu()
        choice = input("Enter your choice (1-12): ")
        if choice == "1":
            handle_add_cake(store)
        elif choice == "2":
            handle_change_cake_price(store)
        elif choice == "3":
            handle_remove_cake(store)
        elif choice == "4":
            handle_view_cakes_by_group(store)
        elif choice == "5":
            handle_show_all_cakes(store)
        elif choice == "6":
            handle_place_order(store)
        elif choice == "7":
            handle_remove_order(store)
        elif choice == "8":
            handle_complete_urgent_order(store)
        elif choice == "9":
            handle_view_urgent_order(store)
        elif choice == "10":
            store.save()
            print("Data saved successfully!")
        elif choice=='11':
            store.show_all_customers()
        elif choice == "12":
            print("Exiting the Cake Store Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
        input("\nPress Enter to return to the main menu...")   
if __name__ == "__main__":
    main()

