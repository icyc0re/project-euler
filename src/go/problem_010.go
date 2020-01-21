package main

import (
	"fmt"
)

const (
	upper_bound = 2000000
)

var (
	sieve = make([]bool, upper_bound)
)

func prepareSieve() {
	sieve[2] = true
	for i := 3; i < upper_bound; i += 2 {
		sieve[i] = true
	}

	for i := 3; i < upper_bound; i += 2 {
		if sieve[i] {
			for k := i * 2; k < upper_bound; k += i {
				sieve[k] = false
			}
		}
	}
}

func main() {
	prepareSieve()

	// sum primes
	var primeSum int64 = 0
	for i, isPrime := range sieve {
		if isPrime {
			primeSum += int64(i)
		}
	}

	fmt.Println(primeSum)
}