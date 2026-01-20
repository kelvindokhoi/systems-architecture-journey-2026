# Maps in Go

### 1. Map Initialization
Maps in Go are like dictionaries in Python. They store key-value pairs.
The zero value of a map is `nil`.

To create a map, we use the `make` function like this:
```go
ages := make(map[string]int)
ages["John"] = 37
ages["Mary"] = 24
ages["Mary"] = 21 // overwrites 24
```
Or by using a literal:
```go
ages := map[string]int{
  "John": 37,
  "Mary": 21,
}
```

The len function works on a map and will return the total number of key/value pairs.
```go
ages := map[string]int{
  "John": 37,
  "Mary": 21,
}
fmt.Println(len(ages)) // 2
```

### 2. General Ops
**Insert:**
```go
m[key] = value
```

**Get an element:**
```go
ele := m[key]
```

**Delete an element:**
```go
delete(m, key)
```
`Delete` is safe even if the key doesn't exist.

**Check if a key exists:**
```go
ele, ok := m[key]
```
ok = true if key exists, false otherwise.

### 3. Key Types
Map keys may be any type that is **comparable**. Aka types that support the `==` and `!=` operators.
This would include:
- Booleans
- Numbers
- Strings
- Pointers
- Channels
- Interfaces
- Structs and Arrays (if their fields or elements are comparable)
And would exclude:
- Slices
- Maps
- Functions

Thus, we can do some fun stuffs like:
```go
hits := make(map[string]map[string]int)
n := hits["/doc/"]["au"]
```
This map of maps could be used to tally web pages hits by country.
However, this approach becomes clunky when adding data, because you need to check if the inner map exists first:
```go
func add(m map[string]map[string]int, path, country string) {
    mm, ok := m[path]
    if !ok {
        mm = make(map[string]int)
        m[path] = mm
    }
    mm[country]++
}
add(hits, "/doc/", "au")
```

On the other hand, if we use a struct as the value type, we can avoid this problem entirely:
```go
type Key struct {
    Path, Country string
}
hits := make(map[Key]int)
hits[Key{"/", "vn"}]++
n := hits[Key{"/ref/spec", "ch"}]
```

### 4. Count Instances
```go
names := map[string]int{}
missingNames := []string{}

if _, ok := names["Denna"]; !ok {
    // if the key doesn't exist yet,
    // append the name to the missingNames slice
    missingNames = append(missingNames, "Denna")
}
```
This code snippet counts the occurrences of names in a list and tracks missing names.

### 5. Missing Keys
When you try to get a value from a map using a key that doesn't exist, Go returns the zero value for the value type.

### 6. Sets using Maps
Go does not have a built-in set type, but we can use maps to implement sets.
```go
distinctWordsBool := make(map[string]bool)
distinctWordsStruct := make(map[string]struct{})

distinctWordsBool["hello"] = true         // Uses 1 byte for the bool value
distinctWordsStruct["hello"] = struct{}{} // Uses 0 bytes for the empty struct
```
The struct{} type is often preferred for sets because it uses no memory for the value, making it more memory efficient.

### 7. Maps are NOT safe for concurrent use

Maps are not safe for concurrent use! If you have multiple goroutines accessing the same map, and at least one of them is writing to the map, you must [lock](https://en.wikipedia.org/wiki/Readers%E2%80%93writer_lock) your maps with a mutex.