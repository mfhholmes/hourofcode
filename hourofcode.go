//home/marcus/.gvm/gos/release/bin/go run $0 $@ ; exit
// you'll need to replace the above path with your $GOROOT path
package main

import (
	"flag"
	"fmt"
)

func main() {
	name := flag.String("name", "world", "who are we saying hello to?")
	flag.StringVar(name, "n", "world", "who are we saying hello to?")
	flag.Parse()
	fmt.Printf("Hello %s!\n", *name)
}
