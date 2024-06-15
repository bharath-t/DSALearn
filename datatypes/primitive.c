#include <stdio.h>   // standar input output - printf, scanf, create, read, write files
#include <stdbool.h> // for bool, _Bool
#include <stdlib.h>  // for argc, argv
#include <string.h>  // strcpy

// int main() is same as int main(void)
int main(int argc, char *argv[])
{
    printf("=====================  stdlib: argc, argv  ==================================\n");
    // check if arguments are passed. argc is atleast 1 (if nothig is passed, default is void, which counts as 1)
    if (argc > 1)
    {
        printf("arg count is %d \n", argc);
        printf("%s \n", argv[0]);
    }

    printf("======================  numeric  =================================\n");
    // numeric: %d, %hd, %ld
    int x = 1;
    short y = 5;
    long z = 1000000L;
    // sizeof returns an object of type size_t: %zu, %lu
    size_t x_size = sizeof(x);
    printf("value of x, y, z are %d, %hd, %ld \n", x, y, z);
    printf("size of int x, short y, long z is %zu, %zu, %zu bytes \n", x_size, sizeof(y), sizeof(z));

    printf("====================  char  ===================================\n");
    // char: %c
    char ch = 'A';
    printf("value of ch is %c \n", ch);
    printf("size of char ch is %zu bytes \n\n", sizeof(ch));

    printf("=======================  float  ================================\n");
    // float, double, long double: %f, %f, %Ld
    // by default %f only returns few digits. use %.nf or %.nLd where n is number of digits after decimal
    float f = 3.14f;
    double d = 3.141592653589793;
    long double ld = 3.14159265358979323846L;
    printf("value of f, d, ld are %f, %.10f, %.15Lf \n", f, d, ld);
    printf("size of float f, double d, long double ld is %zu, %zu, %zu bytes \n", sizeof(f), sizeof(d), sizeof(ld));

    printf("=======================  boolean  ================================\n");
    // boolean: %d or %s (for %s, use ternary operator ?, :)
    _Bool flag = 1; // true
    bool flag2 = false;
    printf("value of f, d, ld are %d, %s, %d \n", flag, flag2 ? "true" : "false", flag2);
    printf("size of _Bool, bool ld is %zu, %zu bytes \n", sizeof(flag), sizeof(flag2));

    printf("=====================  array  ==================================\n");
    // array: we define type of element, number of elements
    // define either size or values or both.
    // int num[]; is invalid because we did not specify size
    // int num[] = {1,2,3} is valid. len is automatically determined by c
    int numbers[3] = {1, 2, 3};
    char str[3] = {'a', 'b', 'c'};
    _Bool bol[3] = {1, 0, 1};
    printf("size of numbers, str, bol is %zu, %zu, %zu bytes \n", sizeof(numbers), sizeof(str), sizeof(bol));

    printf("====================  string  ===================================\n");
    // string: %s. string is a character array with last character as "/0" (null terminator).
    char str1[] = "hello";  // no issue. c will determine the size: num characters + 1 (null terminator)
    char str2[6] = "world"; // add 1 extra space for terminator. else it will cause problems. check readme.md point 6.
    printf("%s \n", str1);
    printf("%s \n", str2);
    printf("size of str1, str2 is %zu, %zu bytes \n", sizeof(str1), sizeof(str2));

    printf("=====================  enum  ==================================\n");
    // enum: %d. converts stored values to indexes starting from 0.
    // space is used for values during compilation but during runtime it uses int space ie 4 bytes.
    enum Color
    {
        RED,
        GREEN,
        BLUE
    };
    enum Color my_color = BLUE;
    printf("%d \n", my_color);
    printf("%zu \n", sizeof(my_color));
    printf("%zu \n", sizeof(enum Color));

    printf("====================  pointer  ===================================\n");
    // Pointer -> special variable %p, points to the base address of a variable
    int g = 10;
    // to access base address of an element, use &
    printf("address of variable g is %p \n", &g);

    int *ptr; // same as int *ptr = NULL; ptr is pointing pointing to null
    printf("pointer address value before assignment is %p \n", ptr);
    printf("pointer address value in int after assignment is %d \n", ptr);

    // we can not use *ptr here and get value null. we can only use *ptr once it is pointing to something valid

    ptr = &g; // assign address of g to ptr variable
    printf("value at pointers address is : %d \n", *ptr);
    // printing address in int will throw a warning but is easy to visualize.

    // pointer type %p is of type (void *) ie pointer to void.
    // in an array, elements are stored continuously. we can verify by printing address of elements in array
    // as the array was of int elements, their addresses should defer by 4 bytes
    printf("address location of array numbers is %d, %d, %d \n", (void *)&numbers[0], &numbers[1], &numbers[2]);

    printf("====================  void, null  ===================================\n");
    // void -> pointer to nothing, null -> undefined
    void *ptr2 = NULL; // Pointer to an unspecified type. can point to anything.
    ptr2 = numbers;
    printf("address location of ptr2 is %d \n", ptr2);
    // this should be same as address of first element in numbers array

    printf("=====================  struct  ==================================\n");
    // struct (class with no methods)
    struct Point
    {
        int x;
        char y;
        long z;
    };
    // similar to array, struct is contigous memory bloc. major diff is struct can store multiple datatypes
    // each element is accessed via offset. for base element, offset is 0, for second element, offset is 1, ....
    // array accesses element by index. struct does it by offset
    struct Point p1 = {10, 'a', 11};

    struct Point p2;
    p2.x = 30;
    p2.y = 'b';
    p2.z = 40;

    printf("size of p1 is %zu \n", sizeof(p1));
    // this may not be what we expect (4 + 1 + 8).
    // C add's padding to smaller elements, size will be more than what we expect
    printf("address location of p1.x, p1.y, p1.z is %d, %d, %d \n", &p1.x, &p1.y, &p1.z);

    printf("=====================  union  ==================================\n");
    // union (struct with only one active variable)
    // unlike struct which uses more memory, union size is size of variable with max space
    union Data
    {
        int i;
        float f;
        char str[5];
    };

    union Data data;
    data.i = 12;
    printf("size of union data is %zu \n", sizeof(data));

    data.f = 12;
    printf("size of union data is %zu \n", sizeof(data));

    // data.str = "abc"; // strings can not be directly assigned. they should be copied
    strcpy(data.str, "abc");
    printf("size of union data is %zu \n", sizeof(data));
    printf("value of union str is %s \n", data.str);

    // below will give random value as it is overwritten when f, str is assigned
    printf("value of union int is %d \n", data.i);

    printf("====================  typedef  ===================================\n");
    // typedef : to change/ create a custom datatype
    // usage "typedef curr_datatype new_datatype"

    // 1. create a custom datatype byte
    typedef unsigned char byte;
    byte b = 'A';

    // 2. create a new datatype using struct
    typedef struct Point new_point;
    new_point a; // instead of "struct Point a"
    a.x = 100;
    a.y = 'c';
    a.z = 1;
    printf("value of struct int is %d \n", a.x);
    printf("=======================================================\n");

    return 0;
}
