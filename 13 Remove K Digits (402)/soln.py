class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        Strategy;
        Remove the last character if numbers are monotonically increasing
        else remove first number whose next number is less than it
        flag to check which of these happened
        '''
        if k==0:
            return num
        length = len(num)
        if length==k:
            return '0'
        num = list(num)
        num.append(',')
        index = 0
        while(True):            
            if num[index]>num[index+1]:
                del(num[index]) 
                k-=1
                if index!=0:
                    index-=1
                if k==0:
                    del (num[-1])
                    return str(int(''.join(num)))
            else:
                index+=1
                