class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> dictionary;
        int idx = 0;
        for (auto number : nums){
            int desired_num = target - number;
            if (dictionary.find(desired_num) != dictionary.end()){
                return vector<int>({dictionary.find(desired_num)->second, idx});
            }
            dictionary[number] = idx;

            ++idx;
        }
        return vector<int>({-1, -2});
    }
};