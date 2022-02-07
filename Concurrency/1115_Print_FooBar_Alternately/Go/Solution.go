package main

import (
	"fmt"
	"sync"
)

// function type for passing function to methods
type printerFunc func()

type FooBar struct {
	// number of iterations
	N int
	// pointer to waitgroup for synchronization with main thread
	Wg *sync.WaitGroup
	// pointer to mutex 1
	Mtx1 *sync.Mutex
	// pointer to mutex 2
	Mtx2 *sync.Mutex
}

// init method
func (fb *FooBar) Init() {
	// lock mutex 2
	fb.Mtx2.Lock()
}

func (fb *FooBar) Foo(printFoo printerFunc) {
	// signal waitgroup done once function execution completes
	defer fb.Wg.Done()
	for i := 0; i < fb.N; i++ {
		// lock mutex 1
		fb.Mtx1.Lock()
		printFoo()
		// unlock mutex 2
		fb.Mtx2.Unlock()
	}
}

func (fb *FooBar) Bar(printBar printerFunc) {
	// signal waitgroup done once function execution completes
	defer fb.Wg.Done()
	for i := 0; i < fb.N; i++ {
		// lock mutex 2
		fb.Mtx2.Lock()
		printBar()
		// unlock mutex 1
		fb.Mtx1.Unlock()
	}
}

func main() {
	// number of iterations
	n := 5
	// create waitgroup
	wg := sync.WaitGroup{}
	// add 2 goroutines to waitgroup
	wg.Add(2)
	// create mutexes
	mtx1 := sync.Mutex{}
	mtx2 := sync.Mutex{}

	// create FooBar struct
	foobar := FooBar{
		N:    n,
		Wg:   &wg,
		Mtx1: &mtx1,
		Mtx2: &mtx2,
	}
	// initiate mutexes
	foobar.Init()

	// run Foo function as a goroutine
	go foobar.Foo(
		func() {
			fmt.Print("foo")
		},
	)

	// run Bar function as a goroutines
	go foobar.Bar(
		func() {
			fmt.Print("bar")
		},
	)

	// wait for goroutines to return
	wg.Wait()
}
