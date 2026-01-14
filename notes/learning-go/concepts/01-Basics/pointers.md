# Pointers in Go

### 1. What is a Pointer?
Similar to C, Go has pointers, which has the same syntax as C.

```go
var p *int
myString := "hello"      // myString is just a string
myStringPtr := &myString // myStringPtr is a pointer to myString's address

fmt.Printf("value of myStringPtr: %v\n", myStringPtr)
// value of myStringPtr: 0x140c050
```

### 2. Dereferencing a Pointer
The `*` operator is also used to dereference a pointer.
```go
*myStringPtr = "world"                              // set myString through the pointer
fmt.Printf("value of myString: %s\n", *myStringPtr) // read myString through the pointer
// value of myString: world
```
Unlike C, Go don't have pointer aithmetic.

