# rileywestonmiller@outlook.com
# practical programming, third edition by Gries, Campbell & Montojo
# expert python programming - second edition


def is_even(num):
    return num % 2 == 0


def collatz(num):
    count = 0
    while num != 1:
        count = 1 + count
        if is_even(num):
            num = num/2
        else:
            num = num * 3 + 1
    return count


def collatz_count(numbers_to_run):
    previous_count = 0
    counter = 0
    while counter < numbers_to_run:
        counter += 1
        counted = collatz(counter)
        if counted > previous_count:
            previous_count = counted
            winning_number = counter
            print(previous_count, winning_number)
    print(previous_count, winning_number)


collatz_count(35000)
