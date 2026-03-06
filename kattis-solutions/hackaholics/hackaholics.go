package main

import (
	"fmt"
)

func main(){
	var N_num_hackathons int
	var C_money_spent int
	var P_avarage_money_per_hkt int
	fmt.Scanln(&N_num_hackathons)
	fmt.Scanln(&C_money_spent)
	fmt.Scanln(&P_avarage_money_per_hkt)
	fmt.Print(N_num_hackathons*P_avarage_money_per_hkt)
}