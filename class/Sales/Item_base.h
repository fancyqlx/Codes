#ifndef ITEM_BASE_H
#define ITEM_BASE_H

#include <string>
using namespace std;

class Item_base{
    public:
        Item_base(const string &book = "",
                double sales_price = 0):
                isbn(book),price(sales_price){}
        string book() const {return isbn;}
        virtual double net_price(size_t n)const{
            return n*price;
        }
        virtual ~Item_base(){}
    private:
        string isbn;
    protected:
        double price;
};
#endif