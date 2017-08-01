#include <iostream>
#include <vector>

using namespace std;

long long int find_max(vector<long long int> &nums, int left, int right){
    int max_idx = left;
    for(int i=left;i<=right;++i){
        if(nums[i]>nums[max_idx]) max_idx = i;
    }
    swap(nums[max_idx],nums[right]);
    return nums[right];
}

long long int find_min(vector<long long int> &nums, int left, int right){
    int min_idx = left;
    for(int i=left;i<=right;++i){
        if(nums[i]<nums[min_idx]) min_idx = i;
    }
    swap(nums[min_idx],nums[left]);
    return nums[left];
}

int main(){
    int n;
    while(cin>>n){
        vector<long long int> nums;
        for(int i=0;i<n;++i){
            int temp;
            cin>>temp;
            nums.push_back(temp);
        }
        if(n<3){
            cout<<0<<endl;
            continue;
        }
        long long int max_1 = find_max(nums,0,n-1);
        long long int max_2 = find_max(nums,0,n-2);
        long long int max_3 = find_max(nums,0,n-3);
        long long int min_1 = find_min(nums,0,n-1);
        long long int min_2 = find_min(nums,1,n-1);
		long long int product = max(max_1*max_2*max_3, max_1*min_1*min_2);
        cout<<product<<endl;
    }
    return 0;
}