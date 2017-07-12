#include <iostream>
#include <map>
#include <string>
#include <fstream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <cstring>
#include <set>
#include <list>

using namespace std;

vector<int> maxInWindows(const vector<int>& num, unsigned int size)
    {
        vector<int> ret;
        int n = num.size();
        if(n==0) return ret;
        int cur_max = num[0];
        int ptr = -1;
        for(int i=0;i<n && i<size;++i){
            if(num[i]>=cur_max){
                cur_max = num[i];
                ptr = i;
            }
        }
        ret.push_back(cur_max);
        for(int i=size;i<n;++i){
            if(num[i]>=cur_max){
                ret.push_back(num[i]);
                cur_max = num[i];
                ptr = i;
            }
            else if(ptr>=i+1-size){
                ret.push_back(cur_max);
            }
            else{
                cur_max = num[i];
                for(int j=i+1-size;j>=0 && j<=i;++j){
                    if(num[j]>=cur_max){
                        cur_max = num[j];
                        ptr = j;
                    }
                }
                ret.push_back(cur_max);
            }
        }
        return ret;
    }


int main(){
    vector<int> vec = {16,14,12,10,8,6,4};
    vector<int> ret = maxInWindows(vec, 5);
    for(int i=0;i<ret.size();++i)
        cout<<ret[i]<<" ";
    cout<<endl;
    return 0;
}