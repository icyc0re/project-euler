package main

import "fmt"

func largestPrimeFactor(value int) int {
	if value < 2 {
		return 1
	}

	n := 2
	for value > 1 {
		if value % n == 0 {
			value /= n
		} else {
			n++
		}
	}
	return n
}

func main() {
	fmt.Println(largestPrimeFactor(13195))
	fmt.Println(largestPrimeFactor(600851475143))
}