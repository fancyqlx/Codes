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

void iteration(int *s, int *f, int **c, int n){
    for(int j=1;j<=n+1;++j){
        for(int i=0;i<=n+1;++i){
            int k = j;
            int max = 0;
            for(int l=i+1;l<=k;++l){
                if(f[i]<=s[l] && f[l]<=s[k]){
                    int temp = c[i][l]+c[l][k]+1;
                    max = (max<temp)?temp:max;
                }
            }
            c[i][k] = max;
            ++k;
        }
    }
}

// int c(int i, int j, int *s, int *f){
//     int max = 0;
//     for(int k=i+1;k<j;++k){
//         if(f[i]<=s[k] && f[k]<=s[j]){
//             int temp = c(i,k,s,f)+c(k,j,s,f)+1;
//             max = max<temp?temp:max;
//         }
//     }
//     return max;
// }

int main(){
    fstream fin("data.in",fstream::in);
    cin.rdbuf(fin.rdbuf());
    int n;
    while(cin>>n){
        int *s = new int[n+2];
        int *f = new int[n+2];
        //input
        s[0] = 0;
        f[0] = 0;
        for(int i=1;i<n+1;++i) cin>>s[i];
        for(int i=1;i<n+1;++i) cin>>f[i];
        s[n+1] = numeric_limits<int>::max();
        f[n+1] = numeric_limits<int>::max();
        //bottom-up implementation
        int ** c = new int*[n];
        for(int i=0;i<n+2;++i){
            c[i] = new int[n+2]();
        }
        iteration(s,f,c,n);
        for(int i=0;i<=n+1;++i){
            for(int j=0;j<=n+1;++j) cout<<c[i][j];
            cout<<endl;
        }
        //top-down implementation
        //cout<<c(0,n+1,s,f)<<endl;
    }
    return 0;
}
