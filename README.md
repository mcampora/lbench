# lbench
Quick comparison of language performance derived from a GNU Linux magazine article.
This is basically a bubblesort algorithm applied to an array of integer.

You need support for makefiles and have the various interpreters or compilers pre-installed, check Makefile.
The bench compares C (compiled with various options), Java, Go, Node.js, Pypy and Python.

to launch the bench:
>make b2
bin/CTest execute en 0.0051s
bin/CTestO execute en 0.0021s
bin/CTestO3 execute en 0.0021s
bin/CTestO3m execute en 0.0020s
java -cp bin JTest execute en 0.0016s
bin/GTest execute en 0.0033s
pypy3 src/PTest.py execute en 0.0049s
node src/JSTest.js execute en 0.0073s
python3 src/PTest.py execute en 0.1624s

PS: "make b1" is launching the test as designed originally in the article I mention. Unfortunately this is giving too much importance to the launch of the process (launched for every single iteration), if your goal is to measure the performance of a server-side application which stays up and process millions of requests the measure is clearly not relevant.
