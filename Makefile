# notes
# installed python3.4.2 in /usr/local/bin
# used XTool gcc -> Apple LLVM version 6.0 (clang-600.0.56) (based on LLVM 3.5svn)
# installed java 1.8.0_25-b17 in /usr/bin
# installed go 1.4 in /usr/local/go
# installed node in /usr/local/bin/node

SRC=src
BIN=bin

all: $(BIN)/CTest $(BIN)/CTestO $(BIN)/GTest $(BIN)/JTest.class

# c program
$(BIN)/CTest: $(SRC)/CTest.c
	gcc $(SRC)/CTest.c -o $(BIN)/CTest
$(BIN)/CTestO: $(SRC)/CTest.c
	gcc $(SRC)/CTest.c -O -o $(BIN)/CTestO

# java program
$(BIN)/JTest.class: $(SRC)/JTest.java
	javac -d $(BIN) $(SRC)/JTest.java

# go program
$(BIN)/GTest: $(SRC)/GTest.go
	go build -o $(BIN)/GTest $(SRC)/GTest.go

clean:
	rm $(BIN)/CTest $(BIN)/CTestO $(BIN)/JTest.class $(BIN)/GTest

# bench, the process is launched 1000 times
b1:
	@bench $(BIN)/CTest
	@bench $(BIN)/CTestO
	@bench "java -cp $(BIN) JTest"
	@bench $(BIN)/GTest
	@bench "python3 $(SRC)/PTest.py"
	@bench "pypy3 $(SRC)/PTest.py"

# bench 2, the process is launched once and runs the algorithm 1000 times
b2:
	@bench2 $(BIN)/CTest
	@bench2 $(BIN)/CTestO
	@bench2 "java -cp $(BIN) JTest"
	@bench2 $(BIN)/GTest
	@bench2 "python3 $(SRC)/PTest.py"
	@bench2 "pypy3 $(SRC)/PTest.py"
