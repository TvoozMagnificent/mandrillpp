
# _mandrill++_

_mandrill++_ is a Python re-implementation of _mandrill_, introducing many more _exciting_ features. 

## Usage

_mandrill++_ can simply be directly executed from source, and doesn't require any libraries. 

```
python main.py program.man
```
will execute `program.man` as a _mandrill++_ file. 

## Grammar

### Differences

The changes in _mandrill++_ as compared to _mandrill_ are:
- Allowing the use of underscores is variable names.
- Adding syntactic sugar like `+=` and `++` that makes writing programs less painful.
- Adding the boolean operators and the ternary operator.
- Depreciating ambiguous grammar associated with chained comparison operators.
- Allowing some syntactic simplifications in `if` and `while` constructs.
- Adding array references.
- Adding procedures. 

### Comments

Comments are deliminated by `\` signs. 

### Variables

Variables in _mandrill++_ are identifiers other than the keywords `if`, `while`, and `else`. 
Using these keywords as variables constitute UB. Identifiers can be made of lowercase letters and underscores,
for instance `var`, `myvar`, `my_var`, `_var_`, `_`, etc. 

Variables have no types in _mandrill++_. They can hold integers, characters, and booleans, but they are all represented
internally with integers by using their value, Unicode value, and 0 and 1. 

Variables are all global and not scoped. 

Variables do not need to be declared and are automatically initialized to 0. For instance, `a = a + 1; ` sets `a` to 1
if `a` was not already initialized. 

We support `+=`, `-=`, `*=`, `/=`, and `%=` syntax, and also support `++` and `--` syntax. For instance, 
`a++; ` sets `a` to 1 if `a` was not already initialized. 

### I/O

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

### Operations

_mandrill++_ supports basic arithmetic operators, comparisons, boolean operators, and the ternary operator, in decreasing order of operation. 

The basic binary arithmetic operators are:
- `+` for addition,
- `-` for subtraction,
- `*` for multiplication,
- `/` for integer division,
- `%` for integer modulo.

The implementations of these operators use the inbuilt Python operators `+`, `-`, `*`, `//` (not `/`), and `%`. 
Notably, the unary operators `+` and `-`, the exponentiation operator `**`, and the bitwise operators are not supported. 
The order of operations are standard. 

The comparison operators are `<`, `>`, `<=`, `>=`, `==`, `!=`, implemented using inbuilt Python operators. These operators
return `1` if the comparison holds, and `0` otherwise. Multiple comparison operators together are not implicitly permitted; that is,
`0 < 1 < 2` will error. One can substitute in either `(0 < 1) < 2` explicitly or `0 < 1 && 1 < 2` following the Python convention. 
The reason we disallow these statements is due to the likelihood of misuse and the indetectible nature of this kind of logic error
in our non-typed environment. 

The boolean operators are `&&`, `||`, and `!`. These operators are logical operators, and do not have control flow abilities. 
For instance, `2 > 1 || 1 / 0 > 0` will error. Unlike Python, they always return `1` or `0`, regardless of the inputs
(which zero denotes false and non-zero denotes true). The order of operations are standard. 

The ternary operator is `? :`. This operator is another logical operator and does not have control flow abilities. 

### Control Flow

Other than procedures, _mandrill++_ supports `if` constructs and `while` constructs. 

`if` constructs have the following syntax: 

```
if (condition) statement;
```

or

```
if (condition) {
  statements;
  statements;
}
```

Optionally, they can be followed by an `else` construct (either `else statement; ` or `else { statements; statements; }`). 
This syntax implicitly allows for `else if` constructs. 

`while` constructs have the following syntax:

```
while (condition) statement;
```

or

```
while (consition) {
  statements;
  statements;
}
```

_mandrill++_ does not support `continue` or `break` constructs, and does not have `else` statements after `while` constructs. 

### Procedures

A procedure can be defined by

```
PROCEDURE_NAME : statement;
```

or

```
PROCEDURE_NAME : {
  statements;
  statements;
}
```

The procedure name must be composed of capital letters and underscores, and cannot start with an underscore. 

Procedures can be called with `PROCEDURE_NAME; `. 

By default, blocks of statements not wrapped in a procedure is stored in the `MAIN` procedure, which is executed. 

Procedures must be defined on previous procedures. `A : A; ` and `A : B; ` are not valid definitions. 
`A : {}` is a valid procedure definition, and so is `A : {}  A : A; `. Procedures can override. 

An extreme case is this: 

```
a++;
b++;

A : {
  MAIN;
  MAIN;
}

B : A;

MAIN : {
  A;
  B;
}
```

Here, `MAIN` is first set to the procedure `a++; b++; `. Then, `A` is set to the procedure `a++; b++; a++; b++; `. `B` is set to the same. 
Finally, `MAIN` is overided with a new assignment to `A; B; ` which is `a++; b++; a++; b++; a++; b++; a++; b++; `. The net effect of `MAIN`
is therefore `a += 4; b += 4; `. 

Of course, it should go without saying that writing programs like this are not appreciated. 

### Array References

Something of the form `var @num`, `var @var`, or `var @(expr)` constitutes an array reference. Those references treat `var` as an array,
and denotes item `num`, `var`, or `expr` of that array. We support negative indices like any other normal indices. 
Arrays have infinite length. Internally, `var @3` is represented by the variable `var.3`. These variable aliases are generated on the fly. 

We also support multi-dimensional array references. For instance, if we have `a = 1; b = 2; `, then `x @a @3 @b @(a+b)` would reference
the variable `x.1.3.2.3`. `read`, `write`, `get`, and `put` can be used as array references. 

Variable names, if needed, are calculated after the expression on the right is evaluated. For instance, when executing

```
read @read @read = read @read;
```

where the input stream is `1 2 3 4 5`, 

```
read @2 @3 = read @1; 
```

is executed. Another example is that `a @read ++; ` will execute `a @2 = a @1 + 1; ` if the input stream is `1 2 3 4 5`. 

## Stylelines and Conventions

### Indentations

Indentations should be placed as expected, and is most preferrably two spaces. For instance:

```
\ some fantastic demo class \
DEMO : {
  \ does something completely weird \
  if ( number < 3 ) {
    number++; \ because harry potter is great \
    if ( other < 2 ) other = number; 
    else if ( other < 3 )
      \ do some number sorcery \
      other = number + other + other * number + 123 + heap @index; \ hooray \
    other++; \ because voldemort is great as well \
  }
}
```

### Spacing

The author prefers spacing around both parentheses and braces - see the code segment above. 

When there is only one order of operation, add spaces around both sides like `a + b`, with the only exception being `i++; `. 
It is acceptible to write both `a + b * c + d` and `a + b*c + d`, but not `a+b*c+d` or, even worse, `a+b * c+d`. 

It is customary to add a space before `++` or `--` if what precedes it is a reference and not a variable, like `array @index ++; `. 

We usually add spaces before reference symbols, but never after them.  

### Comments

Comments can serve three purposes: 
1. for documentation, 
2. for commenting, and
3. for commenting out code. 

When documenting code, a block comment should be used as such: 

```
MAIN : {
  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
  heap @i - heap storing all the elements
  end - index of the end of `heap`
  string @i - input string
  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
  ...
}
```

Notice how the number of backslashes in both lines are odd. 

When commenting, we simply use `/ comment yada yada /`, putting spaces on both sides. 
These comments can come after a line, explaining what the line does, or can come before a line,
explaining what the following lines (not line) do. 

Usually, we use lowercase letters for convenience unless necessary. (But we also don't obfuscate purely to avoid uppercase letters.) 

When commenting out code, it is customary to indent the commented code: 

```
i++;
\
  j++;
  k++;
\
```

However, this is not an obligation, especially if it is inconvenient to indent code. 

### Variable Names

Variable names should usually be words ...

