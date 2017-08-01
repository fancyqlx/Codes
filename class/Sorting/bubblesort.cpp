#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;


void bubblersort(vector<int> &nums){
    int n = nums.size();
    for(int i=0;i<n;++i){
        for(int j=n-1;j>i;--j){
            if(nums[j]<nums[j-1])
                swap(nums[j],nums[j-1]);
        }
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
    bubblersort(nums);
    cout<<"output: ";
    for(auto it=nums.begin();it!=nums.end();++it)
        cout<<*it<<" ";
    cout<<endl;
    return 0;
}