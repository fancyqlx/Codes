#include <iostream>
#include <set>
#include <map>
#include <string>
#include <fstream>
#include <cmath>

using namespace std;

int fac(int x){
    int num = 1;
    while(x!=0){
        num *= x;
        --x;
    }
    return num;
}

int main(){
    fstream fin("data.in",fstream::in);
    cin.rdbuf(fin.rdbuf());
    int T;
    while(cin>>T){
        map<string, set<string> > m;
        set<string> s_1;
        set<string> s_2;
        string x,y;
        for(int i=0;i<T;++i){
            cin>>x>>y;
            if(m.count(y)) m[y].insert(x);
            else m[y] = set<string>();
            if(x[1]=='1') s_1.insert(x);
            else s_2.insert(x);
        }
        int num = fac(8);
        for(int i=7;i>0;--i){
            num -= pow(6,7-i)*fac(i);
        }
        cout<<num<<endl;
    }
    return 0;
}