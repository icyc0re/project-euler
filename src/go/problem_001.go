package main

import "fmt"

func sum_multiples(factors []int, bound int) int {
	sum := 0
	for n := 1; n < bound; n++ {
		for _, f := range factors {
			if n % f == 0 {
				sum += n
				break
			}
		}
	}
	return sum
}

func main() {
	factors := []int{3, 5}
	fmt.Println(sum_multiples(factors, 10))
	fmt.Println(sum_multiples(factors, 1000))
}
