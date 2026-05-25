class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> dict;
        int length = 0;
        int start = 0;
        for (int i=0; i <s.size();i++){
            dict[s[i]] = (dict.contains(s[i]))? dict[s[i]] + 1: 1;



            while (dict[s[i]] >= 2){
                dict[s[start]] -= 1;
                start++;
            }
            length = max(length, i - start + 1);
        }
    return length;
    }
};