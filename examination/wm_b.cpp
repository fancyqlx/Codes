#include <iostream>
#include <stack>
#include <vector>

using namespace std;

void ball(int w, int h, int x, int n, vector<int> & vec){
    if(n==0) return;
    if(w-x>h){
        x = w-(2*h+x-w);
        vec.push_back(x);
        ball(w,h,x,n-1,vec);
    }
    else if(w-x==h){
        x = x;
        vec.push_back(x);
        ball(w,h,x,n-1,vec);
    }
    else{
        x = 2*w-2*h-x;
        vec.push_back(x);
        ball(w,h,x,n-1,vec);
    }
}

int main(){
    int w, h, x, n;
    while(cin>>w>>h>>x>>n){
        vector<int> vec;
        vec.push_back(x);
        ball(w,h,x,n-1,vec);
        for(vector<int>::iterator it = vec.begin();it!=vec.end();++it){
            cout<<*it<<' ';
        }
        cout<<endl;
    }
    return 0;
}