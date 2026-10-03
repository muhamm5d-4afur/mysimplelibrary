from libraryclasses import Book, Library, BookNotFoundError


def main():
    library = Library()

    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Show Books")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            try:
                title = input("Title: ")
                author = input("Author: ")
                publish_date = input("Publish date (MM.YYYY): ")
                rating = float(input("Rating (1-5): "))
                price = float(input("Price: "))

                book = Book(title, author, publish_date, rating, price)
                library.add_book(book)
                print(f"'{title}' added successfully ✅")
            except ValueError as e:
                print("Error:", e)

        elif choice == "2":
            try:
                title = input("Title: ")
                library.borrow_book(title)
                print(f"'{title}' borrowed successfully ✅")
            except BookNotFoundError as e:
                print("Not found:", e)
            except ValueError as e:
                print("Error:", e)

        elif choice == "3":
            print(library)

        elif choice == "4":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()