package main

import (
	"fmt"
	"sync"
)

// function type for passing function to methods
type printerFunc func()

// Foo struct
type Foo struct {
	Wg   *sync.WaitGroup
	Mtx1 *sync.Mutex
	Mtx2 *sync.Mutex
}

// init method to lock all mutexes
func (f *Foo) Init() {
	f.Mtx1.Lock()
	f.Mtx2.Lock()
}

func (f *Foo) First(printFirst printerFunc) {
	// signal end of goroutine execution
	defer f.Wg.Done()
	// execute first print function
	printFirst()
	// unlock mutex 1
	f.Mtx1.Unlock()
}

func (f *Foo) Second(printSecond printerFunc) {
	// signal end of goroutine execution
	defer f.Wg.Done()
	// wait until mutex 1 is unlocked, then lock it
	f.Mtx1.Lock()
	// execute second print function
	printSecond()
	// unlock mutex 2
	f.Mtx2.Unlock()
}

func (f *Foo) Third(printThird printerFunc) {
	// signal end of goroutine execution
	defer f.Wg.Done()
	// wait until mutex 2 is unlocked, then lock it
	f.Mtx2.Lock()
	// execute third print function
	printThird()
}

// clean method to unlock all mutexes
func (f *Foo) Clean() {
	f.Mtx1.Unlock()
	f.Mtx2.Unlock()
}

func main() {
	// create wait group
	wg := sync.WaitGroup{}
	// setup wait group for 3 goroutines
	wg.Add(3)
	// create mutexes
	mtx1 := sync.Mutex{}
	mtx2 := sync.Mutex{}

	// create Foo struct
	foo := Foo{
		Wg:   &wg,
		Mtx1: &mtx1,
		Mtx2: &mtx2,
	}

	// initiate mutexes
	foo.Init()

	// call first print function with anonymous print function
	go foo.First(
		func() {
			fmt.Println("first")
		},
	)

	// call second print function with anonymous print function
	go foo.Second(
		func() {
			fmt.Println("second")
		},
	)

	// call third print function with anonymous print function
	go foo.Third(
		func() {
			fmt.Println("third")
		},
	)

	// wait for all goroutines to complete
	wg.Wait()
	// clean up mutexes
	foo.Clean()
}
