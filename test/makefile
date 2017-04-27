Obj = test.1.o test.o 

main.exe: $(Obj)
	g++ -o main.exe $(Obj)

$(Obj):test.1.cpp test.cpp

.PHONY: clean
clean:
	-rm $(Obj) main.exe