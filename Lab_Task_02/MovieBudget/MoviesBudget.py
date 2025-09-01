''' Mini Project 2: Movie Budget Project
 This program finds the average budget of movies
 and shows which movies have higher than average budget.'''

class MovieBudgetProject:
    def __init__(self, movies):
        self.movies = movies

    def add_movies(self):
        n = int(input("How many movies do you want to add? "))
        for i in range(n):
            name = input(f"Enter movie name: ")    
            budget = int(input(f"Enter budget for {name}: "))
            self.movies.append((name, budget))
        print(f"{n} movies added.")

    def calculate_average(self):
        total = sum(b for _, b in self.movies)    #just add budget
        return total / len(self.movies)

    def movies_above_average(self, avg):
        result = []
        for name, budget in self.movies:
            if budget > avg:
                result.append((name, budget, budget - avg))
        return result

    def display_results(self):
        avg = self.calculate_average()
        above = self.movies_above_average(avg)

        print("Movie Budget Analysis")
        print(f"Average budget: {avg:,.0f}")  #turns decimal into whole number

        if above:
            print("Movies above average:")
            for name, _, diff in above:
                print(f"{name} is {diff:,.0f} above average")
        else:
            print("No movies above average.")

        print(f"\nTotal movies above average: {len(above)}\n")

    def show_all_movies(self):
        print("\nAll Movies in Dataset:")
        for name, budget in self.movies:
            print(f"- {name}: {budget:,.0f}")
        print()

    def menu(self):
        while True:
            print(" Movie Budget Menu")
            print("1. Show All Movies")
            print("2. Add Movies")
            print("3. Show Average and High Budget Movies")
            print("4. Exit")

            choice = input("Enter choice (1-4): ")

            if choice == "1":
                self.show_all_movies()
            elif choice == "2":
                self.add_movies()
            elif choice == "3":
                self.display_results()
            elif choice == "4":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice, try again.\n")


movies = [
    ("Oppenheimer", 100000000),
    ("You (Season 1)", 50000000), 
    ("KGF", 80000000),           
    ("Interstellar", 165000000), 
    ("Comrade", 30000000)       
]


project = MovieBudgetProject(movies)
project.menu()
