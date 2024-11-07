class Solution {
public:
    vector<int> runningSum(vector<int>& vec) {
        vector<int> res(vec);
        res[0] = vec[0];
        for(int i=1;i<vec.size();i++){
            res[i] = res[i-1]+vec[i];  
        }
        return res;
    }
};