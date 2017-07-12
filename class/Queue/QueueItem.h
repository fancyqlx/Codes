#ifndef QUEUEITEM_H
#define QUEUEITEM_H

template<class Type> class Queue;
template <class Type> class QueueItem{
    friend class Queue<Type>;
    QueueItem(const Type &t):item(t),next(0){}
    Type item;
    QueueItem * next;
};
#endif