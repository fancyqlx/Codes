#ifndef SALESITEM_H
#define SALESITEM_H
#include <string>
using namespace std;

class Sales_item{
    public:
        Sales_item():units_sold(0), revenue(0){};
        double avg_price() const;
        bool same_isbn(const Sales_item & rhs) const;
    private:
        string isbn;
        unsigned units_sold;
        double revenue;
};
#endif