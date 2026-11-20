import random

from events import alarm_event, class_canceled, pop_quiz
from game_helpers import ask_yes_no, get_course_name


def wake_up_choice(score, name):
    """Handle the alarm and decide whether the player can attend the first course.

    Args:
        score (int): The player's current score.
        name (str): The player's name.

    Returns:
        tuple: The updated score (int) and whether the player can attend
        the first course (bool).

    Side effects:
        Displays the alarm event and may ask the player a yes/no question.
    """
    print("Morning: You are getting ready for the day.")

    can_attend_first_course = False

    if alarm_event():
        print("Your alarm goes off.")
        if ask_yes_no(name + ", do you want to wake up on time?") == "yes":
            score += 1
            can_attend_first_course = True
            print(name + ", you wake up on time!")
        else:
            print(name + ", you decide to sleep in.")
    else:
        print(name + ", your alarm fails to go off. You wake up late.")
        score -= 1

    return score, can_attend_first_course


def course_1(attended_courses, score, course_name, can_attend):
    """Ask whether the player attends the first course if they got up in time.

    Args:
        attended_courses (int): The number of courses attended so far.
        score (int): The player's current score.
        course_name (str): The first course name entered before the day starts.
        can_attend (bool): True if the player got up in time; otherwise False.

    Returns:
        tuple: The updated course count and score, both integers.

    Side effects:
        Asks whether the player will attend and displays the course outcome.
        If the player got up late, the first course is missed automatically.
    """
    if can_attend:
        if ask_yes_no("Do you want to attend " + course_name + "?") == "yes":
            # A canceled course does not count toward attendance or score.
            if class_canceled():
                print("Your " + course_name + " class is canceled today.")
            else:
                attended_courses += 1
                score += 1
                print("You attended " + course_name + ".")
        else:
            print("You decided to skip " + course_name + ".")
    else:
        print("You missed " + course_name + " because you did not get up on time.")

    return attended_courses, score


def course_2(attended_courses, score, course_name):
    """Ask whether the player attends the second course.

    Args:
        attended_courses (int): The number of courses attended so far.
        score (int): The player's current score.
        course_name (str): The course name entered before the day starts.

    Returns:
        tuple: The updated course count and score, both integers.

    Side effects:
        Asks whether the player will attend and displays the course outcome.
    """
    if ask_yes_no("Do you want to attend " + course_name + "?") == "yes":
        # A canceled course does not count toward attendance or score.
        if class_canceled():
            print("Your " + course_name + " class is canceled today.")
        else:
            attended_courses += 1
            score += 1
            print("You attended " + course_name + ".")
    else:
        print("You decided to skip " + course_name + ".")

    return attended_courses, score


def afternoon_choice(score):
    """Ask the player to review notes or relax, then run a pop quiz.

    Args:
        score (int): The player's current score.

    Returns:
        int: The updated score after the choice and possible pop quiz.

    Side effects:
        Asks the player to choose and displays the pop quiz result.
    """
    print("Afternoon: You have a break.")
    reviewed_notes = ask_yes_no("Do you want to review your notes?") == "yes"

    if reviewed_notes:
        print("You review your notes and feel prepared.")
    else:
        print("You decide to relax.")

    # Both choices earn one point, but the pop quiz depends on the choice.
    score += 1
    score = pop_quiz(score, reviewed_notes)

    return score


def course_3(attended_courses, score, course_name):
    """Ask whether the player attends the third course.

    Args:
        attended_courses (int): The number of courses attended so far.
        score (int): The player's current score.
        course_name (str): The course name entered before the day starts.

    Returns:
        tuple: The updated course count and score, both integers.

    Side effects:
        Asks whether the player will attend and displays the course outcome.
    """
    if ask_yes_no("Do you want to attend " + course_name + "?") == "yes":
        # A canceled course does not count toward attendance or score.
        if class_canceled():
            print("Your " + course_name + " class is canceled today.")
        else:
            attended_courses += 1
            score += 1
            print("You attended " + course_name + ".")
    else:
        print("You decided to skip " + course_name + ".")

    return attended_courses, score


def course_4(attended_courses, score, course_name):
    """Ask whether the player attends the fourth course.

    Args:
        attended_courses (int): The number of courses attended so far.
        score (int): The player's current score.
        course_name (str): The course name entered before the day starts.

    Returns:
        tuple: The updated course count and score, both integers.

    Side effects:
        Asks whether the player will attend and displays the course outcome.
    """
    if ask_yes_no("Do you want to attend " + course_name + "?") == "yes":
        # A canceled course does not count toward attendance or score.
        if class_canceled():
            print("Your " + course_name + " class is canceled today.")
        else:
            attended_courses += 1
            score += 1
            print("You attended " + course_name + ".")
    else:
        print("You decided to skip " + course_name + ".")

    return attended_courses, score


def random_event(score):
    """Run the original end-of-day event and update the score.

    Args:
        score (int): The player's current score.

    Returns:
        int: The updated score after the random event.

    Side effects:
        Displays one of the possible end-of-day events.
    """
    print("An unexpected event happens!")
    event = random.randint(1, 2)

    if event == 1:
        print("The basketball club is holding a recruitment event.")
        if ask_yes_no("Do you want to attend the basketball club recruitment event?") == "yes":
            print("You attend the event and make new friends!")
            score += 1
        else:
            print("You decide not to attend the recruitment event.")
    else:
        print("It starts raining. You get soaked and start feeling sick.")
        score -= 1

    return score


def has_enough_courses(attended_courses):
    """Check whether the player attended at least three courses.

    Args:
        attended_courses (int): The number of courses attended.

    Returns:
        bool: True if at least three courses were attended; otherwise False.
    """
    return attended_courses >= 3


def has_enough_points(score):
    """Check whether the player earned at least four points.

    Args:
        score (int): The player's final score.

    Returns:
        bool: True if the score is at least four; otherwise False.
    """
    return score >= 4


def check_result(attended_courses, score):
    """Determine whether the player wins by checking both parts of the goal.

    Args:
        attended_courses (int): The number of courses attended.
        score (int): The player's final score.

    Returns:
        bool: True if both winning conditions are met; otherwise False.

    Side effects:
        Calls the two helper functions that check the winning conditions.
    """
    if has_enough_courses(attended_courses) and has_enough_points(score):
        return True
    return False


def __main__():
    """Run the school-day game from start to finish.

    The function asks for the player's name and course names, runs each
    part of the day, and prints the final result. It does not return a value.

    Side effects:
        Gets input from the player and prints the progress and final result.
    """
    attended_courses = 0
    score = 0

    name = input("What is your name? ").strip()

    # Choose all four courses before the school day begins.
    course_names = []
    for course_number in range(1, 5):
        course_names.append(get_course_name(course_number))

    print("Welcome, " + name + "! Your school day is starting.")
    print("Attend at least 3 courses and earn at least 4 points to win.")

    score, can_attend_first_course = wake_up_choice(score, name)

    attended_courses, score = course_1(
        attended_courses, score, course_names[0], can_attend_first_course
    )
    attended_courses, score = course_2(attended_courses, score, course_names[1])

    score = afternoon_choice(score)

    attended_courses, score = course_3(attended_courses, score, course_names[2])
    attended_courses, score = course_4(attended_courses, score, course_names[3])

    score = random_event(score)

    print("The day is over, " + name + "!")
    print("Courses attended:", attended_courses)
    print("Points:", score)

    if check_result(attended_courses, score):
        print("You win! You had a successful school day.")
    else:
        print("You lose. Try working harder and getting luckier next time.")


if __name__ == "__main__":
    __main__()
