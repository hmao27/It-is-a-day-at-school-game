# It is a day at school

## How to Play

Keep `game.py`, `events.py`, and `game_helpers.py` in the same folder.
Run `game.py` using Python to start the game.

First, enter your name. Before the school day begins, the game asks you
to enter the names of all four courses you want to take. This only sets
your course schedule. The game does not ask whether you will attend a
course until that part of the day arrives.

Answer yes/no questions with `yes` or `no`. The game accepts uppercase and
lowercase answers, and it ignores extra spaces around the answer. If an
answer is not yes or no, the game asks again.

During the game, you will:
Decide whether to wake up on time.
Decide whether to attend each course when its class time arrives.
Choose whether to review your notes or relax during the break.
There are random events, including a possible alarm problem, a canceled
course, a surprise pop quiz, and one end-of-day event.

To win, you need to attend at least **three courses** and finish with at
least **four points**.

## Game Rules

If the alarm works and you choose to wake up on time, you earn one point
and can try to attend the first course.

If the alarm fails, you wake up late, lose one point, and automatically
miss the first course. You are not asked whether you want to attend it,
and it does not count toward your attendance total.

If the alarm works but you choose to sleep in, you also miss the first
course because you did not get up on time.

For Courses 2, 3, and 4, you decide whether to attend when each course
time arrives. If you attend and the course is not canceled, you earn one
point and the course counts toward your attendance total.

A course you choose to attend can be randomly canceled. A canceled
course does not count toward attendance and does not earn a point.

Both reviewing your notes and relaxing earn one point.But there is
a chance of a surprise pop quiz. If you reviewed your notes,
you earn one extra point. If you relaxed, you lose one point.
At the end of the day, only one of two events happens:
If the basketball club is recruiting, you can choose whether to attend.
Attending gives you one point. Not attending does not change your score.
If it rains, you get soaked and start feeling sick and lose one point.
The basketball recruitment event and the rainy-day event will not happen
at the same time.

The random events make each play different.

## How I Track the Player's State

I use two integer variables, `attended_courses` and `score`, to keep track
of the player's progress.

`attended_courses` starts at zero. It increases by one only when the player
chooses to attend a course and that course is not canceled. If the alarm
fails or the player chooses to sleep in, the first course is missed and
does not increase this variable.

`score` also starts at zero. It changes when the player makes choices or
when a random event happens. I use an integer because the game adds or
subtracts whole points.

Both values are passed to the course functions and returned after they are
updated. At the end, `check_result()` calls `has_enough_courses()` and
`has_enough_points()` to check the two winning conditions. The player wins
only when both conditions are true.

## Program Flow

The game follows this order:

1. Ask for the player's name.
2. Ask for the names of all four courses before the school day starts.
3. Run the random alarm event. If the alarm works, ask whether the player
wants to wake up on time.
4. If the player gets up on time, ask whether they want to attend Course 1.
If the alarm fails or the player sleeps in, Course 1 is missed
automatically.
5. Ask whether the player wants to attend Course 2.
6. Ask whether the player wants to review notes or relax, then run a
possible surprise pop quiz.
7. Ask whether the player wants to attend Course 3 and Course 4.
8. Run one end-of-day event. The basketball recruitment event asks the
player whether to attend; the rainy-day event gives its result directly.
9. Check the number of courses attended and the final score, then show
whether the player wins or loses.

The main flow is shown below:

Start → Enter Name → Enter Four Course Names → School Day Begins → Alarm Event → Wake Up / Miss First Course → Course 1 → Course 2 → Review Notes / Relax → Pop Quiz → Course 3 → Course 4 → Random Event → Check Final Score and Attendance → Win / Lose

Alarm Works → Wake Up → Course 1 Available | Alarm Fails → Miss Course 1
Basketball Club → Choose Yes / No | Rain → Lose 1 Point

The `for` loop in the main function asks for the four course names before
the day begins. The `while` loop in `ask_yes_no()` repeats until the player
enters a valid answer. The `while` loop in `get_course_name()` repeats if
the player leaves a course name blank. `if` statements handle the player's
choices and random events.

## Feedback and Improvements

1. I used `.lower()` and `.strip()` so answers such as `YES`, `Yes`, and
answers with extra spaces are accepted.
2. I added a random alarm failure, a possibility for courses to be canceled,
and a possible pop quiz, so that the game is more interesting and have more possibilities.
3. I also ask the player to choose all four course names before the day begins.
During the game, the player decides whether to attend each course when
its class time arrives.
4. If the alarm fails, the first course is automatically missed. This is more likely to the real life situation.
5. Both reviewing notes and relaxing still earn one point. However, the
pop quiz result depends on whether the player reviewed notes, so the
afternoon choice can affect the final score.
6. I kept the helper functions and random-event functions in separate
files to organize the program.