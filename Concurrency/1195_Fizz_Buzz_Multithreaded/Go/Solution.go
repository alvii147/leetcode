package main

import (
	"fmt"
	"sync"
)

// function type for passing function to methods
type PrinterFunc func()

// function type with int arg for passing function to methods
type NumberPrinterFunc func(n int)

// FizzBuzzSolution struct
type FizzBuzzSolution struct {
	// range of tokens
	n int
	// fizz channel
	fizzCh chan struct{}
	// buzz channel
	buzzCh chan struct{}
	// fizzbuzz channel
	fizzbuzzCh chan struct{}
}

// fizz function
func (fb *FizzBuzzSolution) Fizz(printFizz PrinterFunc) {
	// keep reading fizz channel until it's closed
	for range fb.fizzCh {
		// print fizz
		printFizz()
		// signal done by inserting to fizz channel
		fb.fizzCh <- struct{}{}
	}
}

// buzz function
func (fb *FizzBuzzSolution) Buzz(printBuzz PrinterFunc) {
	// keep reading buzz channel until it's closed
	for range fb.buzzCh {
		// print buzz
		printBuzz()
		// signal done by inserting into buzz channel
		fb.buzzCh <- struct{}{}
	}
}

// fizzbuzz function
func (fb *FizzBuzzSolution) FizzBuzz(printFizzBuzz PrinterFunc) {
	// keep reading fizzbuzz channel until it's closed
	for range fb.fizzbuzzCh {
		// print fizzbuzz
		printFizzBuzz()
		// signal done by inserting into fizzbuzz channel
		fb.fizzbuzzCh <- struct{}{}
	}
}

// number function
func (fb *FizzBuzzSolution) Number(printNumber NumberPrinterFunc) {
	// iterate over token range
	for i := 1; i <= fb.n; i++ {
		// check if i is divisible by 3
		divisibleBy3 := i%3 == 0
		// check if i is divisible by 5
		divisibleBy5 := i%5 == 0
		if divisibleBy3 && divisibleBy5 {
			// insert into fizzbuzz channel to initiate printing fizzbuzz
			fb.fizzbuzzCh <- struct{}{}
			// wait for fizzbuzz function to signal done
			<-fb.fizzbuzzCh
		} else if divisibleBy3 {
			// insert into fizz channel to initiate printing fizz
			fb.fizzCh <- struct{}{}
			// wait for fizz function to signal done
			<-fb.fizzCh
		} else if divisibleBy5 {
			// insert into buzz channel to initiate printing buzz
			fb.buzzCh <- struct{}{}
			// wait for buzz function to signal done
			<-fb.buzzCh
		} else {
			// print number if divisible by neither 3 nor 5
			printNumber(i)
		}
	}

	// close fizz channel
	close(fb.fizzCh)
	// close buzz channel
	close(fb.buzzCh)
	// close fizzbuzz channel
	close(fb.fizzbuzzCh)
}

func main() {
	// create wait group for goroutine synchronization
	wg := sync.WaitGroup{}
	// add 4 wait groups for the 4 methods
	wg.Add(4)

	// token range
	n := 15
	// create FizzBuzzSolution with token range and channels
	fb := FizzBuzzSolution{
		n:          n,
		fizzCh:     make(chan struct{}),
		buzzCh:     make(chan struct{}),
		fizzbuzzCh: make(chan struct{}),
	}

	// fizz printer function
	printFizz := func() {
		fmt.Println("fizz")
	}
	// buzz printer function
	printBuzz := func() {
		fmt.Println("buzz")
	}
	// fizzbuzz printer function
	printFizzBuzz := func() {
		fmt.Println("fizzbuzz")
	}
	// number printer function
	printNumber := func(n int) {
		fmt.Println(n)
	}

	// fizz goroutine
	go func() {
		fb.Fizz(printFizz)
		// signal wait group done
		wg.Done()
	}()
	// buzz goroutine
	go func() {
		fb.Buzz(printBuzz)
		// signal wait group done
		wg.Done()
	}()
	// fizzbuzz goroutine
	go func() {
		fb.FizzBuzz(printFizzBuzz)
		// signal wait group done
		wg.Done()
	}()
	// number goroutine
	go func() {
		fb.Number(printNumber)
		// signal wait group done
		wg.Done()
	}()

	// wait for wait groups to be done
	wg.Wait()
}
