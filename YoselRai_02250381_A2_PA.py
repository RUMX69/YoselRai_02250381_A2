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


def get_default_student_ids():
    """
    Return default list of student IDs.
    """
    return [1001, 1005, 1002, 1008, 1003, 1010, 1004, 1009, 
            1007, 1012, 1015, 1018, 1011, 1014, 1017, 1020, 
            1006, 1013, 1016, 1019]


def get_default_scores():
    """
    Return default sorted list of scores.
    """
    return [45, 52, 58, 63, 67, 72, 75, 78, 82, 85, 
            88, 90, 92, 95, 98, 99, 100, 102, 105, 108]


def get_student_ids_from_user():
    """
    Get student IDs from user input.
    
    Returns:
        list: List of student IDs entered by user
    """
    student_ids = []
    try:
        print("\n--- Enter Student IDs for Linear Search ---")
        print("Enter student IDs one by one (enter 'done' when finished):")
        count = 1
        while True:
            id_input = input(f"Enter student ID #{count} (or 'done' to finish): ").strip()
            if id_input.lower() == 'done':
                if len(student_ids) < 2:
                    print("Error: Please enter at least 2 student IDs.")
                    continue
                break
            try:
                student_id = int(id_input)
                student_ids.append(student_id)
                print(f"✓ Added student ID: {student_id}")
                count += 1
            except ValueError:
                print("Error: Please enter a valid integer for student ID.")
    except KeyboardInterrupt:
        print("\nInput interrupted.")
    
    return student_ids


def get_scores_from_user():
    """
    Get test scores from user input and sort them.
    
    Returns:
        list: Sorted list of scores entered by user
    """
    scores = []
    try:
        print("\n--- Enter Test Scores for Binary Search ---")
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
                score = int(score_input)
                scores.append(score)
                print(f"✓ Added test score: {score}")
                count += 1
            except ValueError:
                print("Error: Please enter a valid integer for test score.")
    except KeyboardInterrupt:
        print("\nInput interrupted.")
    
    # Sort the scores for binary search
    scores.sort()
    return scores


def choose_data_source(data_type):
    """
    Let user choose between default data or entering their own data.
    
    Args:
        data_type (str): Type of data ('student_ids' or 'scores')
    
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
                if data_type == 'student_ids':
                    data = get_default_student_ids()
                    print(f"Using default student IDs: {data}")
                    return data
                else:  # scores
                    data = get_default_scores()
                    print(f"Using default scores: {data}")
                    return data
            elif choice == 2:
                if data_type == 'student_ids':
                    return get_student_ids_from_user()
                else:  # scores
                    return get_scores_from_user()
            else:
                print("Error: Please enter 1 or 2.")
        except ValueError:
            print("Error: Please enter a valid integer (1-2).")


def linear_search_operation():
    """
    Execute linear search operation for student IDs.
    
    User chooses between default data or entering their own data.
    """
    print("\n" + "="*60)
    print("LINEAR SEARCH - Find Student ID")
    print("="*60)
    
    student_ids = choose_data_source('student_ids')
    
    if not student_ids:
        print("No student IDs available. Returning to main menu.")
        return
    
    try:
        print(f"\nStudent IDs list: {student_ids}")
        target_id = int(input("Enter Student ID to search for: "))
        position, comparisons = linear_search_student_id(student_ids, target_id)
        
        print("\n" + "-"*40)
        if position != -1:
            print(f"✓ SUCCESS: Student ID {target_id} found at position {position}")
        else:
            print(f"✗ NOT FOUND: Student ID {target_id} not found in the list")
        print(f"Comparisons made: {comparisons}")
        print("-"*40)
        
    except ValueError:
        print("Error: Please enter a valid integer for Student ID.")


def binary_search_operation():
    """
    Execute binary search operation for scores.
    
    User chooses between default data or entering their own data.
    """
    print("\n" + "="*60)
    print("BINARY SEARCH - Find Score")
    print("="*60)
    
    scores = choose_data_source('scores')
    
    if not scores:
        print("No scores available. Returning to main menu.")
        return
    
    try:
        print(f"\nSorted scores list: {scores}")
        target_score = int(input("Enter score to search for: "))
        position, comparisons = binary_search_scores(scores, target_score)
        
        print("\n" + "-"*40)
        if position != -1:
            print(f"✓ SUCCESS: Score {target_score} found at position {position}")
        else:
            print(f"✗ NOT FOUND: Score {target_score} not found in the list")
        print(f"Comparisons made: {comparisons}")
        print("-"*40)
        
    except ValueError:
        print("Error: Please enter a valid integer for Score.")


def display_search_menu():
    """
    Display the searching algorithms menu.
    """
    print("\n" + "="*80)
    print()
    print("=== SEARCHING ALGORITHMS PROGRAM ===")
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
    print("You can choose to use default data or enter your own data for each operation!")

    while True:
        display_search_menu()

        try:
            choice = int(input("Enter your choice (1-3): "))

            if choice == 1:
                linear_search_operation()
            elif choice == 2:
                binary_search_operation()
            elif choice == 3:
                print("\nThank you for using the search program! (˘･_･˘)")
                break
            else:
                print("Error: Please enter a valid choice (1-3).")
                continue

            if choice != 3:
                while True:
                    cont_choice = input("\nWould you like to perform another search? (y/n): ").strip().lower()
                    if cont_choice == "n":
                        print("\nThank you for using the search program! (˘･_･˘)")
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