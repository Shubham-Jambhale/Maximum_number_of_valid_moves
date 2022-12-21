# Maximum_number_of_valid_moves

# Question

You are given a list of 3 positive integers. You are allowed to make a decrement to any two of
the three (non zero) integers in a single move. Your objective is to find the maximum number
of moves you can play before you run out of valid moves (i.e there are less than two non-zero
integers left).

# Example 1

input = [2,4,6]

output: 6

Explanation:

1st move: decrement 1st and the 3rd integer: list = (1, 4, 5)

2nd move: decrement 1st and the 3rd integer: list = (0, 4, 4)

3rd move: decrement 2nd and the 3rd integer: list = (0, 3, 3)

4th move: decrement 2nd and the 3rd integer: list = (0, 2, 2)

5th move: decrement 2nd and the 3rd integer: list = (0, 1, 1)

6th move: decrement 2nd and the 3rd integer: list = (0, 0, 0)


# Example 2

input = [4,4,6]

output: 7

Explanation:

1st move: decrement 1st and the 2nd integer: list = (3, 3, 6)

2nd move: decrement 1st and the 3rd integer: list = (2, 3, 5)

3rd move: decrement 2st and the 3rd integer: list = (1, 3, 4)

4th move: decrement 2nd and the 3rd integer: list = (0, 3, 3)

5th move: decrement 2nd and the 3rd integer: list = (0, 2, 2)

6th move: decrement 2nd and the 3rd integer: list = (0, 1, 1)

7th move: decrement 2nd and the 3rd integer: list = (0, 0, 0)
