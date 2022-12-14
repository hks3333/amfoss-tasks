package main

import (
	"syscall/js"
)

func add(this js.Value, i []js.Value) any {
	s := js.ValueOf(i[0].Int() + 1)
	js.Global().Get("document").Call("getElementById", "int").Set("innerHTML", s)
	return nil
}

func subtract(this js.Value, i []js.Value) any {
	s := js.ValueOf(i[0].Int() - 1)
	js.Global().Get("document").Call("getElementById", "int").Set("innerHTML", s)
	return nil
}

func main() {
	c := make(chan struct{}, 0)

	println("WASM Go Initialized")
	js.Global().Set("add", js.FuncOf(add))
	js.Global().Set("subtract", js.FuncOf(subtract))
	<-c
}
