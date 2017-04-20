#ifndef MESSAGE_H
#define MESSAGE_H

#include <iostream>
#include <string>
#include <set>
#include "Folder.h"
using namespace std;

class Message{
    public:
        Message(const string &str = ""):contents(str){}
        Message(const Message &);
        Message & operator=(const Message &);
        ~Message();
        void save(Folder &);
        void remove(Folder &);
    private:
        string contents;
        set<Folder *> folders;
        void put_Msg_in_Folders(const set<Folder *> &);
        void remove_Msg_from_Folders();
};
#endif