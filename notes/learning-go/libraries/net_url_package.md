# net/url in Go

The `net/url` package is part of Go's standard library. You can instantiate a [URL struct](https://pkg.go.dev/net/url#Parse) using `url.Parse`:
```go
parsedURL, err := url.Parse("https://homestarrunner.com/toons")
if err != nil {
	fmt.Println("error parsing url:", err)
	return
}
```
and it will give us this type of struct:
```go
type URL struct {
	Scheme      string
	Opaque      string    // encoded opaque data
	User        *Userinfo // username and password information
	Host        string    // host or host:port (see Hostname and Port methods)
	Path        string    // path (relative paths may omit leading slash)
	RawPath     string    // encoded path hint (see EscapedPath method)
	OmitHost    bool      // do not emit empty host (authority)
	ForceQuery  bool      // append a query ('?') even if RawQuery is empty
	RawQuery    string    // encoded query values, without '?'
	Fragment    string    // fragment for references, without '#'
	RawFragment string    // encoded fragment hint (see EscapedFragment method)
}
```
The fields of the URL struct represent different components of a URL, such as the scheme (e.g., "https"), host (e.g., "homestarrunner.com"), path (e.g., "/toons"), query parameters, and fragment identifiers.

And then you can extract just the hostname:
```go
parsedURL.Hostname()
// homestarrunner.com
```