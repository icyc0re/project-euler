package main

import "fmt"

func sumOfSquares(n int) int {
	return n * (n + 1) * (2 * n + 1) / 6
}

func squareOfSum(n int) int {
	v := (n + 1) * n / 2
	return v * v
}

func main() {
	res := squareOfSum(100) - sumOfSquares(100)
	fmt.Println(res)
}
