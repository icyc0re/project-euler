package main

import (
	"bufio"
	"flag"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	filepath = flag.String("input", "input/problem_011.txt", "file containing the input value")
)

func parseInt(n string) int {
	value, err := strconv.Atoi(n)
	if err != nil {
		panic(err)
	}
	return value
}

// get list of numbers from a line read from the file
func parseNumbers(line string) []int {
	entries := strings.Split(strings.Trim(line, " \n"), " ")
	nums := make([]int, len(entries))
	for i, e := range entries {
		nums[i] = parseInt(e)
	}
	return nums
}

func readInput(filename string) [][]int {
	file, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var lines [][]int
	for scanner := bufio.NewScanner(file); scanner.Scan(); {
		lines = append(lines, parseNumbers(scanner.Text()))
	}
	return lines
}

// find greatest product for a sequence of k values
// expects NxN input
func greatestProduct(values [][]int, k int) int {
	partialMax := 0

	// horizontal
	for i := 0; i < len(values); i++ {
		for j := 0; j < len(values[i]) - k; j++ {
			partialProduct := 1
			for offset := 0; offset < k; offset++ {
				partialProduct *= values[i][j + offset]
			}
			if partialProduct > partialMax {
				partialMax = partialProduct
			}
		}
	}

	// vertical
	for i := 0; i < len(values) - k; i++ {
		for j := 0; j < len(values[i]); j++ {
			partialProduct := 1
			for offset := 0; offset < k; offset++ {
				partialProduct *= values[i + offset][j]
			}
			if partialProduct > partialMax {
				partialMax = partialProduct
			}
		}
	}

	// diagonal 1
	for i := 0; i < len(values) - k; i++ {
		for j := 0; j < len(values[i]) - k; j++ {
			partialProduct := 1
			for offset := 0; offset < k; offset++ {
				partialProduct *= values[i + offset][j + offset]
			}
			if partialProduct > partialMax {
				partialMax = partialProduct
			}
		}
	}

	// diagonal 2
	for i := 0; i < len(values) - k; i++ {
		for j := 0; j < len(values[i]) - k; j++ {
			partialProduct := 1
			for offset := 0; offset < k; offset++ {
				partialProduct *= values[i + offset][j + k - offset]
			}
			if partialProduct > partialMax {
				partialMax = partialProduct
			}
		}
	}

	return partialMax
}

func main() {
	flag.Parse()

	inputValues := readInput(*filepath)

	fmt.Println(greatestProduct(inputValues, 4))
}
