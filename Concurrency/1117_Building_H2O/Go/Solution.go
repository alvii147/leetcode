package main

import (
	"fmt"
	"sync"
)

// function type for passing function to methods
type ReleaseFunc func()

type H2O struct {
	// hydrogen molecule count
	H2Count int
	// mutex for r/w synchronization of hydrogen molecule count
	Mtx *sync.Mutex
}

// allocate & initiate channels
func (h2o *H2O) Init() {
	// lock mutex
	h2o.Mtx.Lock()
	// initialize hydrogen count to zero
	h2o.H2Count = 0
	// unlock mutex
	h2o.Mtx.Unlock()
}

// hydrogen molecule function
func (h2o *H2O) Hydrogen(releaseHydrogen ReleaseFunc) {
	// loop exit condition
	exitLoop := false

	for !exitLoop {
		// lock mutex
		h2o.Mtx.Lock()
		if h2o.H2Count < 2 {
			// increment hydrogen count if space available
			h2o.H2Count++
			// release hydrogen molecule
			releaseHydrogen()
			// exit loop
			exitLoop = true
		}
		// unlock mutex
		h2o.Mtx.Unlock()
	}
}

// oxygen molecule function
func (h2o *H2O) Oxygen(releaseOxygen ReleaseFunc) {
	// loop exit condition
	exitLoop := false

	for !exitLoop {
		// lock mutex
		h2o.Mtx.Lock()
		if h2o.H2Count >= 2 {
			// reset hydrogen count if water can be formed
			h2o.H2Count = 0
			// release oxygen molecule
			releaseOxygen()
			// exit loop
			exitLoop = true
		}
		// unlock mutex
		h2o.Mtx.Unlock()
	}
}

func main() {
	// input test string
	input := "OOOOHHHHHHHH"
	// mutex for r/w synchronization of hydrogen molecule count
	mtx := sync.Mutex{}
	// create wait group for goroutine synchronization
	wg := sync.WaitGroup{}
	// add one wait group for each letter
	wg.Add(len(input))

	// create & initiate H2O object
	h2o := H2O{
		Mtx: &mtx,
	}
	h2o.Init()

	// printer function for releasing hydrogen
	releaseH := func() {
		fmt.Print("H")
	}
	// printer function for releasing oxygen
	releaseO := func() {
		fmt.Print("O")
	}

	var char string
	for _, c := range input {
		// convert rune to character string
		char = fmt.Sprintf("%c", c)
		if char == "H" {
			// hydrogen goroutine
			go func() {
				h2o.Hydrogen(releaseH)
				// signal wait group termination
				wg.Done()
			}()
		} else if char == "O" {
			// oxygen goroutine
			go func() {
				h2o.Oxygen(releaseO)
				// signal wait group termination
				wg.Done()
			}()
		} else {
			panic("Invalid character found, `input` must consist of 'H' or 'O' characters")
		}
	}

	// wait for all waitgroups to be done
	wg.Wait()
	fmt.Print("\n")
}
