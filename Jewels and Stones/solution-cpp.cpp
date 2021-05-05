class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
      int contador = 0, nStones = stones.length();
      char stones_array[nStones + 1];
        strcpy(stones_array, stones.c_str());

        for (char x : jewels) contador += count(stones_array, stones_array + nStones, x);
        return contador; 
    }
};