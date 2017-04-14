#include <iostream>
#include <string>
#include "Message.h"
#include "Folder.h"
using namespace std;

int main(){
    Message msg_1("1");
    Message msg_2("2");
    Folder folder;
    msg_1.save(folder);
    msg_2.save(folder);
    Message msg_3(msg_1);
    Message msg_4("3");
    msg_4 = msg_3;
    msg_3.remove(folder);
    cout<<folder.get_size()<<endl;
    return 0;
}