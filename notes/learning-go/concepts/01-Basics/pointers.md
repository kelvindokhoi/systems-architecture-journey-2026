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

### 3. Fields of Pointers
When your function receives a pointer to a struct, you might try to access a field like this and encounter an error:
```go
msgTotal := *analytics.MessagesTotal
```

Instead, access it – like you'd normally do — using a [selector expression](https://go.dev/ref/spec#Selectors).
```go
msgTotal := analytics.MessagesTotal
```

This approach is the recommended, simplest way to access struct fields in Go, and is shorthand for:
```go
(*analytics).MessagesTotal
```

### 3. Pointer Receivers
This is already been mentioned in [functions](..\01-Basics\functions.md#9-receiver-function), but to recap:

When you define methods on struct types, you can choose to use either value receivers or pointer receivers. Pointer receivers allow the method to modify the original struct, while value receivers work on a copy of the struct.