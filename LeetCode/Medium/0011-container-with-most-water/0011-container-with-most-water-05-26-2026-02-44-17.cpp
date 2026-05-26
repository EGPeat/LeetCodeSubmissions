class Solution {
public:
    int maxArea(vector<int>& height) {
        int st = 0, ed = height.size() - 1;
        cout << height.size() << endl;
        int maxarea = min(height[st], height[ed]) * (ed-st);
        
        int curr_area = 0;
        while (st < ed){
            int w = ed - st;
            int h =min(height[st], height[ed]);
            curr_area = w * h;
            if (height[st] > height[ed]){ed--;}
            else{st++;}
            maxarea = max(maxarea, curr_area);
        }
        return maxarea;
    }
};