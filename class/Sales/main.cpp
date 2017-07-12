#include "Sales_item.h"
#include "Item_base.h"
#include "Bulk_item.h"

#include <iostream>

using namespace std;

int a(){
    cout<<"a"<<endl;
}

int a(int num){
    cout<<"a:"<<num<<endl;
}

int main(){
    Sales_item item;
    Item_base base;
    Bulk_item bulk;
    Bulk_item bulk2;
    bulk.print_price(bulk2);
    a();
    a(10);
    return 0;
}