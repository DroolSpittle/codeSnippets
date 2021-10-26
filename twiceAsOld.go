package main

import
(
	"fmt"
	"math"
)

func TwiceAsOld(dadYearsOld, sonYearsOld int) int {
	if dadYearsOld/2 == sonYearsOld {
		return 0;
	}
	difference := dadYearsOld - sonYearsOld
	result := float64(difference - sonYearsOld)
	return int(math.Abs(result));
}

func main() {
	fmt.Println(TwiceAsOld(42,21))
	fmt.Println(TwiceAsOld(36,7))
	fmt.Println(TwiceAsOld(29,0))
}

//Better Way

package main
import "math"

func TwiceAsOld(dadYearsOld int, sonYearsOld int) int { 
  return int(math.Abs(float64(dadYearsOld - (sonYearsOld * 2))))
}
