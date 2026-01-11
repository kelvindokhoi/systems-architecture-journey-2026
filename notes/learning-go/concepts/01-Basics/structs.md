# Structs in Go

### 1. Struct in Go
Struct in Go can be represented like this:
```go
type car struct {
	brand      string
	model      string
	doors      int
	mileage    int
}
```

Structs in Go = Class in Python.
In Python:
```python
class Car:
    def __init__(self, brand: str, model: str, doors: int, mileage: int):
        self.brand = brand
        self.model = model
        self.doors = doors
        self.mileage = mileage
```

### 2. Anonymous Struct
If a struct is meant to be used once and then thrown away, you can use an anonymous struct.
```go
myCar := struct {
  brand string
  model string
} {
  brand: "Toyota",
  model: "Camry",
}
```

The equivalent in Python would be using a dictionary:
```python
my_car = {
    "brand": "Toyota",
    "model": "Camry"
}
```

We can nest structs as well.
```go
type owner struct {
    name string
    contact struct {
        email string
        phone string
    }
}
```

### 3. Embedded Structs
Go supports embedding structs within other structs, allowing for composition and reuse of fields and methods.
```go
package main

type User struct {
	Name string
	Membership
}

type Membership struct {
	Type string
	MessageCharLimit int
}

func newUser(name string, membershipType string) User {
	var user User = User{Name: name, Membership: Membership{Type: membershipType, MessageCharLimit:100}}
	if membershipType=="premium"{
		user.Membership.MessageCharLimit = 1000
	}
	return user
}

```
This is similar to inheritance in Python, but Go uses composition instead of classical inheritance.

### 4. Accessing Struct Fields
You can access struct fields using the dot `.` notation.
```go  
myCar := car{name:"Cookie Monster", model:"Model S"}
fmt.Println(myCar.name) // Outputs: Cookie Monster
```

Which is 100% identical to Python.

### 5. Struct Methods
Since Go is not an OOP Language, we need a workaround.
```go
type rect struct {
  width int
  height int
}

// area has a receiver of (r rect)
// rect is the struct
// r is the placeholder
func (r rect) area() int {
  return r.width * r.height
}

var r = rect{
  width: 5,
  height: 10,
}

fmt.Println(r.area())
// prints 50
```

### 6. Memory Layout
Structs in Go are laid out in memory in a way that optimizes for performance. The fields of a struct are stored in the order they are defined, but Go may add padding between fields to ensure proper alignment based on the architecture. This can lead to more efficient access patterns and better cache utilization.

This is efficient:
```go
type stats struct {
	Reach    uint16
	NumPosts uint8
	NumLikes uint8
}
```
But this is not:
```go
type stats struct {
	NumPosts uint8
	Reach    uint16
	NumLikes uint8
}
```
In the second example, Go may add padding after `NumPosts` to align `Reach` properly, which can lead to wasted memory.

To check, we can use the `reflect` package:
```go
typ := reflect.TypeOf(stats{})
fmt.Printf("Struct is %d bytes\n", typ.Size())
```
or `unsafe` package:
```go
fmt.Printf("Struct is %d bytes\n", unsafe.Sizeof(stats{}))
```

This will print the size of the struct in bytes, allowing you to see the impact of field ordering on memory usage.

A common rule of thumb is to order struct fields from largest to smallest data types to minimize padding and optimize memory layout.

### 7. Empty Struct
An empty struct in Go is defined as `struct{}{}`. It takes up NO MEMORY at all. I'm truely amazed by this.