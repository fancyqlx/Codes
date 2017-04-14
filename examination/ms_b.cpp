#include <iostream>
#include <vector>
#include <fstream>
#include <set>
using namespace std;

int main(){
    fstream fin("data.in",fstream::in);
    cin.rdbuf(fin.rdbuf());
    int N, M, K;
    while(cin>>N>>M>>K){
        int * parent = new int[N+1]();
        vector<vector<int> > vec_l;
        int * level = new int[M];
        for(int i=0;i<M;++i) cin>>level[i];
        for(int i=0;i<M;++i){
            vector<int> vec_temp;
            for(int j=0;j<level[i];++j){
                int temp;
                cin>>temp;
                vec_temp.push_back(temp);
            }
            vec_l.push_back(vec_temp);
        }
        int * leaf = new int[K];
        set<int> set_l;
        for(int i=0;i<K;++i) {
            cin>>leaf[i];
            set_l.insert(leaf[i]);
        }
        int **dis = new int*[N+1];
        for(int i=0;i<N+1;++i) dis[i] = new int[N+1]();
        for(int i=0;i<K;++i)
            for(int j=0;j<K;++j)
                cin>>dis[leaf[i]][leaf[j]];
        //finished initialization
        for(int i=M-1;i>0;--i){
            for(int j=0;j<level[i];++j){
                if(j==0){
                    for(int k=0;k<level[i-1];++k){
                        if(!set_l.count(vec_l[i-1][k])){
                            parent[vec_l[i][j]] = vec_l[i-1][k];
                            break;
                        }
                    }
                    for(int t=0;t<N+1;++t){
                        if(dis[vec_l[i][j]][t]!=0){
                            dis[parent[vec_l[i][j]]][t] = dis[vec_l[i][j]][t]-1;
                            dis[t][parent[vec_l[i][j]]] = dis[vec_l[i][j]][t]-1;
                        }
                    }
                    dis[parent[vec_l[i][j]]][j] = 1;
                    dis[j][parent[vec_l[i][j]]] = 1;
                }
                else if(dis[vec_l[i][j]][vec_l[i][j-1]]==2){
                    parent[vec_l[i][j]] = parent[vec_l[i][j-1]];
                }
                else{
                    for(int k=0;k<level[i-1];++k){
                        if(!set_l.count(vec_l[i-1][k]) && vec_l[i-1][k] != parent[vec_l[i][j-1]])
                        {
                            parent[vec_l[i][j]] = vec_l[i-1][k];
                            break;
                        }
                    }
                    for(int t=0;t<N+1;++t){
                        if(dis[vec_l[i][j]][t]!=0){
                            dis[parent[vec_l[i][j]]][t] = dis[vec_l[i][j]][t]-1;
                            dis[t][parent[vec_l[i][j]]] = dis[vec_l[i][j]][t]-1;
                        }
                    }
                }
            }
        }
        for(int i=1;i<N+1;++i) cout<<parent[i]<<" ";
        cout<<endl;
    }
    return 0;
}