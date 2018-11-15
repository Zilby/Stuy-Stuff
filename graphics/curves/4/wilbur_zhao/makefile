OBJECTS: Parser.class Matrix.class EdgeMatrix.class Frame.class test.class CurveScript.class

all: $(OBJECTS)

Parser.class: Parser.java EdgeMatrix.java Matrix.java Frame.java
	javac Parser.java

Matrix.class: Matrix.java
	javac Matrix.java

EdgeMatrix.class: Matrix.java EdgeMatrix.java
	javac EdgeMatrix.java

Frame.class: Frame.java EdgeMatrix.java
	javac Frame.java

test.class: test.java Frame.java Matrix.java EdgeMatrix.java Parser.java
	javac test.java

CurveScript.class: CurveScript.java
	javac CurveScript.java

run: test.class
	java CurveScript
	java test

clean:
	rm *~ *.class