int main()
{
  double area = 3.14 * 4 * 4;
  // It prints the area
  // of a circle of radius = 4
  print('area is $area');
 
return 0;
}

// comment format

/* first comment line
 * next comment line
 * last comment line
 */

// ---------------------------------------

void main(){
    int n = 10;
    print(n);
    
    double d = 10.5;
    print(d);
    
    bool b = true;
    print(b);
    
    String s = 'baraa dawalibi';
    print(s);
    
    var v = 50.2;
    print(v);
    
    dynamic ood = 'men';
    print(ood);
    ood = 1500;
    print(ood);
  
    // final end = 'const value';
    final String end = 'const value';
    print(end);
    
    // const c = 50;
    const int c = 50;
    print(c);
}

// ---------------------------------------

void main()
{
  var lst = [1, 2, 3];
  /*
  It prints
  the whole list
  at once
  */
  print(lst);
  print(lst[0]);
   }

// ---------------------------------------

int main()
{
  int n = 43;
  print(checkEven(n));
  return 0;
}

bool checkEven(n){
  /// Returns true
  /// if n is even
  if(n%2==0)
 
      return true;
  /// Returns false if n is odd
  else
 
      return false; }
 
// ---------------------------------------

// Dart program to show the single inheritance

// Creating parent class
class Parent{
	
// Creating a function
void output(){
	print("Welcome to gfg!!\nYou are inside output function.");
}
}

// Creating Child class
class Child extends Parent{
// We are not defining
// any thing inside it...
}
void main() {
// Creating object of GfgChild class
var obj = new Child();
	
// Calling function
// inside Gfg(Parent class)
obj.output();
}

// ---------------------------------------

// Dart program for multilevel interitance

// Creating parent class
class Grand{
	
// Creating a function
void output1(){
	print("Welcome to gfg!!\nYou are inside the output function of Gfg class.");
}
}

// Creating Child1 class
class Parent extends Grand{
	
// Creating a function
void output2(){
	print("Welcome to gfg!!\nYou are inside the output function of GfgChild1 class.");
}
}

// Creating Child2 class
class Child extends Parent{
// We are not defining
// any thing inside it...
}

void main() {
// Creating object
// of GfgChild class
var obj = new Child();
	
// Calling function
// inside Gfg
//(Parent class of Parent class)
obj.output1();
	
// Calling function
// inside GfgChild
// (Parent class)
obj.output2();
}

// ---------------------------------------

// Dart program for Hierarchical inheritance

// Creating parent class
class Parent{
	
// Creating a function
void output(){
	print("Welcome to gfg!!\nYou are inside output function of Gfg class.");
}
}

// Creating Child1 class
class Child1 extends Parent{
// We are not defining
// any thing inside it...
}

// Creating Child2 class
class Child2 extends Gfg{
	
// We are not defining
// any thing inside it...
}

void main() {
// Creating object
// of GfgChild1 class
var obj1 = new Child1();
	
// Calling function
// inside Gfg(Parent class)
obj1.output();
	
// Creating object of
// GfgChild1 class
var obj2 = new Child2();
	
// Calling function
// inside Gfg(Parent class)
obj2.output();
}

// ---------------------------------------

class Man {
	var name;
	var age;

	void sett(x, y)
	{
		this.name = x;
		this.age = y;
	}

	void add()
	{
		var info = this.name + this.age;
		print(info);
	}
}

void main()
{
	// Creating objects of class GFG
	Man obj1 = new Man();
	Man obj2 = new Man();

	// Without using Cascade Notation
	obj1.sett('bara ', ' 32');
	obj1.add();

	// Using Cascade Notation
	obj2.sett('marah ', ' 13');
	obj2.add();
}

// ---------------------------------------
