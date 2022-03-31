"""
Task from https://codingbat.com/prob/p190859
We want make a package of goal kilos of chocolate.
We have small bars (1 kilo each) and big bars (5 kilos each).
Return the number of small bars to use, assuming we always use big bars
before small bars. Return -1 if it can't be done.
"""


def make_chocolate(small, big, goal):
    """
    Evaluate how much small bars should be used, assuming we
    always use big bars before small bars. Returns -1 if it can't be done.

    :param small: Amount of small bars given.
    :type small: int
    :param big: Amount of big bars given.
    :type big: int
    :param goal: How much kilos needed.
    :type goal: int
    :return: How much small bars can be used, -1 if impossible.
    :rtype: int
    """
    small, big, goal = (int(x) for x in (small, big, goal))
    if small < 0 or big < 0 or goal < 0:
        raise RuntimeError
    big_mass = big * 5
    small_mass = goal - big_mass if big_mass < goal else goal % 5
    return small_mass if small_mass <= small else -1
