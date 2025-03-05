import mysql.connector

# Function to connect to MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="rohit",
        database="MovieDB"
    )

# Function to get movie recommendations
def get_movie_recommendation(language, genre):
    db = connect_db()
    cursor = db.cursor()

    # Query to fetch movies based on user input
    query = "SELECT title, release_year FROM Movies WHERE language = %s AND genre = %s"
    cursor.execute(query, (language, genre))
    results = cursor.fetchall()

    db.close()
    return results

# Function to insert a movie into the database
def insert_movie():
    db = connect_db()
    cursor = db.cursor()

    # Asking user for movie details
    title = input("Enter the movie title: ")
    language = input("Enter the movie language: ")
    genre = input("Enter the movie genre: ")
    release_year = input("Enter the release year: ")

    # Inserting the movie into the database
    insert_query = "INSERT INTO Movies (title, language, genre, release_year) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (title, language, genre, release_year))
    db.commit()

    print(f"Movie '{title}' has been added to the database.")
    db.close()

# Main function to interact with the user
def main():
    while True:
        print("\n--- Movie Recommendation System ---")
        print("1. Get a movie recommendation")
        print("2. Add a movie to the database")
        print("3. Exit")

        choice = input("Please choose an option (1, 2, or 3): ")

        if choice == "1":
            language = input("Enter preferred language: ")
            genre = input("Enter preferred genre: ")
            recommendations = get_movie_recommendation(language, genre)
            
            if recommendations:
                print("\n--- Movie Recommendations ---")
                for movie in recommendations:
                    print(f"Title: {movie[0]}, Release Year: {movie[1]}")
            else:
                print("No movies found matching your criteria.")
            
            # Ask if the user wants more recommendations
            another_recommendation = input("Do you want do further any activity? (yes/no): ").lower()
            if another_recommendation == "no":
                continue
        
        elif choice == "2":
            # Insert a movie into the database
            insert_movie()
        
        elif choice == "3":
            print("Thank you for using the Movie Recommendation System. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
