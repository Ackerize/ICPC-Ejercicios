class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        map<int, vector<int>> m;
        for(int i = 0; i < groupSizes.size(); i++){
            m[groupSizes[i]].push_back(i);
        }
        vector<vector<int>> res;
        vector<int> temp;
        for(map<int, vector<int>>::const_iterator it = m.begin(); it != m.end(); ++it){
            for(int j = 0; j < it->second.size(); j++){
                temp.push_back(it->second.at(j));
                if(temp.size() == it->first){
                    res.push_back(temp);
                    temp.clear();
                }
            }
        }
        return res;
    }
};