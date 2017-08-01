#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;


int main(){
    int n;
    while(cin>>n){
        vector<int> h;
        for(int i=0;i<n;++i){
            int temp; cin>>temp;
            h.push_back(temp);
        }
        int m;
        cin>>m;
        vector<int> w;
        for(int i=0;i<m;++i){
            int temp; cin>>temp;
            w.push_back(temp);
        }

        int count = 0;
        sort(h.begin(),h.end());
        sort(w.begin(),w.end());

        int *has = new int[h.size()]();
        
        for(int i=0;i<w.size();++i){
            for(int j=h.size()-1;j>=0;--j){
                if(has[j]==0 && w[i]>=h[j] ){
                    has[j] = 1;
                    ++count;
                    break;
                }
            }
        }
        cout<<count<<endl;

    }
    return 0;
}