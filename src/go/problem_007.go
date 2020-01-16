package main

import (
	"fmt"
)

const SIEVE_SIZE = 1000000
var sieve [SIEVE_SIZE]bool

func generatePrimes(ch chan int) {
	// prepare
	sieve[2] = true
	for n := 3; n < SIEVE_SIZE; n+=2 {
		sieve[n] = true
	}
	ch <-2
	for n := 3; n < SIEVE_SIZE; n+=2 {
		if sieve[n] {
			ch <- n
			for k := 2 * n; k < SIEVE_SIZE; k += n {
				sieve[k] = false
			}
		}
	}
	close(ch)
}

func main() {
	primes := make(chan int)

	go generatePrimes(primes)

	for cnt := 0; cnt < 10000; cnt++ {
		_, ok := <-primes
		if !ok {
			fmt.Println("ERROR: channel closed before reaching target value.")
			return
		}
	}
	// next value is the one we are looking for
	fmt.Println(<-primes)
}
