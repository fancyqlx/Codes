#include <iostream>
#include <stdio.h>
#include <cstring>
#include <string>
#include <stdexcept>
#include <fstream>
#include <vector>
#include <algorithm>
#include <limits>
#include <stack>

using namespace std;

int min_stack(int * B, stack<int> & ST){
    int index = ST.top();
    ST.pop();
    int min = B[index];
    stack<int> temp;
    while(ST.size()!=0){
        int t = ST.top();
        ST.pop();
        if(B[t] < min) {
            temp.push(index);
            index = t;
        }
    }
    while(temp.size()!=0){
        ST.push(temp.top());
        temp.pop();
    }
    return index;
}

stack<int> Dijkstra(int A[][6], int x, int y){
    int B[6];
    for(int i=0;i<6;++i){
        B[i] = numeric_limits<int>::max();
    }
    B[x] = 0;
    int C[6] = {0,0,0,0,0,0};
    int * pre = new int[6]();
    stack<int> ST;
    ST.push(x);
    while(ST.size()!=0){
        int s = min_stack(B,ST);
        C[s] = -1;
        for(int i=0;i<6;++i){
            if(A[s][i] != -1 && C[i] != -1){
                if(B[i] > B[s] + A[s][i]){
                    B[i] = B[s] + A[s][i];
                    pre[i] = s;
                }
            }
        }
    }
    stack<int> road;
    int i = y;
    road.push(i);
    while(i!=x){
        i = pre[i];
        road.push(i);
    }
    cout<<B[y]<<endl;
    return road;
}

int main(){
    //fstream fin("data.in",fstream::in);
    //cin.rdbuf(fin.rdbuf());
    int x,y;
    int A[6][6] = {{1,2,3,4,5,6},
                    {2,4,1,1,4,6},
                    {5,2,5,1,8,4},
                    {3,5,2,7,4,7},
                    {2,3,4,5,7,1},
                    {4,2,3,6,7,1}};
    while(cin>>x>>y){
        stack<int> road = Dijkstra(A,x,y);
        while(road.size()!=1 && road.size()!=0){
            cout<<(road.top())<<',';
            road.pop();
        }
        cout<<road.top()<<endl;
    }
    return 0;
}
