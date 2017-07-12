#include "Bulk_item.h"
#include <iostream>
using namespace std;

double Bulk_item::net_price(size_t cnt) const{
    if(cnt>=min_qty){
        return cnt*(1-discount)*price;
    }
    else{
        return cnt*price;
    }
}

void Bulk_item::print_price(Bulk_item &a){
    cout<<price<<endl;
    cout<<a.price<<endl;
}