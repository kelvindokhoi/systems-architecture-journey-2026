# Defer in Go

`defer` is a keyword in Go that schedules a function call to be run after the function completes. This is often used for cleanup tasks, such as closing files or releasing resources.

When a function containing a `defer` statement returns, the deferred function calls are executed in last-in-first-out order.