from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list_ = []
        fizz_buzz = {
            3: "Fizz",
            5: "Buzz",
            15: "FizzBuzz"
        }
        
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                list_.append(fizz_buzz[15])
            elif i % 3 == 0:
                list_.append(fizz_buzz[3])
            elif i % 5 == 0:
                list_.append(fizz_buzz[5])
            else:
                list_.append(str(i))
        return list_
    
print(Solution().fizzBuzz(50))