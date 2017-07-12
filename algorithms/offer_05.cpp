#include <iostream>
#include <fstream>
using namespace std;

struct ListNode{
    int key;
    ListNode * next;
};

void print(ListNode * p){
    if(p->next != NULL){
        print(p->next);
    }
    cout<<p->key<<endl;
}

int main(){
    fstream fin("data.in",fstream::in);
    cin.rdbuf(fin.rdbuf());
    int n;
    while(cin>>n){
        ListNode * p = NULL;
        ListNode * head = NULL;
        for(int i=0;i<n;++i){
            ListNode * q = new ListNode();
            int key;
            cin>>key;
            q->key = key;
            if(p != NULL) {p->next = q; p = p->next;}
            else {p = q; head = q;}
        }
        print(head);
    }
    return 0;
}