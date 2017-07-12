#ifndef BULK_ITEM_H
#define BULK_ITEM_H

#include <string>
#include "Item_base.h"
using namespace std;

class Bulk_item: public Item_base{
    public:
        Bulk_item():min_qty(0),discount(0){}
        Bulk_item(const string& book, double sales_price,
                    size_t qty = 0, double disc_rate = 0):
                    Item_base(book,sales_price),min_qty(qty),
                    discount(disc_rate){}
        double net_price(size_t) const;
        void print_price(Bulk_item &);
    private:
        size_t min_qty;
        double discount;
};
#endif