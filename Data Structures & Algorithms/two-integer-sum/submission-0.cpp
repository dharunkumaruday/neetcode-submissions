class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m1;

        for(int i = 0; i < nums.size(); i ++){
            if(m1.contains(target - nums[i]))
                return {m1[target - nums[i]], i};
            m1[nums[i]] = i;
        }

        return {};
    }
};
