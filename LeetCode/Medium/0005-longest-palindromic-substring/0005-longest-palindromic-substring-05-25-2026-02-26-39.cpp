class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, true));
        int start_pos = 0;
        int max_length = 1;

        for(int i=n-2; i > -1; i--){
            for (int j=i+1; j < n; j++){
                dp[i][j] = false;
                if (s[i] == s[j]){
                    dp[i][j] = dp[i + 1][j - 1];
                    if (dp[i][j] and max_length < j-i+1){
                        start_pos = i;
                        max_length = j-i+1;
                    }
                }
            }


        }

    return s.substr(start_pos, max_length);
    }
};