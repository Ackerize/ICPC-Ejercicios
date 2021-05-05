class Solution:
    def reverse(self, x: int) -> int:
        if (x >= 0 and x <= 9):
            return x
        if str(x)[0] == '-':
            reversedNumber = int("-"+(str(x)[1::])[::-1])
        else:
            reversedNumber = int(str(x)[::-1])

        if(reversedNumber < -2**31 or reversedNumber > (2**31) - 1):
            return 0
        return reversedNumber