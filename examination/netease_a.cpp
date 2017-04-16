#include <iostream>
#include <fstream>
#include <map>
#include <string>
using namespace std;

map<string,int> m;

void rec(int & i, string & s){
    int n = s.size();
    if(i >= n) return;
    while(i<n){
        if(s[i] == '<' && i+1<n && s[i+1] == 'd'){
            i += 7;
            while(i<n && i+1 <n && s[i+1] != '/'){
                if(s[i] == '<' && s[i+1] != '/') rec(i,s);
                if(s[i] != ' ' and s[i] != '<') m["black"] += 1;
                ++i;
            }
            i += 8;
            return;
        }
        if(s[i] == '<' && i+1<n && s[i+1] == 'c'){
            i += 7;
            string color;
            while(i < n && s[i] != '>'){
                color += s[i];
                ++i;
            }
            ++i;
            while(i<n && i+1 <n && s[i+1] != '/'){
                if(s[i] == '<' && s[i+1] != '/') rec(i,s);
                if(s[i] != ' ' and s[i] != '<') m[color] += 1;
                ++i;
            }
            i += 8;
            return;
        }
        ++i;
    }
    
}

int main(){
    fstream fin("data.in",fstream::in);
    cin.rdbuf(fin.rdbuf());
    int s;
    while(cin>>s){
        cin.ignore();
        for(int i=0;i<s;++i){
            m.clear();
            m["black"] = 0;
            string line;
            getline(cin,line);
            int j = 0;
            rec(j,line);
            cout<<"Case "<<i<<" "<<line.size()<<" "<<m.size()<<endl;
            for(map<string,int>::iterator it = m.begin();it!=m.end();++it){
                if(it->second != 0){
                    cout<<it->first<<": "<<it->second<<endl;
                }
            }
        }
    }
    return 0;
}