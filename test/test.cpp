#include <iostream>
#include <map>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

vector<string> rec(string & digits, vector<string> *tel, int i, int j){
        if(i==j) return tel[digits[i]-'0'];
        vector<string> vec;
        int mid = (i+j)/2;
        vector<string> a = rec(digits,tel,i,mid);
        vector<string> b = rec(digits,tel,mid+1,j);
        for(vector<string>::iterator it_a = a.begin();it_a!=a.end();++it_a){
            for(vector<string>::iterator it_b = b.begin();it_b!=b.end();++it_b){
                vec.push_back(*it_a+*it_b);
            }   
        }
        return vec;
    }
    
    vector<string> letterCombinations(string digits) {
        vector<string> tel[10] = {{},{},{"a","b","c"},{"d","e","f"},{"g","h","i"},
                            {"j","k","l"},{"m","n","o"},{"p","q","r","s"},
                            {"t","u","v"},{"w","x","y","z"}};
        return rec(digits,tel,0,digits.size());
    }

int main(){
    //fstream fin("..\\test\\data.in",fstream::in);
    //cin.rdbuf(fin.rdbuf());
    vector<string> tel[10] = {{},{},{"a","b","c"},{"d","e","f"},{"g","h","i"},
                            {"j","k","l"},{"m","n","o"},{"p","q","r","s"},
                            {"t","u","v"},{"w","x","y","z"}};
    string digits = "34342";
    letterCombinations(digits);
    return 0;
}