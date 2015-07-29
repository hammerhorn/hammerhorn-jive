all: simple_2d6 simple_2d6++ dice.jar die6x2.jar drawDie.jar
	rm -f *.class
	mv *.java ./src/
	
simple_2d6: src/simple_2d6.c
	gcc -O2 src/simple_2d6.c -o simple_2d6

simple_2d6++: src/simple_2d6.cpp
	g++ -O2 src/simple_2d6.cpp -o simple_2d6++

dice.jar: dice.class src/dice.MF Die.class Keyboard.class MyOpts.class TuiTeX.class Thing.class
	jar cvmf src/dice.MF dice.jar dice.class Die.class Keyboard.class MyOpts.class TuiTeX.class Thing.class
	chmod +x dice.jar
	
die6x2.jar: die6x2.class src/die6x2.MF Keyboard.class Die.class MyOpts.class Thing.class TuiTeX.class TwoD6.class
	jar cvmf src/die6x2.MF die6x2.jar die6x2.class Keyboard.class Die.class MyOpts.class Thing.class TuiTeX.class TwoD6.class
	chmod +x die6x2.jar
	
drawDie.jar: drawDie.class src/drawDie.MF Die.class Keyboard.class MyOpts.class Thing.class TuiTeX.class
	jar cvmf src/drawDie.MF drawDie.jar drawDie.class Die.class Keyboard.class MyOpts.class Thing.class TuiTeX.class
	chmod +x drawDie.jar

dice.class: dice.java MyOpts.java Keyboard.java
	javac dice.java
	
drawDie.class: drawDie.java
	javac drawDie.java

die6x2.class: die6x2.java
	javac die6x2.java

TwoD6.class: TwoD6.java
	javac TwoD6.java

Thing.class: Thing.java
	javac Thing.java

Die.class: Die.java
	javac Die.java

Keyboard.class: Keyboard.java
	javac Keyboard.java

MyOpts.class: MyOpts.java Keyboard.java
	javac MyOpts.java

TuiTeX.class: TuiTeX.java
	javac TuiTeX.java