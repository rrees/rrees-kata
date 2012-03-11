
def integers_from(n):
	i = n
	while True:
		yield i
		i = i + 1


def remove_factors(prime, integers):
	for i in integers:
		if i % prime:
			yield i

def sieve(n):
	prime = 1
	all_integers = integers_from(prime)

	while prime < n:
		prime = all_integers.next()
		yield prime

		if prime > 1:
			all_integers = remove_factors(prime, all_integers)


