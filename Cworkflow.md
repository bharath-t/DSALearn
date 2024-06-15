# Source: ChatGPT

# Compilation Steps and Intermediate Files

This doc shows step by step process of how a machine understands and executes c code.

1: hello.c file created by us.

```
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

2. Preprocessing (hello.c → hello.i):

```bash
gcc -E hello.c -o hello.i
```

Content of hello.i (after preprocessing. also a c file):

```c
# 1 "hello.c"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "hello.c"
# 1 "/usr/include/stdio.h" 1 3 4
# 27 "/usr/include/stdio.h" 3 4
# 1 "/usr/include/features.h" 1 3 4
# 396 "/usr/include/features.h" 3 4
# 1 "/usr/include/sys/cdefs.h" 1 3 4
...
// Contents of stdio.h included here
...
# 10 "hello.c" 2
// Contents of hello.c after preprocessing
# 1 "/usr/include/stdio.h" 1 3 4
# 27 "/usr/include/stdio.h" 3 4
# 1 "/usr/include/features.h" 1 3 4
# 396 "/usr/include/features.h" 3 4
# 1 "/usr/include/sys/cdefs.h" 1 3 4
...
// Contents of stdio.h included here
...
int main() {
    printf("Hello, World!\n");
    return 0;
}
```

Explanation: hello.i contains the contents of hello.c after preprocessing, including the contents of the included <stdio.h> header.

3. Compilation (hello.i → hello.s):

```bash
gcc -S hello.i -o hello.s
```

Content of hello.s (assembly code):

```assembly
.file "hello.c"
.section .rodata
.LC0:
    .string "Hello, World!"
.text
.globl main
.type main, @function
main:
    pushq %rbp
    movq %rsp, %rbp
    leaq .LC0(%rip), %rdi
    call printf
    movl $0, %eax
    popq %rbp
    ret
```

Explanation: hello.s contains assembly language code (x86-64 architecture in this example) generated from hello.i. It includes instructions to print "Hello, World!" using printf.

4. Assembly (hello.s → hello.o):

```bash
gcc -c hello.s -o hello.o
```

Content of hello.o (object file):
hello.o is a binary file containing machine code specific to the target architecture (x86-64 in this case). It's not readable as text, but it encapsulates the compiled instructions from hello.s.

5. Linking (hello.o + libraries → hello):

```bash
gcc hello.o -o hello
```

Explanation: The linker (ld) combines hello.o with necessary libraries (like libc) to produce the final executable hello.

6. Final Executable (hello)
   Running the executable:

```bash
./hello
```

Summary
.c File: Source code written in C (hello.c).
.i File: Preprocessed source code (hello.i) after expanding macros and #include directives.
.s File: Assembly code (hello.s) generated from the preprocessed C code.
.o File: Object file (hello.o) containing machine code specific to the target architecture.

Final Executable: Linked executable (hello) ready to be executed, which prints "Hello, World!" to the console.
Understanding these intermediate files and the compilation process helps in debugging, optimizing, and gaining insights into how C programs are transformed from source code to executable binaries.
