def primes(nb_primes: int):
    if nb_primes > 1000:
        nb_primes = 1000

    p = [0] * 1000

    len_p: int = 0  # The current number of elements in p.
    n: int = 2
    while len_p < nb_primes:
        # Is n prime?
        for i in p[:len_p]:
            if n % i == 0:
                break

        # If no break occurred in the loop, we have a prime.
        else:
            p[len_p] = n
            len_p += 1
        n += 1

    # Let's copy the result into a Python list:
    result_as_list = [prime for prime in p[:len_p]]
    return result_as_list


if __name__ == "__main__":
    primes(1000)
