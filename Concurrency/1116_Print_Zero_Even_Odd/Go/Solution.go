package main

import (
	"fmt"
	"sync"
)

// function type for passing function to methods
type printerFunc func(i int)

type ZeroEvenOdd struct {
	// number of iterations
	n int
	// mutex for printing zeros
	MtxZero *sync.Mutex
	// mutex for printing even numbers
	MtxEven *sync.Mutex
	// mutex for printing odd numbers
	MtxOdd *sync.Mutex
}

// zero printing method
func (zeo *ZeroEvenOdd) Zero(printNumber printerFunc) {
	for i := 0; i < zeo.n; i++ {
		// lock zero mutex
		zeo.MtxZero.Lock()

		// print zero
		printNumber(0)

		if i%2 == 0 {
			// unlock odd mutex if index is even
			zeo.MtxOdd.Unlock()
		} else {
			// unlock even mutex if index is odd
			zeo.MtxEven.Unlock()
		}
	}
}

// even printing method
func (zeo *ZeroEvenOdd) Even(printNumber printerFunc) {
	for i := 2; i < zeo.n; i += 2 {
		// lock even mutex
		zeo.MtxEven.Lock()
		// print index
		printNumber(i)
		// unlock zero mutex
		zeo.MtxZero.Unlock()
	}
}

// odd printing method
func (zeo *ZeroEvenOdd) Odd(printNumber printerFunc) {
	for i := 1; i < zeo.n; i += 2 {
		// lock odd mutex
		zeo.MtxOdd.Lock()
		// print index
		printNumber(i)
		// unlock zero mutex
		zeo.MtxZero.Unlock()
	}
}

func main() {
	// wait group to synchronize goroutines
	wg := sync.WaitGroup{}
	// add 3 wait groups
	wg.Add(3)

	// number of iterations
	n := 12
	// create mutexes
	mtxZero := sync.Mutex{}
	mtxEven := sync.Mutex{}
	mtxOdd := sync.Mutex{}
	// lock even & odd mutexes
	mtxEven.Lock()
	mtxOdd.Lock()

	// printer function
	printNumber := func(i int) {
		fmt.Println(i)
	}

	// create solution object
	zeo := ZeroEvenOdd{
		n:       n,
		MtxZero: &mtxZero,
		MtxEven: &mtxEven,
		MtxOdd:  &mtxOdd,
	}

	// zero printing goroutine
	go func() {
		zeo.Zero(printNumber)
		// signal wait group termination
		wg.Done()
	}()

	// even number printing goroutine
	go func() {
		zeo.Even(printNumber)
		// signal wait group termination
		wg.Done()
	}()

	// odd number printing goroutine
	go func() {
		zeo.Odd(printNumber)
		// signal wait group termination
		wg.Done()
	}()

	// wait for wait groups to terminate
	wg.Wait()
}
