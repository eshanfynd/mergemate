def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True




def find_maximum(lst):
    return max(lst) if lst else None
        


def bubble_sort(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
