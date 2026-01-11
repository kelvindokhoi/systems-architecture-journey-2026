# Interfaces in Go

Interfaces in Go allows functions to be more flexible by accepting different types that implement the same methods.
Example:
```go
type shape interface {
  area() float64
  perimeter() float64
}

type rect struct {
    width, height float64
}
func (r rect) area() float64 {
    return r.width * r.height
}
func (r rect) perimeter() float64 {
    return 2*r.width + 2*r.height
}

type circle struct {
    radius float64
}
func (c circle) area() float64 {
    return math.Pi * c.radius * c.radius
}
func (c circle) perimeter() float64 {
    return 2 * math.Pi * c.radius
}
```
Now this function will work with any type that implements the `shape` interface:
```go
func printShapeData(s shape) {
	fmt.Printf("Area: %v - Perimeter: %v\n", s.area(), s.perimeter())
}
```

Every type has the empty interface `interface{}` which can hold values of any type.
Example:
```go
func printValue(v interface{}) {
    fmt.Println(v)
}
```
You can use type assertions to extract the underlying value from an interface.
Example:
```go
func printIfString(v interface{}) {
    str, ok := v.(string)
    if ok {
        fmt.Println("String value:", str)
    } else {
        fmt.Println("Not a string")
    }
}
```