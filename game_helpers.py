def ask_yes_no(question):
    """Ask a yes/no question and return a valid answer.

    Args:
        question (str): The question shown to the player.

    Returns:
        str: The answer, either "yes" or "no", in lowercase.

    Side effects:
        Prompts the player and displays a reminder for an invalid answer.
    """
    answer = input(question + " (yes/no): ").strip().lower()

    while answer != "yes" and answer != "no":
        print("Please enter yes or no.")
        answer = input(question + " (yes/no): ").strip().lower()

    return answer


def get_course_name(course_number):
    """Ask the player for the name of one course.

    Args:
        course_number (int): The number of the course in the game.

    Returns:
        str: The name entered by the player.

    Side effects:
        Prompts the player and repeats if the course name is blank.
    """
    course_name = input(
        "What course would you like to take for Course " + str(course_number) + "? "
    ).strip()

    while course_name == "":
        print("Please enter a course name.")
        course_name = input(
            "What course would you like to take for Course " + str(course_number) + "? "
        ).strip()

    return course_name
