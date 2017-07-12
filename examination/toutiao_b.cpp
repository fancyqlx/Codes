
#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <vector>
#include <fstream>
using namespace std;

int main(){
    fstream fin("data.in",fstream::in);
    cin.rdbuf(fin.rdbuf());
    int n, m;
    while(cin>>n>>m){
        vector<string> vec_n;
        vector<set<string> > vec_sn;
        vector<set<string> > vec_sm;
        for(int i=0;i<n;++i){
            string line, word;
            getline(cin, line);
            vec_n.push_back(line);
            stringstream stream(line);
            set<string> set_w;
            while(stream>>word){
                word[0] = tolower(word[0]);
                set_w.insert(word);
            }
            vec_sn.push_back(set_w);
        }
        for(int i=0;i<m;++i){
            string line, word;
            getline(cin, line);
            stringstream stream(line);
            set<string> set_w;
            while(stream>>word){
                word[0] = tolower(word[0]);
                set_w.insert(word);
            }
            vec_sm.push_back(set_w);
        }

        for(int i=0;i<m;++i){
            int max = -1;
            int index = 0;
            for(int j=0;j<n;++j){
                int same = 0;
                for(set<string>::iterator k=vec_sm[i].begin(); k!=vec_sm[i].end();++k)
                    if(vec_sn[j].count(*k))
                        ++same;
                if(same > max){
                    max = same;
                    index = j;
                }
            }
            cout<<vec_n[index]<<endl;
        }
    }
    return 0;
}