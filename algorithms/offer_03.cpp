#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main(){
    fstream fin("data.in",fstream::in);
    cin.rdbuf(fin.rdbuf());
    int n, num;
    while(cin>>n>>num){
        vector<vector<int> > vec;
        for(int i=0;i<n;++i){
            vector<int> v;
            for(int j=0;j<n;++j){
                int t; cin>>t;
                v.push_back(t);
            }
            vec.push_back(v);
        }
        int row=0, col=n-1, flag = 0;
        while(row<n && col>-1){
            if(vec[row][col]<num) ++row;
            else if(vec[row][col]>num) --col;
            else{
                flag = 1;
                break;
            }
        }
        cout<<flag<<endl;
    }
    return 0;
}