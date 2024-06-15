# Source: ChatGPT

This doc shows step by step process of how a machine understands and executes python code.

1. hello.py:

```python
print('hello.py')
```

2. execute:

```
python -m hello.py
```

PVM - python vitrual machine compiles .py to .pyc and executes python bite code instrunction directly.
.pyc is created inside **pycache** directory.
these instructions are in arduino. to explicitly compile, use:

```
python -m py_compile hello.py
```

contents of complied .pyc file will look like:

```arduino
LOAD_CONST  'Hello, World!'
PRINT_ITEM
PRINT_NEWLINE
```
