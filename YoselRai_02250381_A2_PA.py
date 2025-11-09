# YoselRai_02250381_A2_PA.py

def linear_search_student_id(student_ids, target_id):
    """
    Perform linear search to find a student ID in the list.

    Args:
        student_ids (list): List of student IDs to search through
        target_id (int): The student ID to search for

    Returns:
        tuple: (position, comparisons) where position is 1-indexed, comparisons is count
    """
    comparisons = 0
    for i in range(len(student_ids)):
        comparisons += 1
        if student_ids[i] == target_id:
            return i + 1, comparisons  # Return 1-indexed position
    return -1, comparisons


def binary_search_scores(scores, target_score):
    """
    Perform binary search to find a score in the sorted list.

    Args:
        scores (list): Sorted list of scores to search through
        target_score (int): The score to search for

    Returns:
        tuple: (position, comparisons) where position is 1-indexed, comparisons is count
    """
    comparisons = 0
    low = 0
    high = len(scores) - 1
    
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        
        if scores[mid] == target_score:
            return mid + 1, comparisons  # Return 1-indexed position
        elif scores[mid] < target_score:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1, comparisons


def linear_search_operation():
    """
    Execute linear search operation for student IDs.
    
    Prompts user for target ID and displays search results.
    """
    student_ids = [1001, 1005, 1002, 1008, 1003, 1010, 1004, 1009, 
                   1007, 1012, 1015, 1018, 1011, 1014, 1017, 1020, 
                   1006, 1013, 1016, 1019]
    
    try:
        print(f"Searching in the list: {student_ids}")
        target_id = int(input("Enter Student ID to search: "))
        position, comparisons = linear_search_student_id(student_ids, target_id)
        
        if position != -1:
            print(f"Result: Student ID {target_id} found at position {position}")
        else:
            print(f"Result: Student ID {target_id} not found")
        print(f"Comparisons made: {comparisons}")
        
    except ValueError:
        print("Error: Please enter a valid integer for Student ID.")


def binary_search_operation():
    """
    Execute binary search operation for scores.
    
    Prompts user for target score and displays search results.
    """
    scores = [45, 52, 58, 63, 67, 72, 75, 78, 82, 85, 
              88, 90, 92, 95, 98, 99, 100, 102, 105, 108]
    
    try:
        print(f"Sorted scores: {scores}")
        target_score = int(input("Enter score to search: "))
        position, comparisons = binary_search_scores(scores, target_score)
        
        if position != -1:
            print(f"Result: Score {target_score} found at position {position}")
        else:
            print(f"Result: Score {target_score} not found")
        print(f"Comparisons made: {comparisons}")
        
    except ValueError:
        print("Error: Please enter a valid integer for Score.")


def display_search_menu():
    """
    Display the searching algorithms menu.
    """
    print("\n" + "="*80)
    print()
    print("=== Searching Algorithms Menu ===")
    print()
    print("Select a search operation (1-3):")
    print("1. Linear Search - Find Student ID")
    print("2. Binary Search - Find Score")
    print("3. Exit program")
    print()
    print("="*80)
    print()


def main():
    """
    Main function to run the search program.

    Continuously displays the menu and executes selected search operations
    until the user chooses to exit.
    """
    print("(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ Welcome to the Searching Algorithms Program! ✧ﾟ･: *ヽ(◕ヮ◕ヽ)")

    while True:
        display_search_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                linear_search_operation()
            elif choice == 2:
                binary_search_operation()
            elif choice == 3:
                print("Thank you for using the search program! (˘･_･˘)")
                break
            else:
                print("Error: Please enter a valid choice (1-3).")
                continue

            if choice != 3:
                while True:
                    cont_choice = input("Would you like to perform another search? (y/n): ").strip().lower()
                    if cont_choice == "n":
                        print("Thank you for using the search program! (˘･_･˘)")
                        exit()
                    elif cont_choice == "y":
                        break
                    else:
                        print("Error: Please enter 'y' or 'n'.")
                        
        except ValueError:
            print("Error: Please enter a valid integer (1-3).")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting... (╯°□°）╯︵ ┻━┻")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()