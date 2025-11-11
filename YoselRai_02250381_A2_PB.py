# YoselRai_02250381_A2_PB.py

def bubble_sort_student_names(names):
    """
    Sort student names alphabetically using bubble sort.

    Args:
        names (list): List of student names to sort

    Returns:
        list: Sorted list of names
    """
    n = len(names)
    names_copy = names.copy()
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if names_copy[j] > names_copy[j + 1]:
                names_copy[j], names_copy[j + 1] = names_copy[j + 1], names_copy[j]
    
    return names_copy


def insertion_sort_scores(scores):
    """
    Sort test scores in ascending order using insertion sort.

    Args:
        scores (list): List of test scores to sort

    Returns:
        list: Sorted list of scores
    """
    scores_copy = scores.copy()
    
    for i in range(1, len(scores_copy)):
        key = scores_copy[i]
        j = i - 1
        while j >= 0 and key < scores_copy[j]:
            scores_copy[j + 1] = scores_copy[j]
            j -= 1
        scores_copy[j + 1] = key
    
    return scores_copy


def quick_sort_book_prices(prices, recursive_calls=0):
    """
    Sort book prices in ascending order using quick sort.

    Args:
        prices (list): List of book prices to sort
        recursive_calls (int): Counter for recursive calls

    Returns:
        tuple: (sorted_list, recursive_calls_count)
    """
    if len(prices) <= 1:
        return prices, recursive_calls
    
    pivot = prices[len(prices) // 2]
    left = [x for x in prices if x < pivot]
    middle = [x for x in prices if x == pivot]
    right = [x for x in prices if x > pivot]
    
    recursive_calls += 1
    
    sorted_left, recursive_calls = quick_sort_book_prices(left, recursive_calls)
    sorted_right, recursive_calls = quick_sort_book_prices(right, recursive_calls)
    
    return sorted_left + middle + sorted_right, recursive_calls


def get_default_student_names():
    """
    Return default list of student names.
    """
    return ["Kado", "Bobchu", "Zamu", "Nado", "Lemo", 
            "Alice", "John", "Emma", "David", "Sophia",
            "Michael", "Sarah", "Daniel", "Olivia", "James"]


def get_default_test_scores():
    """
    Return default list of test scores.
    """
    return [78, 45, 92, 67, 88, 54, 73, 82, 91, 59, 
            76, 85, 48, 93, 71, 89, 57, 80, 69, 95]


def get_default_book_prices():
    """
    Return default list of book prices.
    """
    return [450, 230, 678, 125, 890, 345, 560, 780, 199, 
            320, 650, 420, 290, 510, 380]


def get_student_names_from_user():
    """
    Get student names from user input.
    
    Returns:
        list: List of student names entered by user
    """
    names = []
    try:
        print("\n--- Enter Student Names for Bubble Sort ---")
        print("Enter student names one by one (enter 'done' when finished):")
        count = 1
        while True:
            name = input(f"Enter student name #{count} (or 'done' to finish): ").strip()
            if name.lower() == 'done':
                if len(names) < 2:
                    print("Error: Please enter at least 2 student names.")
                    continue
                break
            if name:
                names.append(name)
                print(f"✓ Added student: {name}")
                count += 1
            else:
                print("Error: Please enter a valid name.")
    except KeyboardInterrupt:
        print("\nInput interrupted.")
    
    return names


def get_test_scores_from_user():
    """
    Get test scores from user input.
    
    Returns:
        list: List of test scores entered by user
    """
    scores = []
    try:
        print("\n--- Enter Test Scores for Insertion Sort ---")
        print("Enter test scores one by one (enter 'done' when finished):")
        count = 1
        while True:
            score_input = input(f"Enter test score #{count} (or 'done' to finish): ").strip()
            if score_input.lower() == 'done':
                if len(scores) < 2:
                    print("Error: Please enter at least 2 test scores.")
                    continue
                break
            try:
                score = float(score_input)
                scores.append(score)
                print(f"✓ Added test score: {score}")
                count += 1
            except ValueError:
                print("Error: Please enter a valid number for test score.")
    except KeyboardInterrupt:
        print("\nInput interrupted.")
    
    return scores


def get_book_prices_from_user():
    """
    Get book prices from user input.
    
    Returns:
        list: List of book prices entered by user
    """
    prices = []
    try:
        print("\n--- Enter Book Prices for Quick Sort ---")
        print("Enter book prices one by one (enter 'done' when finished):")
        count = 1
        while True:
            price_input = input(f"Enter book price #{count} (or 'done' to finish): ").strip()
            if price_input.lower() == 'done':
                if len(prices) < 2:
                    print("Error: Please enter at least 2 book prices.")
                    continue
                break
            try:
                price = float(price_input)
                prices.append(price)
                print(f"✓ Added book price: {price}")
                count += 1
            except ValueError:
                print("Error: Please enter a valid number for book price.")
    except KeyboardInterrupt:
        print("\nInput interrupted.")
    
    return prices


def choose_data_source(data_type):
    """
    Let user choose between default data or entering their own data.
    
    Args:
        data_type (str): Type of data ('names', 'scores', or 'prices')
    
    Returns:
        list: Chosen data list
    """
    while True:
        print(f"\nChoose data source for {data_type}:")
        print("1. Use default data")
        print("2. Enter my own data")
        
        try:
            choice = int(input("Enter your choice (1-2): "))
            
            if choice == 1:
                if data_type == 'names':
                    data = get_default_student_names()
                    print(f"Using default student names: {data}")
                    return data
                elif data_type == 'scores':
                    data = get_default_test_scores()
                    print(f"Using default test scores: {data}")
                    return data
                else:  # prices
                    data = get_default_book_prices()
                    print(f"Using default book prices: {data}")
                    return data
            elif choice == 2:
                if data_type == 'names':
                    return get_student_names_from_user()
                elif data_type == 'scores':
                    return get_test_scores_from_user()
                else:  # prices
                    return get_book_prices_from_user()
            else:
                print("Error: Please enter 1 or 2.")
        except ValueError:
            print("Error: Please enter a valid integer (1-2).")


def bubble_sort_operation():
    """
    Execute bubble sort operation for student names.
    
    User chooses between default data or entering their own data.
    """
    print("\n" + "="*60)
    print("BUBBLE SORT - Sort Student Names")
    print("="*60)
    
    student_names = choose_data_source('names')
    
    if not student_names:
        print("No names available. Returning to main menu.")
        return
    
    print(f"\nOriginal names: {student_names}")
    print("\nPerforming Bubble Sort...")
    sorted_names = bubble_sort_student_names(student_names)
    
    print("\n" + "-"*40)
    print("SORTING COMPLETE!")
    print(f"Sorted names: {sorted_names}")
    print("-"*40)


def insertion_sort_operation():
    """
    Execute insertion sort operation for test scores.
    
    User chooses between default data or entering their own data.
    """
    print("\n" + "="*60)
    print("INSERTION SORT - Sort Test Scores")
    print("="*60)
    
    test_scores = choose_data_source('scores')
    
    if not test_scores:
        print("No scores available. Returning to main menu.")
        return
    
    print(f"\nOriginal scores: {test_scores}")
    print("\nPerforming Insertion Sort...")
    sorted_scores = insertion_sort_scores(test_scores)
    
    print("\n" + "-"*40)
    print("SORTING COMPLETE!")
    print(f"Sorted scores: {sorted_scores}")
    
    top_5 = sorted_scores[-5:][::-1]
    print("\nTop 5 Scores:")
    for i, score in enumerate(top_5, 1):
        print(f"{i}. {score}")
    print("-"*40)


def quick_sort_operation():
    """
    Execute quick sort operation for book prices.
    
    User chooses between default data or entering their own data.
    """
    print("\n" + "="*60)
    print("QUICK SORT - Sort Book Prices")
    print("="*60)
    
    book_prices = choose_data_source('prices')
    
    if not book_prices:
        print("No prices available. Returning to main menu.")
        return
    
    print(f"\nOriginal prices: {book_prices}")
    print("\nPerforming Quick Sort...")
    sorted_prices, recursive_calls = quick_sort_book_prices(book_prices)
    
    print("\n" + "-"*40)
    print("SORTING COMPLETE!")
    print(f"Sorted prices: {sorted_prices}")
    print(f"Recursive calls: {recursive_calls}")
    print("-"*40)


def display_sort_menu():
    """
    Display the sorting algorithms menu.
    """
    print("\n" + "="*80)
    print()
    print("=== SORTING ALGORITHMS PROGRAM ===")
    print()
    print("Select a sorting operation (1-4):")
    print("1. Bubble Sort - Sort Student Names")
    print("2. Insertion Sort - Sort Test Scores")
    print("3. Quick Sort - Sort Book Prices")
    print("4. Exit program")
    print()
    print("="*80)
    print()


def main():
    """
    Main function to run the sorting program.

    Continuously displays the menu and executes selected sorting operations
    until the user chooses to exit.
    """
    print("(づ￣ ³￣)づ Welcome to the Sorting Algorithms Program! ヽ(°〇°)ﾉ")
    print("You can choose to use default data or enter your own data for each operation!")

    while True:
        display_sort_menu()

        try:
            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                bubble_sort_operation()
            elif choice == 2:
                insertion_sort_operation()
            elif choice == 3:
                quick_sort_operation()
            elif choice == 4:
                print("\nThank you for using the sorting program! (⌒‿⌒)")
                break
            else:
                print("Error: Please enter a valid choice (1-4).")
                continue

            if choice != 4:
                while True:
                    cont_choice = input("\nWould you like to perform another sort? (y/n): ").strip().lower()
                    if cont_choice == "n":
                        print("\nThank you for using the sorting program! (⌒‿⌒)")
                        exit()
                    elif cont_choice == "y":
                        break
                    else:
                        print("Error: Please enter 'y' or 'n'.")
                        
        except ValueError:
            print("Error: Please enter a valid integer (1-4).")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting... (ﾉ≧∇≦)ﾉ ﾐ ┻━┻")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()