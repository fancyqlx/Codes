#include "Sales_item.h"
#include <string>
using namespace std;

double Sales_item::avg_price()const{
    if(units_sold)
        return revenue/units_sold;
    else
        return 0;
}

bool Sales_item::same_isbn(const Sales_item & rhs) const{
    return isbn==rhs.isbn;
}