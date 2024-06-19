# DSALearn

basic datatypes will be done in c. this gives more clarity. Checkout other .md files for more fun.
data structures, algorithms will be implemented using python.

## to execute C files,

1. main is always a must. return type is always int. most os consider 0 as true/ successful execution. by default, argument for main is void.

2. compile, grant executable permissions to file and execute:

```
gcc program.c -o file && ./program
```

## Datatypes: defines what type of data.

3. memory is alloted in terms of bytes (8 bits). each character/value is represented as binary (bits) + data type
4. when we define a variable, it returns the pointer to the memory location of that variable
5. Array is a contigous block of memory. using (starting pointer address + (n X size of element)), we can directly access the address of nth element. eg: starting address + 5 X 4 gives pointer of 6th element in array of integers. (int size is 4 bytes)

6. BE CAREFUL WITH STRINGS

   string: %s. string is a character array with last character as "/0" (null terminator).
   its better not to define size when declaring string. allot size+1 or dont define size, let c determine

   Danger: if below str2 is defined as str2[5] or less, instead of str2[6] which includes "/0" terminator,
   it behaves weirdly. str2 gets access to some other memory.
   when you print it, its size will be greater than what we defined.
   if str2 is modified, if other memory is some system file, it may mess up our system. Read C memory overflow.

```
    char str1[] = "hello";
    char str2[6] = "world";
    printf("%s \n", str1);
    printf("%s \n", str2);
```

## Python vs C:

7. C is compiled and executed. Python is directly executed by PVM.

8. Was thinking when we implement a node in python, does the next variable store entire node object or just the pointer like in C. Turns out python uses reference semantics so its all good.
   Eg:

```
int x = 10;
int y = x;
// C: this copies value of x into y
```

```
x = 10
y = x
// Python: no copy. y is now pointing to same address of x. dont have to handle pointers in python.
// This is known as reference semantics, which is different from value semantics found in languages like C.
```

9. Python datatypes that also exist in C ARE NOT THE SAME.
   Eg:
   - int in C, many other languages is 4 bytes. python int does not have any such limitation.
   - C has static and dynamic arrays. Python lists are always dynamic.
     (Forget about optimising space in python)

## DataStructures: how data is stored. useful for effecient storage, retrieval.

array, linked list, hashmap, hastable, queue, stack, tree, trie, heap, priority queue, maps, graphs, disjoint sets

## Algorithms: Efficient way to do things (search, sort, path finding, dynamic programming..)

## Source:

1. https://frontendmasters.com/courses/algorithms/trees-overview/
2. https://www.youtube.com/watch?v=qp8u-frRAnU&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&ab_channel=codebasics
3. ChatGPT - To understand low level details of C
