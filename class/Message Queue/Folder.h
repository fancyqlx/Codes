#ifndef FOLDER_H
#define FOLDER_H
#include <iostream>
#include <set>
using namespace std;

class Message;

class Folder{
    public:
        void add_Msg(Message *);
        void delete_Msg(Message *);
        size_t get_size();
    private:
        set<Message *> messages;
};
#endif