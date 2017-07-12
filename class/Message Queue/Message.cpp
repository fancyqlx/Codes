#include <iostream>
#include <string>
#include <set>
#include "Message.h"
#include "Folder.h"
using namespace std;

Message::Message(const Message & Msg):
    contents(Msg.contents), folders(Msg.folders){
        put_Msg_in_Folders(folders);
}

Message& Message::operator=(const Message & Msg){
    if(this != &Msg){
        remove_Msg_from_Folders();
        contents = Msg.contents;
        folders = Msg.folders;
        put_Msg_in_Folders(Msg.folders);
    }
    return *this;
}

Message::~Message(){
    remove_Msg_from_Folders();
}

void Message::save(Folder & f){
    f.add_Msg(this);
    folders.insert(&f);
}

void Message::remove(Folder & f){
    f.delete_Msg(this);
    folders.erase(&f);
}

void Message::put_Msg_in_Folders(const set<Folder*> &s){
    for(set<Folder*>::iterator it = s.begin();it!=s.end();++it){
        (*it)->add_Msg(this);
    }
}

void Message::remove_Msg_from_Folders(){
    for(set<Folder*>::iterator it = folders.begin();it!=folders.end();++it){
        (*it)->delete_Msg(this);
    }
}