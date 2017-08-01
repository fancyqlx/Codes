#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;


string multi(string str1, string str2)
{
    int i, j;
    
    int length1 = str1.size();
    int length2 = str2.size();
    string result = "";

    reverse(str1.begin(), str1.end());
    reverse(str2.begin(), str2.end());

    if (length1 == 0 || length2 == 0)
        return result;

    int *iresult = new int[length1+length2+1]();

    for(i = 0; i < length1; i++)
        for(j = 0; j < length2; j++)
            iresult[i+j] += ((str1[i] - '0') * (str2[j] - '0'));

    int carry = 0;
    for(i = 0; i < length1 + length2; i++)
    {
        int value = iresult[i] + carry;
        iresult[i] = value % 10;
        carry = value / 10;
    }

    for(i = length1 + length2 - 1; i >= 0; i--)
    {
        if(iresult[i] != 0)
            break;
    }

    for(; i >= 0; i--)
        result = result + (char)(iresult[i]+'0');

    delete [] iresult;

    if(result == "") result = "0";
    return result;
}


int main(){
    string str1, str2;
    while(cin>>str1>>str2){
        cout<<multi(str1,str2)<<endl;
    }
    return 0;
}