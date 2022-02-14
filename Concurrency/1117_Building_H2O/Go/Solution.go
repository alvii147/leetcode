package main

import (
	"fmt"
	"sync"
)

// function type for passing function to methods
type ReleaseFunc func()

type H2O struct {
	// hydrogen molecule count
	HydrogenCount int
	// oxygen molecule count
	OxygenCount int
	// mutex for r/w synchronization of hydrogen/oxygen counts
	Mtx *sync.Mutex
}

// allocate & initiate channels
func (h2o *H2O) Init() {
	// lock mutex
	h2o.Mtx.Lock()
	// initialize hydrogen count to zero
	h2o.HydrogenCount = 0
	// initialize oxygen count to zero
	h2o.OxygenCount = 0
	// unlock mutex
	h2o.Mtx.Unlock()

	go h2o.Bond()
}

// bond hydrogen & oxygen molecules if possible
func (h2o *H2O) Bond() {
	for {
		h2o.Mtx.Lock()
		if h2o.HydrogenCount == 2 && h2o.OxygenCount == 1 {
			h2o.HydrogenCount = 0
			h2o.OxygenCount = 0
		}
		h2o.Mtx.Unlock()
	}
}

// hydrogen molecule function
func (h2o *H2O) Hydrogen(releaseHydrogen ReleaseFunc) {
	// loop exit condition
	exitLoop := false

	for !exitLoop {
		// lock mutex
		h2o.Mtx.Lock()
		if h2o.HydrogenCount < 2 {
			// increment hydrogen count if space available
			h2o.HydrogenCount++
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
		if h2o.OxygenCount < 1 {
			// increment oxygen count if space available
			h2o.OxygenCount++
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
	input := "OOHHHOHOOHHHHHHHHHOOHHHHHOOOHHOHH"
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
