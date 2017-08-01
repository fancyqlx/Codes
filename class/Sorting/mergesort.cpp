#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;


void mergesort(vector<int> &nums, int left, int right){
    if(left>=right) return;
    int mid = (left+right)/2;
    mergesort(nums,left,mid);
    mergesort(nums,mid+1,right);

    vector<int> temp;
    int i=left, j=mid+1;
    while(i<=mid && j<=right){
        if(nums[i]<=nums[j])
            temp.push_back(nums[i++]);
        else
            temp.push_back(nums[j++]);
    }
    while(i<=mid) temp.push_back(nums[i++]);
    while(j<=right) temp.push_back(nums[j++]);
    i=0;
    for(int k=left;k<=right;++k){
        nums[k] = temp[i++];
    }
}

int main(){
    fstream fin("data.in",fstream::in);
    cin.rdbuf(fin.rdbuf());
    int num;
    vector<int> nums;
    while(cin>>num){
        nums.push_back(num);
    }
    cout<<"input: ";
    for(auto it=nums.begin();it!=nums.end();++it)
        cout<<*it<<" ";
    cout<<endl;
    mergesort(nums,0,nums.size()-1);
    cout<<"output: ";
    for(auto it=nums.begin();it!=nums.end();++it)
        cout<<*it<<" ";
    cout<<endl;
    return 0;
}