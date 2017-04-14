objects = main.o Folder.o Message.o

main.exe: $(objects)
	g++ -o main.exe $(objects)

main.o: main.cpp
	g++ -c main.cpp

Folder.o: Folder.cpp
	g++ -c Folder.cpp 

Message.o: Message.cpp
	g++ -c Message.cpp 

.Phony: clean

clean:
	rm main.exe $(objects)
