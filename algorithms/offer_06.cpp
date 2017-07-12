#include <iostream>
#include <fstream>
using namespace std;

struct TreeNode{
    int key;
    TreeNode * left;
    TreeNode * right;
    TreeNode(int k, TreeNode * l=NULL, TreeNode * r=NULL):key(k){
        left = l; right = r;
    }
    TreeNode(){};
};

TreeNode * construct(int* pre, int pl, int pr, int* mid, int ml, int mr){
    if(pl>pr) return NULL;
    TreeNode * head = new TreeNode(pre[pl]);
    int i=ml;
    for(;i<=mr;++i){
        if(mid[i]==pre[pl]) break;
    }
    head->left = construct(pre, pl+1, pl+i-ml, mid, ml, i-1);
    head->right = construct(pre, pl+i-ml+1, pr, mid, i+1, mr);
    return head;
}

void print(TreeNode * p){
    if(p!=NULL){
        cout<<p->key;
        print(p->left);
        print(p->right);
    }
}

int main(){
    fstream fin("data.in",fstream::in);
    cin.rdbuf(fin.rdbuf());
    int n;
    while(cin>>n){
        int * pre = new int[n];
        int * mid = new int[n];
        int t = 0;
        for(int i=0;i<n;++i){cin>>t; pre[i] = t;}
        for(int i=0;i<n;++i){cin>>t; mid[i] = t;}
        TreeNode * head = construct(pre,0,n-1,mid,0,n-1);
        print(head);
    }
    return 0;
}