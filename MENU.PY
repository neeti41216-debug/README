def show_menu():
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Mini Statement")
        print("6. Exit")
        print("===============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Create Account selected")

        elif choice == "2":
            print("Deposit Money selected")

        elif choice == "3":
            print("Withdraw Money selected")

        elif choice == "4":
            print("Check Balance selected")

        elif choice == "5":
            print("Mini Statement selected")

        elif choice == "6":
            print("Thank you for using Mini Statement Bank!")
            break

        else:
            print("Invalid choice. Please try again.")
