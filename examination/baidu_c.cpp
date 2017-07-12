#include <iostream>
using namespace std;

int main(){
    int n,k;
    while(cin>>n>>k){
        int **dp = new int *[n+1];
        for(int i=0;i<=n;++i) {
            dp[i] = new int[k+1]();
            dp[i][0] = 1;
        }
        for(int i=2;i<=n;++i){
            for(int j=1;j<=k;++j){
                dp[i][j] = dp[i-1][j-1]*(i-j)+dp[i-1][j]*(j+1);
            }
        }
        cout<<dp[n][k]%2017<<endl;
    }
    return 0;
}