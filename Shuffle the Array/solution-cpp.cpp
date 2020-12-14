class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> result;
        for(int i = 0; i < n; i++){
            result.push_back(nums.at(i));
            result.push_back(nums.at(i+n));
        }
        return result;
    }
};