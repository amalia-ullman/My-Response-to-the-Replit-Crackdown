#include <vector>
using namespace std;
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int temp = 0;
        for(int x; x < m + n; x++){
            cout << nums1[x] << endl;
            cout << nums2[temp] << endl; 
            if(nums1[x] > nums2[temp]){
                nums1.insert(nums1.begin(),nums2[temp]);
                temp++;
            }
        }

    }
};