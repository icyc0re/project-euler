package main

import "fmt"

func fibonacci(high_bound int, ch chan int) {
	a, b := 1, 1
	// less than value, and check for int not to overflow
	for b < high_bound && a+b > b {
		ch <- b
		a, b = b, a+b
	}
	close(ch)
}

func countEvenFibo(high_bound int) int {
	ch := make(chan int)
	go fibonacci(high_bound, ch)

	sum := 0
	for val := range(ch) {
		if val % 2 == 0 {
			sum += val
		}
	}
	return sum
}

func main() {
	fmt.Println(countEvenFibo(4000000))
}
