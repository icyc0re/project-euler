package main

import (
	"fmt"
)

func isPalindrom(n int) bool {
	reverse := 0
	for tmp := n; tmp > 0; tmp /= 10 {
		remainder := tmp % 10
		reverse = reverse * 10 + remainder
	}
	return n == reverse
}

func main() {
	highest := 0
	for a := 100; a < 1000; a++ {
		for b := a; b < 1000; b++ {
			v := a * b
			if isPalindrom(v) && v > highest {
				highest = v
			}
		}
	}
	fmt.Println(highest)
}
