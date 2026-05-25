class Solution {
public:
    int reverse(int x) {
        long output = 0;
        bool is_neg = false;
        if (x < 0){
            is_neg = true;
            x = static_cast<long>(x) * -1;
        }
        while (x>0){
            output *= 10;
            output += x%10;
            x /= 10;
        }
        if (is_neg){
            output *= -1;
        }
        if ((output >pow(2,31)-1) or (output < -pow(2,31))){
            output = 0;
        }

    
    return static_cast<int>(output);}
};