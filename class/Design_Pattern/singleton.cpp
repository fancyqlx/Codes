#include <iostream>
#include <mutex>

using namespace std;

class Singleton{
    private:
        static Singleton * singleton;
        static mutex mut;
        Singleton (){
            cout<<"Create a singleton!"<<endl;
        }
    public:
        static Singleton * createSingleton(){
            if(singleton==nullptr){
                mut.lock();
                if(singleton==nullptr)
                    singleton = new Singleton();
                mut.unlock();
            }
            return singleton;
        }
};

Singleton * Singleton::singleton = nullptr;
mutex Singleton::mut;

int main(){
    for(int i=0;i<10;++i)
        auto x = Singleton::createSingleton();
    return 0;
}