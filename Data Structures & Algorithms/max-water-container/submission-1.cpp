class Solution {
public:
    int maxArea(vector<int>& heights) {
        

        // Brute Force got TLE. we need to think of o(n) time complexity.
        
        int l=0;
        int r= heights.size()-1;
        int area=0;
        
        while(l<r)
        {
            int temp= (r-l)*min(heights[l],heights[r]);
            area=max(temp,area);

            if(heights[l]<heights[r])
            {
                l++;
            }
            else{
                r--;
            }
        }

        return area;
    }
};
