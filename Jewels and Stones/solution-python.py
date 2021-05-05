class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        contador = 0
        for c in jewels:
            contador += stones.count(c)
        return contador