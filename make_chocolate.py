"""
Task from https://codingbat.com/prob/p190859
We want make a package of goal kilos of chocolate.
We have small bars (1 kilo each) and big bars (5 kilos each).
Return the number of small bars to use, assuming we always use big bars
before small bars. Return -1 if it can't be done.
"""


def get_user_input():
    """
    Get user input and validate it.

    :return: list of numbers user input
    :rtype: list
    """
    print(("Please enter amount of small and big bars and the goal. "
           "Enter numbers one by one, confirming them with Enter key. "
           "Press Ctrl + C for exit."))
    try:
        user_input = []
        for _ in range(3):
            value = input()
            user_input.append(validate(value))
    except ValueError:
        print("Please make sure you enter only natural numbers!")
    except RuntimeError:
        print("Negative numbers are unacceptable!")
    else:
        return user_input


def make_chocolate(small, big, goal):
    """
    Evaluate how much small bars should be used, assuming we
    always use big bars before small bars. Returns -1 if it can't be done.

    :param small: Amount of small bars given.
    :type small: int
    :param big: Amount of big bars given.
    :type big: int
    :param goal: How many kilos needed.
    :type goal: int
    :return: How much small bars can be used, -1 if impossible.
    :rtype: int
    """
    big_mass = big * 5
    small_mass = goal - big_mass if big_mass < goal else goal % 5
    return small_mass if small_mass <= small else -1


def validate(user_input):
    """
    Convert user input to int and check if it is not negative.

    :param user_input: raw user input
    :type user_input: str
    :return: validated and converted to int user input
    :rtype: int
    """
    user_input = int(user_input)
    if user_input < 0:
        raise RuntimeError
    return user_input


def main():
    while True:
        user_input = get_user_input()
        if not user_input:
            continue
        amount = make_chocolate(*user_input)
        if amount == -1:
            print("It's impossible!")
        else:
            print(f"You will need {amount} of small bars")


if __name__ == '__main__':
    main()
