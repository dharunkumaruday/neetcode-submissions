class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> m1;

        for(int num : nums){
            if(m1.contains(num))
                return true;
            m1[num] = 1;
        }

        return false;
    }
};