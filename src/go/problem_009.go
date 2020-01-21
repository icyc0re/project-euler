package main

import (
	"fmt"
)

func isPythagoreanTriplet(a, b, c int) bool {
	return a * a + b * b == c * c
}

func main() {
	target := 1000

	for a := 1; a < target / 3; a++ {
		for b := a + 1; b < target / 2; b++ {
			c := target - a - b
			if isPythagoreanTriplet(a, b, c) {
				fmt.Println(a, b, c)
				fmt.Println(a * b * c)
				return
			}
		}
	}
}
