#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;


void quicksort(vector<int> &nums, int low, int high){
    if(low>=high) return;
    int i=low-1;
    int pivot = nums[high];
    for(int j=low;j<high;++j){
        if(nums[j]<pivot){
            ++i;
            swap(nums[i],nums[j]);
        }
    }
    ++i;
    swap(nums[high],nums[i]);
    quicksort(nums,low,i-1);
    quicksort(nums,i+1,high);
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
    quicksort(nums,0,nums.size()-1);
    cout<<"output: ";
    for(auto it=nums.begin();it!=nums.end();++it)
        cout<<*it<<" ";
    cout<<endl;
    return 0;
}