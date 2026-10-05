class Solution {
public:
    int maxArea(vector<int>& heights) {
        

        //Brute Force

        //calculate the area for all possible combinations and then return the max area.

        int area=0;

        for(int i=0;i<heights.size();i++)
        {
            for(int j=i+1;j<heights.size();j++)
            {
                int temp= min(heights[i],heights[j])*(j-i);

                if(temp>area){
                    area=temp;
                }
            }
        }
        return area;
    }
};
