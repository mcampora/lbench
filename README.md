# lbench
Quick comparison of language performance derived from a GNU Linux magazine article.
This is basically a bubblesort algorithm applied to an array of integer.

You need support for makefiles and have the various interpreters or compilers pre-installed, check Makefile.
The bench compares C (compiled with various options), Java, Go, Node.js, Pypy and Python.

to launch the bench:
>\>make b2<br/>
bin/CTest execute en 0.0051s<br/>
bin/CTestO execute en 0.0021s<br/>
bin/CTestO3 execute en 0.0021s<br/>
bin/CTestO3m execute en 0.0020s<br/>
java -cp bin JTest execute en 0.0016s<br/>
bin/GTest execute en 0.0033s<br/>
pypy3 src/PTest.py execute en 0.0049s<br/>
node src/JSTest.js execute en 0.0073s<br/>
python3 src/PTest.py execute en 0.1624s<br/>

PS: "make b1" is launching the test as designed originally in the article I mention. Unfortunately this is giving too much importance to the launch of the process (launched for every single iteration), if your goal is to measure the performance of a server-side application which stays up and process millions of requests the measure is clearly not relevant.
