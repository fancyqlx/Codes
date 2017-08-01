#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

void max_heapify(vector<int> &nums, int i, int size){
    if(i>=size-1) return;
    int left = i*2+1, right = i*2+2;
    int max_idx = i;
    if(left<=size-1){
        if(nums[left]>nums[i])
            max_idx = left;
        if(right<=size-1){
            if(nums[right]>nums[max_idx])
                max_idx = right;
        }
        if(i!=max_idx){
            swap(nums[i],nums[max_idx]);
            max_heapify(nums,max_idx,size);
        }
    }
}

void construct_heap(vector<int> &nums){
    for(int i=nums.size()/2-1;i>=0;--i){
        max_heapify(nums,i,nums.size());
    }
}

void heapsort(vector<int> &nums){
    construct_heap(nums);
    int n = nums.size();
    for(int i=n-1;i>=0;--i){
        swap(nums[0],nums[i]);
        max_heapify(nums,0,--n);
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
    heapsort(nums);
    cout<<"output: ";
    for(auto it=nums.begin();it!=nums.end();++it)
        cout<<*it<<" ";
    cout<<endl;
    return 0;
}