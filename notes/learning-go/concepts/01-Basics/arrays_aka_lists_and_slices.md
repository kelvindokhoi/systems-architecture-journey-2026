# Arrays in Go


### 1. Fixed-Size Arrays
Go does not support dynamic arrays like Python lists (😢). Instead, Go has fixed-size arrays and dynamic slices.

It goes like this:
```go
var arr [number_of_elements]element_type
list := [number_of_elements]element_type{element1, element2, element3,...}
list[index] = new_value
``` 

Arrays are fixed in size, so once we made `[67]int`, we can't add the 68th element later.
Zero value of an array is an array with all elements set to the zero value of the element type.

### 2. Slices in Go
Slices are more flexible than arrays. They are dynamically-sized, and you can append elements to them.
Zero value of a slice is `nil`.
Non-nil slices ALWAYS have an underlying array, though it isn't always specified explicitly.
To explicitly creat a slice on top of an array:
```go
primes := [6]int{2, 3, 5, 7, 11, 13}
mySlice := primes[1:4]
// mySlice = {3, 5, 7}
ages := []int{}
```
The general syntax is:
```go
arrayname[lowIndex:highIndex]
arrayname[lowIndex:]
arrayname[:highIndex]
arrayname[:]
```
Where `lowIndex` is inclusive and `highIndex` is exclusive (just like Python, and can be omitted, omitting both will give you the entire array).

Slices hold references to an underlying array, and if you assign one slice to another, both refer to the same array. If a function takes a slice argument, any changes it makes to the elements of the slice will be visible to the caller, analogous to passing a [pointer](https://en.wikipedia.org/wiki/Pointer_%28computer_programming%29) (we'll cover pointers later) to the underlying array. A Read function can therefore accept a slice argument rather than a pointer and a count; the length within the slice sets an upper limit of how much data to read. Here is the signature of the [Read()](https://pkg.go.dev/os#File.Read) method of the `File` type in package `os`:

Referenced from [Effective Go](https://golang.org/doc/effective_go.html#slices)
```go
func (f *File) Read(buf []byte) (n int, err error)
```

### 3. Create Slices with `make`
You can create slices using the built-in `make` function.
```go
// func make([]T, len, cap) []T
mySlice := make([]int, 5, 10)

// the capacity argument is usually omitted and defaults to the length
mySlice := make([]int, 5)
```
If we want to create a slice with a specific set of values, we can use a slice literal:
```go
mySlice := []string{"I", "love", "go"}
```

The length of a slice can be obtained using the built-in `len` function. It is simply the number of elements in the slice.
The capacity of a slice can be obtained using the built-in `cap` function.

Generally speaking, unless you're hyper-optimizing the memory usage of your program, you don't need to worry about the capacity of a slice because it will automatically grow as needed.

Indexing:
```go
mySlice := []string{"I", "love", "go"}
fmt.Println(mySlice[2]) // go

mySlice[0] = "you"
fmt.Println(mySlice) // [you love go]
```

### 4. Variadic Functions
Many functions, especially those in the standard library, can take an arbitrary number of final arguments. This is accomplished by using the "..." syntax in the function signature.

A variadic function receives the variadic arguments as a slice.
```go
func concat(strs ...string) string {
    final := ""
    // strs is just a slice of strings
    for i := 0; i < len(strs); i++ {
        final += strs[i]
    }
    return final
}

func main() {
    final := concat("Hello ", "there ", "friend!")
    fmt.Println(final)
    // Output: Hello there friend!
}
```

This is the signature of the Println function. It is, like many others, variadic.
```go
func Println(a ...interface{}) (n int, err error)
```

### 5. Spread Operator
The spread operator allows us to pass a slice into a variadic function. The spread operator consists of three dots following the slice in the function call.
Example:
```go
func printStrings(strings ...string) {
	for i := 0; i < len(strings); i++ {
		fmt.Println(strings[i])
	}
}

func main() {
    names := []string{"bob", "sue", "alice"}
    printStrings(names...)
}
```

### 6. Append to Slices
You can append elements to a slice using the built-in `append` function.
```go
slice = append(slice, oneThing)
slice = append(slice, firstThing, secondThing)
slice = append(slice, anotherSlice...)
```

### 7. Range
Go provides a syntactic sugar to iterate easily over elements of a slice.
```go
for INDEX, ELEMENT := range SLICE {
}
```
For example:
```go
fruits := []string{"apple", "banana", "grape"}
for i, fruit := range fruits {
    fmt.Println(i, fruit)
}
// 0 apple
// 1 banana
// 2 grape
```

### 8. Slice of Slices
Just like Python lists, Go slices can contain other slices.
Example:
```go   
rows := [][]int{}
rows = append(rows, []int{1, 2, 3})
rows = append(rows, []int{4, 5, 6})
fmt.Println(rows)
// [[1 2 3] [4 5 6]]
```
You can access elements like this:
```go
fmt.Println(rows[1][2]) // 6
```

### 9. Appending Bug
When appending to a slice, be careful if you are appending to a slice that is itself an element of a slice of slices.
If the cap is exceeded during the append, a new underlying array will be created, and the changes will not be reflected in the original slice of slices.
Otherwise, it will overwrite the data in the original underlying array.

### Tricks:
- To make a string individual characters slice:
```go
runes := []rune("hello")
```
