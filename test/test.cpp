#include <iostream>
#include <map>
#include <string>
#include <fstream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

double dis(double a[3], double b[3]){
    double x = a[0]-b[0],y=a[1]-b[1],z=a[2]-b[2];
    return sqrt(x*x+y*y+z*z);
}

int main(){
    fstream fin("..\\test\\data.in",fstream::in);
    cin.rdbuf(fin.rdbuf());
    int n;
    while(cin>>n){
        char * color = new char[n];
        double (*point)[3] = new double[n][3];
        char ch; double p;
        for(int i=0;i<n;++i){
            cin>>ch; color[i] = ch;
            for(int j=0;j<3;++j){
                cin>>p; point[i][j] = p;
            }
        }
        double max = 0;
        for(int i=0;i<n;++i){
            for(int j=i+1;j<n;++j){
                for(int k=j+1;k<n;++k){
                    if((color[i] == color[j] && color[i] == color[k] && color[j]==color[k]) || (color[i]!=color[j] && color[i]!=color[k] && color[j]!=color[k])){
                        double a=dis(point[i],point[j]);
                        double b=dis(point[i],point[k]);
                        double c=dis(point[j],point[k]);
                        double p=(a+b+c)/2;
                        double s=sqrt(p*(p-a)*(p-b)*(p-c));
                        if(s>max) max = s;
                    }
                }
            }
        }
        //cout.precision(5);
        cout<<fixed<<setprecision(5)<<max<<endl;
    }
    return 0;
}