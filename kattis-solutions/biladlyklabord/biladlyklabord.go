package main

import (
	"fmt"
	"os"
	"bufio"
)
func check (inp string) string{
	if len(inp) < 2{
		return inp
	}
	r_inp := []rune(inp)
	var outp []rune
	old := r_inp[0]
	for i:=1;i<len(inp);i++ {
		if r_inp[i]!=old{
			outp = append(outp, old)
			old = r_inp[i]
		} else {
			if i==len(inp)-1{
				outp = append(outp, r_inp[i])
			}
		}
	}
	return string(outp)
}
func main(){
	in := bufio.NewReader(os.Stdin)
	inp,_ := in.ReadString('\n')
	fmt.Print(check(inp))
}