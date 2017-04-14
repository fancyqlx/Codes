#include <iostream>
using namespace std;

int main(){
    int a = int(3);
    cout<<a<<endl;
    int *p = new int(5);
    int *q = new int[10]();
    cout<<*p<<endl;
    return 0;
}