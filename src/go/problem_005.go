package main

import (
	"fmt"
	"math"
)

func getFactors(n int) map[int]int {
	m := make(map[int]int)
	i := 2
	for n > 1 {
		if n % i == 0 {
			n /= i
			m[i]++
		} else {
			i++
		}
	}
	return m
}

// return least common multiple of all values from 1 to bound
func Lcm(bound int) int {
	factors := make(map[int]int)
	for i := 2; i <= bound; i++ {
		for k,v := range getFactors(i) {
			if v > factors[k] {
				factors[k] = v
			}
		}
	}
	prod := 1.0
	for k, v := range factors {
		prod *= math.Pow(float64(k), float64(v))
	}
	return int(prod)
}

func main() {
	fmt.Println(Lcm(10))
	fmt.Println(Lcm(20))
}
