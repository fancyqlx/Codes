#include <iostream>
#include <cstdio>
#include <math.h>
using namespace std;

double sum = 0;
int N;
double Q;
double P;

void recursion(int l, int num, int flag, double pro, double a)
{
    if(flag && (a > 0)){
        if(num==1) {
            sum += pro*l;
            return;
        }
        --num;
        double b = P/(1<<(N-num));
        if(b>=1) recursion(l+1,num,1,pro*1,1);
        else{
            recursion(l+1,num,1,pro*b,b);
            recursion(l+1,num,0,pro*(1-b),(1-b));
        }
    }
    else{
        a = a + Q;
        if(a>=1) recursion(l+1,num,1,pro*1,1);
        else{
            recursion(l+1,num,1,pro*a,a);
            recursion(l+1,num,0,pro*(1-a),1-a);
        }
    }
}

int main(){
    
    while(cin>>P>>Q>>N){
        sum = 0;
        P /= 100;
        Q /= 100;
        if(P>0){
            recursion(1,N,1,P,P);
            recursion(1,N,0,1-P,1-P);
        }
        else{
            recursion(1,N,0,1,1);
        }
        printf("%.2f\n",sum);
    }
    return 0;
}