#include <iostream>
#include <fstream>

using namespace std;

int r_bag(int *v, int *w, int i, int g){
    if(i == 0 || g == 0) return 0;
    int a = r_bag(v,w,i-1,g);
    int b=0;
    if(g-w[i]>=0) {
        b = r_bag(v,w,i-1,g-w[i]) + v[i];
        return (a>b?a:b);
    }
    return a;
}

int main(){
    fstream fin("data.in",fstream::in);
    cin.rdbuf(fin.rdbuf());
    int n,g;
    while(cin>>n>>g){
        //input
        int *w = new int[n+1]();
        int *v = new int[n+1]();
        for(int i=1;i<n+1;++i) cin>>w[i]>>v[i];
        //bottom-up implementation
        //implementation-two-dimensional-array
        //initialization
        //int **c = new int*[n];
        // for(int i=0;i<n+1;++i) c[i] = new int[g+1]();
        // for(int i=1;i<=n;++i){
        //     for(int j=1;j<=g;++j){
        //         if(j-w[i]>=0){
        //             c[i][j] = max(c[i-1][j],c[i-1][j-w[i]]+v[i]);
        //         }
        //     }
        // }
        // cout<<c[n][g]<<endl;
        //implementation-one-dimensinal-array
        int *c = new int[g+1]();
        for(int i=1;i<=n;++i){
            for(int j=g;j>0;--j){
                if(j-w[i]>=0)
                    c[j] = max(c[j],c[j-w[i]]+v[i]);
            }
        }
        cout<<c[g]<<endl;
        //top-down implementation
        //cout<<r_bag(v,w,n,g)<<endl;
    }
    return 0;
}