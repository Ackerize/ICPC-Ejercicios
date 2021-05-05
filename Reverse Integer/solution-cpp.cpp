class Solution {
public:
    int reverse(int x) {
        if(x >= 0 && x <= 9) return x;

        string newString = to_string(x);

        if(x < 0){
            std::reverse(newString.begin() + 1, newString.end());
        }else{
            std::reverse(newString.begin(), newString.end());
        }

        long long newInt = stoll(newString);

        if(newInt < -pow(2, 31) || newInt > pow(2, 31) - 1) return 0;

        return newInt;
    }
};