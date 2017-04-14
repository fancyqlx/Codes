#include <string>
#include <set>
#include "Folder.h"
#include "Message.h"
using namespace std;

void Folder::add_Msg(Message * Msg){
    messages.insert(Msg);
}

void Folder::delete_Msg(Message * Msg){
    messages.erase(Msg);
}

size_t Folder::get_size(){
    return messages.size();
}