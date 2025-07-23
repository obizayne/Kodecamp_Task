# Task 5: Movie Ticket Booking System

# Scenario: Manage ticket booking for a cinema.

# Instructions:

# - Show movie options with available seats and ticket price (dictionary)

# - Allow users to:

#  - Book a ticket (reduce seat count)

#  - View movies and seats

#  - Exit

# - Validate:

#  - That the movie exists

#  - That enough seats are available

# - Use functions, loops, error handling, and data 
movies = {
    "Red One": {"seats": 10, "price": 100},
    "justice league": {"seats": 5, "price": 150},
    "jungle book": {"seats": 60, "price": 200},  # No seats available
}

def list_movie():
    for index, movie in enumerate(movies):
        print(f"{index + 1}: {movie}")
        
    
    
def book_ticket():
    list_movie()     
    movie_name = input("Please input the movie name you want to book: ")
    if movie_name not in movies:
        print(f"Movie '{movie_name}' not found.")
        return
    
    seats_available = movies[movie_name]['seats']
    if seats_available <= 0:
        print(f"No seats available for '{movie_name}'.")
        return
    
    movies[movie_name]['seats'] -= 1
    print(f"Ticket booked successfully for '{movie_name}'. Remaining seats: {movies[movie_name]['seats']}")

def menu():
    print("1. Book a Ticket")
    print("2. view ticket")
    print("3. Exit")
    print("please input your choice: ")

def app():
    while True:
        menu()
        choice = int(input())
        try:
            if choice ==1:
                book_ticket()
            elif choice ==2:
                list_movie()
                print()
                # for index,movie in enumerate(movies):
                #     print(f"{index +1}: {movie}")
            elif choice ==3:
                print("thank you!!")
            
        except ValueError as e:
            print("Invalid input")
app()
