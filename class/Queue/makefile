Obj = main.o Queue.o 

main: $(Obj)
	g++ $(Obj) -o main

$(Obj): QueueItem.h Queue.h

.PHONY: clean

clean:
	-rm $(Obj) main