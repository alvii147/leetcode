package main

import (
	"fmt"
	"sync"
)

// function type for passing function to methods
type printerFunc func()

// Foo struct with mutexes
type Foo struct {
	mtx1 *sync.Mutex
	mtx2 *sync.Mutex
}

// init method to lock all mutexes
func (foo *Foo) Init() {
	foo.mtx1.Lock()
	foo.mtx2.Lock()
}

func (foo *Foo) First(printFirst printerFunc) {
	// execute first print function
	printFirst()
	// unlock mutex 1
	foo.mtx1.Unlock()
}

func (foo *Foo) Second(printSecond printerFunc) {
	// wait until mutex 1 is unlocked, then lock it
	foo.mtx1.Lock()
	// execute second print function
	printSecond()
	// unlock mutex 2
	foo.mtx2.Unlock()
}

func (foo *Foo) Third(printThird printerFunc) {
	// wait until mutex 2 is unlocked, then lock it
	foo.mtx2.Lock()
	// execute third print function
	printThird()
}

// clean method to unlock all mutexes
func (foo *Foo) Clean() {
	foo.mtx1.Unlock()
	foo.mtx2.Unlock()
}

func main() {
	// create mutexes
	mtx1 := sync.Mutex{}
	mtx2 := sync.Mutex{}

	// create Foo struct
	foo := Foo{
		mtx1: &mtx1,
		mtx2: &mtx2,
	}

	// create wait group
	wg := sync.WaitGroup{}
	// setup wait group for 3 goroutines
	wg.Add(3)

	// initiate mutexes
	foo.Init()

	// call first print function with anonymous print function
	go foo.First(
		func() {
			fmt.Println("first")
			// signal end of goroutine execution
			defer wg.Done()
		},
	)

	// call second print function with anonymous print function
	go foo.Second(
		func() {
			fmt.Println("second")
			// signal end of goroutine execution
			defer wg.Done()
		},
	)

	// call third print function with anonymous print function
	go foo.Third(
		func() {
			fmt.Println("third")
			// signal end of goroutine execution
			defer wg.Done()
		},
	)

	// wait for all goroutines to complete
	wg.Wait()
	// clean up mutexes
	foo.Clean()
}
