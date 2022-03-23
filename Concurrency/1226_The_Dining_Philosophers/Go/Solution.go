package main

import (
	"fmt"
	"sync"
)

// function type for passing function to methods
type PrinterFunc func()

type DiningPhilosophers struct {
	// number of philosophers
	NumOfPhilosophers int
	// mutex locks
	Forks []sync.Mutex
}

// initialize Dining Philosophers solution struct
func (dp *DiningPhilosophers) Init(numOfPhilosophers int) {
	// set up number of philosophers
	dp.NumOfPhilosophers = numOfPhilosophers
	// initialize mutex locks
	dp.Forks = make([]sync.Mutex, dp.NumOfPhilosophers)
}

// instruct philosopher to eat
func (dp *DiningPhilosophers) WantsToEat(
	philosopher int,
	pickLeftFork PrinterFunc,
	pickRightFork PrinterFunc,
	eat PrinterFunc,
	putLeftFork PrinterFunc,
	putRightFork PrinterFunc) {

	// left and right forks
	leftForkIdx := (philosopher + 1) % dp.NumOfPhilosophers
	rightForkIdx := philosopher

	// divide order of fork locking to prevent deadlocks
	if philosopher%2 == 0 {
		// lock left fork and pick it up
		dp.Forks[leftForkIdx].Lock()
		pickLeftFork()
		// lock right fork and pick it up
		dp.Forks[rightForkIdx].Lock()
		pickRightFork()
	} else {
		// lock right fork and pick it up
		dp.Forks[rightForkIdx].Lock()
		pickRightFork()
		// lock left fork and pick it up
		dp.Forks[leftForkIdx].Lock()
		pickLeftFork()
	}

	// eat spaghetti
	eat()

	// unlock left fork and put it down
	putLeftFork()
	dp.Forks[leftForkIdx].Unlock()
	// unlock right fork and put it down
	putRightFork()
	dp.Forks[rightForkIdx].Unlock()
}

func main() {
	// number of times each philosopher wants to eat
	n := 5
	// number of philosophers
	numOfPhilosophers := 5
	// wait group for goroutine synchronization
	wg := sync.WaitGroup{}
	// add number of times wantsToEat() will be called to wait group
	wg.Add(n * numOfPhilosophers)

	// create and initialize Dining Philosophers solution struct
	dp := DiningPhilosophers{}
	dp.Init(numOfPhilosophers)

	for i := 0; i < n; i++ {
		for id := 0; id < numOfPhilosophers; id++ {
			// go routine for philosopher to eat
			go func(philosopher int) {
				dp.WantsToEat(
					philosopher,
					func() { fmt.Println(philosopher, 1, 1) },
					func() { fmt.Println(philosopher, 2, 1) },
					func() { fmt.Println(philosopher, 0, 3) },
					func() { fmt.Println(philosopher, 1, 2) },
					func() { fmt.Println(philosopher, 2, 2) },
				)
				// signal wait group termination
				wg.Done()
			}(id)
		}
	}

	// wait for all waitgroups to be done
	wg.Wait()
}
