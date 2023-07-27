# Precompute primes up to a given natural
def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False

    p = 2
    while p**2 <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1

    return [num for num in range(limit + 1) if primes[num]]


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def find_prime_palindrome(value):
    try:
        value = int(value)
    except ValueError:
        print("Only integers! Invalid input!")
        return

    if value < 0:
        print("Only positive numbers are possible! Invalid input!")
        return

    primes = sieve_of_eratosthenes(10**6)  # Generate primes up to a reasonable limit
    num = value + 1

    while True:
        if num > 10**9:
            # If the number is larger than the precomputed primes, use the is_prime function
            if is_palindrome(num) and all(num % p != 0 for p in primes):
                print(num)
                break
        else:
            # If the number is within the precomputed primes, check directly from the list
            if is_palindrome(num) and num in primes:
                print(num)
                break

        num += 1


if __name__ == "__main__":
    user_input = input("Enter a number: ")
    find_prime_palindrome(user_input)
