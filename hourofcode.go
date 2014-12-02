//home/marcus/.gvm/gos/release/bin/go run $0 $@ ; exit
package main

import (
	"flag"
	"fmt"
)

func main() {
	var name = flag.String("name", "world", "who are we saying hello to?")
	flag.StringVar(name, "n", "world", "who are we saying hellow to?")
	flag.Parse()
	fmt.Printf("Hello %s!\n", *name)
}
