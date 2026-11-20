import random


def alarm_event():
    """Randomly decide whether the player's alarm works.

    Returns:
        bool: True if the alarm works; False if the alarm fails.

    Side effects:
        Uses a random number to choose the alarm result.
    """
    event = random.randint(1, 4)

    if event == 1:
        return False
    return True


def class_canceled():
    """Randomly decide whether a course is canceled.

    Returns:
        bool: True if the course is canceled; otherwise False.

    Side effects:
        Uses a random number to decide whether the course is canceled.
    """
    event = random.randint(1, 4)

    if event == 1:
        return True
    return False


def pop_quiz(score, reviewed_notes):
    """Run a possible pop quiz and update the player's score.

    Args:
        score (int): The player's current score.
        reviewed_notes (bool): True if the player reviewed notes; otherwise False.

    Returns:
        int: The updated score after the possible pop quiz.

    Side effects:
        Uses a random number and displays the pop quiz result.
    """
    event = random.randint(1, 2)

    if event == 1:
        print("There is a surprise pop quiz!")

        if reviewed_notes:
            print("Your review helps you do well on the quiz.")
            score += 1
        else:
            print("You did not review your notes, so you lose one point.")
            score -= 1
    else:
        print("There is no pop quiz today.")

    return score
