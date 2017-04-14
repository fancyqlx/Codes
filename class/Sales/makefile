objects = main.o Item_base.o Bulk_item.o Sales_item.o

main.exe: $(objects)
	g++ -o main.exe $(objects)

main.o: main.cpp
	g++ -c main.cpp

Item_base.o: Item_base.cpp
	g++ -c Item_base.cpp

Bulk_item.o: Bulk_item.cpp
	g++ -c Bulk_item.cpp 

Sales_item.o: Sales_item.cpp
	g++ -c Sales_item.cpp
 
.Phony: clean

clean:
	rm main.exe $(objects)
