# main.py

from delivery_utils import Package, save_packages, load_packages

def register_package(packages):
    sender = input("Enter sender name: ")
    recipient = input("Enter recipient name: ")
    package = Package(sender, recipient)
    packages.append(package)
    print(f"Package registered with ID: {package.id}")

def mark_delivered(packages):
    pkg_id = input("Enter package ID to mark as delivered: ")
    for pkg in packages:
        if pkg.id == pkg_id:
            if pkg.status == "Delivered":
                print("Package is already marked as delivered.")
            else:
                pkg.status = "Delivered"
                print("Package marked as delivered.")
            return
    print("Package not found.")

def view_packages(packages):
    if not packages:
        print("No packages to display.")
        return
    for pkg in packages:
        print(f"ID: {pkg.id} | Sender: {pkg.sender} | Recipient: {pkg.recipient} | Status: {pkg.status}")

def main():
    packages = load_packages()
    print("Welcome to the Package Delivery System")

    while True:
        print("\nMenu:")
        print("1. Register a package")
        print("2. Mark package as delivered")
        print("3. View all packages")
        print("4. Save packages to file")
        print("5. Load packages from file")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register_package(packages)
        elif choice == '2':
            mark_delivered(packages)
        elif choice == '3':
            view_packages(packages)
        elif choice == '4':
            save_packages(packages)
        elif choice == '5':
            packages = load_packages()
            print("Packages loaded from file.")
        elif choice == '6':
            save_packages(packages)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
