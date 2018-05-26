def is_factor(num):
    if num == 0 or num == 1 or num == 2 or num == 3:
        print("this number is already prime, you blockhead!")
        return True
    elif num > 3:
        index = 2
        count = 0
        while index < num:
            if num % index == 0:
                if is_prime(index):
                    print(index)
                    count += 1
            index += 1
        if count == 0:
            print("this number is already prime, you blockhead!")
            return True
        else:
            print("There are", count, "prime numbers")


def is_prime(num):
    index = 2
    while index < num:
        if num % index == 0:
            return False
        index += 1
    return True


while True:
    user_number = input("Enter a number to find prime factors: ")
    if user_number == "quit":
        break
    else:
        try:
            is_factor(int(user_number))
        except ValueError:
            print("Invalid integer '%s', try again" % (user_number,))
