#ifndef QUEUE_CPP
#define QUEUE_CPP

#include "QueueItem.h"
#include "Queue.h"

template <class T> void Queue<T>::destroy(){
    while(!empty()) pop();
}

template <class T> void Queue<T>::pop(){
    QueueItem<T> * p = head;
    head = p->next;
    delete p;
}

template <class T> void Queue<T>::push(const T & val){
    QueueItem<T> * pt = new QueueItem<T>(val);
    if(empty()) head = tail = pt;
    else{
        tail->next = pt;
        tail = pt;
    }
}

template <class T> void Queue<T>::copy_elems(const Queue & orig){
    for(QueueItem<T> *pt = orig.head;pt;pt=pt->next){
        push(pt->item);
    }
}

template <class T> Queue<T>& Queue<T>::operator=(const Queue & Q){
    if(this != &Q){
        destroy();
        copy_elems(Q);
    }
    return *this;
}

#endif