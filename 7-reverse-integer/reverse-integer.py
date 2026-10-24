import math
class Solution:
    def reverse(self, x: int) -> int:
        if(x>0):
            val=int(str(x)[::-1])
        elif(x<0):
            val=-(int(str(abs(x))[::-1]))
        else:
            return 0
        if(val<-2**31 or val>2**31-1):
                return 0
        else:
                return val