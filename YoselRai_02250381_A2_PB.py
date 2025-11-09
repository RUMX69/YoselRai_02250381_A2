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


def bubble_sort_operation():
    """
    Execute bubble sort operation for student names.
    
    Displays original and sorted lists.
    """
    student_names = ["Kado", "Bobchu", "Zamu", "Nado", "Lemo", 
                     "Alice", "John", "Emma", "David", "Sophia",
                     "Michael", "Sarah", "Daniel", "Olivia", "James"]
    
    print(f"Original names: {student_names}")
    print("\nPerforming Bubble Sort...")
    sorted_names = bubble_sort_student_names(student_names)
    print(f"Sorted names: {sorted_names}")


def insertion_sort_operation():
    """
    Execute insertion sort operation for test scores.
    
    Displays original list, sorted list, and top 5 scores.
    """
    test_scores = [78, 45, 92, 67, 88, 54, 73, 82, 91, 59, 
                   76, 85, 48, 93, 71, 89, 57, 80, 69, 95]
    
    print(f"Original scores: {test_scores}")
    print("\nPerforming Insertion Sort...")
    sorted_scores = insertion_sort_scores(test_scores)
    print(f"Sorted scores: {sorted_scores}")
    
    top_5 = sorted_scores[-5:][::-1]
    print("\nTop 5 Scores:")
    for i, score in enumerate(top_5, 1):
        print(f"{i}. {score}")


def quick_sort_operation():
    """
    Execute quick sort operation for book prices.
    
    Displays original list, sorted list, and number of recursive calls.
    """
    book_prices = [450, 230, 678, 125, 890, 345, 560, 780, 199, 
                   320, 650, 420, 290, 510, 380]
    
    print(f"Original prices: {book_prices}")
    print("\nPerforming Quick Sort...")
    sorted_prices, recursive_calls = quick_sort_book_prices(book_prices)
    print(f"Sorted prices: {sorted_prices}")
    print(f"Recursive calls: {recursive_calls}")


def display_sort_menu():
    """
    Display the sorting algorithms menu.
    """
    print("\n" + "="*80)
    print()
    print("=== Sorting Algorithms Menu ===")
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

    while True:
        display_sort_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                bubble_sort_operation()
            elif choice == 2:
                insertion_sort_operation()
            elif choice == 3:
                quick_sort_operation()
            elif choice == 4:
                print("Thank you for using the sorting program! (⌒‿⌒)")
                break
            else:
                print("Error: Please enter a valid choice (1-4).")
                continue

            if choice != 4:
                while True:
                    cont_choice = input("\nWould you like to perform another sort? (y/n): ").strip().lower()
                    if cont_choice == "n":
                        print("Thank you for using the sorting program! (⌒‿⌒)")
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