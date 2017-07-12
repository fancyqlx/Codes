#include <iostream>
#include <fstream>
using namespace std;

int main(){
    fstream fin("data.in",fstream::in);
    cin.rdbuf(fin.rdbuf());
    string s;
    while(getline(cin,s)){
        int c = 0;
        for(int i=0;i<s.size();++i){
            if(s[i]==' ') ++c;
        }
        int sz = s.size()+c*3+1;
        char * str = new char[sz];
        int j=s.size()-1;
        for(int i=sz-2;i>-1 && j>-1;--i,--j){
            if(s[j]==' '){
                str[i--] = '0';
                str[i--] = '2';
                str[i] = '%';
            }
            else str[i] = s[j];
        }
        str[sz-1] = '\0';
        cout<<str<<endl;
    }
}