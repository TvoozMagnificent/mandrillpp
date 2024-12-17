
# _mandrill++_

_mandrill++_ is a Python re-implementation of _mandrill_, introducing many more _exciting_ features. 

## Usage

_mandrill++_ can simply be directly executed from source, and doesn't require any libraries. 

```
python main.py program.man
```
will execute `program.man` as a _mandrill++_ file. 

## _mandrill_ and _mandrill++_

_mandrill++_ is a re-implementation of _mandrill_, supporting more features, adding game-changing syntax, 
and allowing for less redundant grammar. Any _mandrill_ program that does not use raw characters as comments
can be run in _mandrill++_. 

## Grammar

### Variables

Variables in _mandrill++_ are identifiers other than the keywords `if`, `while`, and `else`. 
Using these keywords as variables constitute UB. Identifiers can be made of lowercase letters and underscores,
for instance `var`, `myvar`, `my_var`, `_var_`, `_`, etc. 

Variables have no types in _mandrill++_. They can hold integers, characters, and booleans, but they are all represented
internally with integers by using their value, Unicode value, and 0 and 1. 

Variables do not need to be declared and are automatically initialized to 0. For instance, `a = a + 1; ` sets `a` to 1
if `a` was not already initialized. 

`read`, `write`, `get`, and `put` are special variables that serve the purpose of I/O. When evaluating, `read`
evaluates to the next integer in input stream, and `get` evaluates to the next non-whitespace character in the input stream. 
There is no way to differentiate the input streams

```
1
2
```

and

```
1 2
```

in _mandrill++_. When assigning, `write` and `put` redirects the assignment to the output stream, where `write` interprets
the value as an integer and `put` interprets the value as a character. 

It is possible to assign to `read` and `get`, but it is impossible to fetch these assigned values. Similarly, 
it is possible to evaluate to `write` and `put` (which defaults to 0), but it is impossible to assign to them. 

For instance, `write = read + read; ` solves the A+B problem, and `write = 43; put = 32; write = 21; put = 10; ` prints

```
43 21
```

with a newline at the end. 

`read`, `write`, `get`, and `put` can be used as array references. 


