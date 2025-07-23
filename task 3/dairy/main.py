# main.py

from dairy_tool import DiaryEntry, save_entries, load_entries, search_entries

def add_entry(entries):
    title = input("Enter entry title: ").strip()
    content = input("Enter entry content: ").strip()

    if not title or not content:
        print("Title and content cannot be empty.")
        return

    entry = DiaryEntry(title, content)
    entries.append(entry)
    print("Diary entry added.")

def view_all(entries):
    if not entries:
        print("No diary entries found.")
        return

    for entry in entries:
        print(f"\nDate: {entry.date}")
        print(f"Title: {entry.title}")
        print(f"Content: {entry.content}")
        print("-" * 40)

def search(entries):
    keyword = input("Search by date (YYYY-MM-DD) or title keyword: ").strip()
    results = search_entries(entries, keyword)

    if not results:
        print("No matching entries found.")
        return

    for entry in results:
        print(f"\nDate: {entry.date}")
        print(f"Title: {entry.title}")
        print(f"Content: {entry.content}")
        print("-" * 40)

def main():
    entries = load_entries()

    while True:
        print("\n--- Personal Diary Menu ---")
        print("1. Add entry")
        print("2. View all entries")
        print("3. Search by date or title")
        print("4. Save & Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_entry(entries)
        elif choice == '2':
            view_all(entries)
        elif choice == '3':
            search(entries)
        elif choice == '4':
            save_entries(entries)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main()
