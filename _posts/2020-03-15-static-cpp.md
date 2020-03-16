---
type: post
date: 2020-03-15
title: "static keyword in C++"
---

Modified from [here](https://www.geeksforgeeks.org/static-keyword-cpp/).

## Static variables in functions

If a variable is declared "static", space for it gets allocated for the lifetime of the program. Even if the function is called multiple times, space for the static variable is allocated only once, and the value of variable in the previous call is carried over to the next function call.

Useful when the previous state of function must be stored.

```c++
void demo() {
  static int count = 0;
  std::cout << count << "\n";
  count++;
}

int main() {
  for (int i = 0; i < 5; i++) {
    demo();
  }

  return 0;
}
```
Output of this program is:
```c++
1
2
3
4
5
```
as the value of the static variable `count` is carried through function calls. It does not get re-initialized during each function call.


## Static variables in a class

Variables declared static are initialized only once, as they are allocated space in separate static storage. Thus, static variables in a class are shared by instances of the class. Thus, they cannot be initialized using constructors.

```c++
class Foo {
public:
  static int my_int;
  
  Foo() {}
};

int main() {
  Foo f1;
  Foo f2;
  f1.my_int = 2;
  f2.my_int = 3;
  
  std::cout << "f1: " << f1.my_int << ", f2: "<< f2.my_int << std::endl;
}
```
Unfortunately, the compiler throws an error for the above program.

Instead, the static variable should be initialized by the user using the class, outside the scope of the class.
```c++
class Foo {
public:
  static int my_int;
  
  Foo() {}
};

int Foo::i = 1;

int main() {
  Foo f;
  std::cout << f.my_int << std::endl;
}
```

## Static class objects

If you mark a class object as static, it has scope for the lifetime of the program.

```c++
class Foo {
public:
  Foo() {
    std::cout << "Inside constructor" << std::endl;
  }
  
  ~Foo() {
    std::cout << "Inside destructor" << std::endl;
  }
};

int main() {
  Foo f;

  std::cout << "End of main" << std::endl;
  return 0;
}
```
The output of the non-static `Foo` class is:
```
Inside constructor
Inside destructor
End of main
```

while the output of this static `Foo` class 
```c++
class Foo {
public:
  Foo() {
    std::cout << "Inside constructor" << std::endl;
  }
  
  ~Foo() {
    std::cout << "Inside destructor" << std::endl;
  }
};

int main() {
  static Foo f;

  std::cout << "End of main" << std::endl;
  return 0;
}
```
is
```
Inside Constructor
End of main
Inside Destructor
```
The destructor of the static `Foo` class is invoked after the end of the `main` function, since the `Foo` object is scoped until the end of the program.

## Static functions in a class

Static member functions do not depend on an instance of a class. The recommended way to invoke a static member function is to use the class name, then scope resolution operator:

```c++
class Foo {
public:
  Foo() {}
    
  static void print_message() {
    std::cout << "print me!" << std::endl;
  }
};

int main() {
  Foo::print_message();
}
```


