
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
- Adding the unary subtraction operator, boolean operators, and the ternary operator.
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

```
a = 2 > 0;
b = 3 - 2;
c = 'b' - 97;
```
set `a`, `b`, and `c` to 1. 

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

_mandrill++_ supports basic arithmetic operators, unary subtraction, comparisons, boolean operators, and the ternary operator, in decreasing order of operation. 

The basic binary arithmetic operators are:
- `+` for addition,
- `-` for subtraction,
- `*` for multiplication,
- `/` for integer division,
- `%` for integer modulo.

The implementations of these operators use the inbuilt Python operators `+`, `-`, `*`, `//` (not `/`), and `%`. 
Notably, the unary operator `+`, the exponentiation operator `**`, and the bitwise operators are not supported. 
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
MAIN : {
  a++;
  b++;
}

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

Variable names, if needed, are calculated before the expression on the right is evaluated. For instance, when executing

```
read @read @read = read @read;
```

where the input stream is `1 2 3 4 5`, 

```
read @1 @2 = read @3; 
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

Usually, only one statement is present per line. The exceptions are `put = 32; ` and `put = 10; ` to print either a space or a newline. 
These statements can follow an assignment to `write` or `put` directly. 

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

When commenting, we simply use `\ comment yada yada \`, putting spaces on both sides. 
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

Variable names should usually be words, and may be many words concatenated with underscores. 
For instance, `age`, `time`, and `row_number` are great variable names. 

To avoid name collision with keywords or predefined variables, append an underscore at the end. 
For instance, `write_` and `age_` are acceptable. One common use case for this naming convention is
the change of one variable. For instance, in a fibonacci program, we can have

```
current = 1;
next = 1;
while (current < 1000) {
  write = current; put = 32; 
  current_ = next;
  next_ = current + next;
  current = current_;
  next = next_; 
}
put = 10; 
```

which outputs

```
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 
```

A single underscore is sometimes used as a temporary variable, for instance in the snippet:

```
_ = a;
a = b;
b = _; 
```

Some common variable concepts like `time`, `row`, `column`, `change`, `stack`, `queue`, etc. 
can use shorter variable names like `t`, `r`, `c`, `d`, `s`, `q`, etc. Abstract concepts like
`x`, `y`, and `z` also warrant this use. 

### Procedures

Each procedure should not contain more than 10 statements. Avoid writing long code without splitting it into procedures. 

For instance, we can solve Problem 25 of the Guts Estimation Round of the Berkeley Math Competition 2021, which asks for `a` if
`2021^2021 / 2021!` can be expressed as `x1 x2 x3 ... xl . xl+1 xl+2 ... xa y1 y2 ... yb y1 y2 ... yb ...`, that is, the number of
digits not in the repeating decimal places. 

To solve this, we use mathematics for the digits after the decimal point, counting the number of factors of 2 in 2021!. 
We use brute force for the digits before the decimal point by simply calculating the value. 

Without procedures, the code is: 

```
power = 1;
i = 1;
while (i <= 2021) {
  power *= 2021;
  i++;
}
factorial = 1; 
i = 1; 
while (i <= 2021) {
  factorial *= i; 
  i++; 
}
front_digits = 0; 
quotient = power / factorial;
while (quotient) {
  quotient /= 10; 
  front_digits++; 
}
back_digits = 0;
number = 2021;
while (number) {
  number /= 2;
  back_digits += number;
}
write = front_digits + back_digits; put = 10; 
```

Notice how there are clearly four sections of our code: calculating the power, calculating the factorial, 
finding the number of digits in front of the decimal point, and finding the number of digits after the decimal point. 
Therefore, we can reformat our code: 

```
POWER : {
  power = 1;
  i = 1;
  while (i <= 2021) {
    power *= 2021;
    i++;
  }
}

FACTORIAL : {
  factorial = 1; 
  i = 1; 
  while (i <= 2021) {
    factorial *= i; 
    i++; 
  }
}

FRONT_DIGITS : {
  front_digits = 0; 
  quotient = power / factorial;
  while (quotient) {
    quotient /= 10; 
    front_digits++; 
  }
}

BACK_DIGITS : {
  back_digits = 0;
  number = 2021;
  while (number) {
    number /= 2;
    back_digits += number;
  }
}

MAIN : {
  POWER; 
  FACTORIAL;
  FRONT_DIGITS;
  BACK_DIGITS;
  write = front_digits + back_digits; put = 10; 
}
```

## Examples

### Guts Round Estimation. 

We can try to similarly solve Question 27, which asks for the difference between the number of even digits and odd digits
across the numbers from `2^0` to `2^2021`. Here, we use a top-down approach, first sketching out our `MAIN` procedure and then
filling in the details. 

```
MAIN : {
  number = 1; 
  while (count < 2022) {
    SOLVE; 
    number *= 2; 
    count++; 
  }
  write = even - odd; 
}
```

We now implement the `SOLVE` procedure: 

```
SOLVE : {
  \ `RECORD` each digit in `number` \
  copy = number; 
  while (copy) {
    digit = copy % 10; 
    RECORD; 
    copy /= 10; 
  }
}
```

and the `RECORD` procedure:

```
RECORD : {
  \ update `even` and `odd` according to `digit`. \
  if (digit % 2 == 0) even++; 
  else odd++; 
}
```

We can test our implementation by calculating up to `2^4`, which should have the digits `124816`, so the difference is 2. 
Now we crank this up to `2^2021`, and get 1776, the correct answer. Notably, our interpreter will struggle with this and the code
will take quite a while (around 11 seconds). 

It is possible to optimize this approach, storing only the difference, etc. 

```
SOLVE : {
  copy = number; 
  while (copy) {
    difference += 1 - copy % 2 * 2; 
    copy /= 10; 
  }
}

MAIN : {
  number = 1; 
  while (count < 2022) {
    SOLVE; 
    number *= 2; 
    count++; 
  }
  write = difference; put = 10; 
}
```

This version only takes around 7 seconds to run, but it sacrifices readability. 

### A More Complex Problem

> Kailey starts with the number 0, and she has a fair coin with sides labeled 1 and 2. She
> repeatedly flips the coin, and adds the result to her number. She stops when her number is a
> positive perfect square. What is the expected value of Kailey’s number when she stops?

The shortcoming of our programming language is obvious: we can't store decimals implicitly. 
However, realize that the probability of landing on the number `N` is always an integer after we multiply it by `2^N`. 
Therefore, we have our initial probability stored as, say, `2^10000`, and simulate 10000 iterations. 
Here's our `MAIN` function. 

```
MAIN : {
  INIT; \ initialize `probability @0` \
  while (i < 10000) {
    i++;
    probability @i = (probability @(i-1) + probability @(i-2)) / 2;
    CHECK_SQUARE;
    if (return) {
      sum += i * probability @i; 
      probability @i = 0; 
    }
  }
  write = sum * 100000000000000 / probability @0; put = 10; 
}
```

The `INIT` procedure is straighforward enough: 

```
INIT : {
  number = 1; \ for CHECK_SQUARE \
  \ initialize `probability @0` \
  probability @0 = 1;
  while (count < 10000) {
    probability @0 *= 2;
    count++; 
  }
}
```

The `CHECK_SQUARE` procedure would be more painful if the numbers we check aren't in increasing order. 

```
CHECK_SQUARE : {
  \ check whether the square root of i is number \
  if (number * number == i) {
    return = 1;
    number++; 
  } else return = 0; 
}
```

Notice how we conventionally use the variable `return` for return values of procedures. 

The output is `359036568873322`, so our answer is `0.359036568873322`. This agrees with the answer given by the problem-setters. 

In our implementation, we use array references to get the job done. Of course, it is possible to evade them - 
that is left as an exercise to the reader. 

### Conway's Game of Life

To implement Conway's Game of Life, we introduce a new special variable: `random`. Evaluating `random` gives
either 0 or 1 with 1/2 chance. 

Our `MAIN` procedure is now mostly a sketch: 

```
MAIN : {
  INITIALIZE; 
  while (1) ADVANCE;
}
```

Our `INITIALIZE` procedure will take in an integer from the user and use it as the dimensions of the grid. 

```
INITIALIZE : {
  n = read;
  x = 0;
  while (x < n) {
    y = 0;
    while (y < n) {
      grid @x @y = random; 
      y++;
    }
    x++;
  }
}
```

Our `ADVANCE` procedure will have 3 steps: 

```
ADVANCE : {
  COUNT_ALL;
  UPDATE_ALL;
  SHOW_ALL;
}
```

`COUNT_ALL`, `UPDATE_ALL`, `SHOW_ALL` will both just call `COUNT`, `UPDATE`, and `SHOW` over all the cells: 

```
COUNT_ALL : {
  x = 0;
  while (x < n) {
    y = 0;
    while (y < n) {
      COUNT;
      y++;
    }
    x++;
  }
}
```

```
UPDATE_ALL : {
  x = 0;
  while (x < n) {
    y = 0;
    while (y < n) {
      UPDATE;
      y++;
    }
    x++;
  }
}
```

```
SHOW_ALL : {
  put = 10; put = 10; put = 10; put = 10; put = 10; put = 10; put = 10; put = 10; put = 10; put = 10; \ clear \
  x = 0;
  while (x < n) {
    y = 0;
    while (y < n) {
      SHOW;
      y++;
    }
    x++;
    put = 10; \ add newline \
  }
}
```

`COUNT` will simply loop over all the neighbors. Here, we don't use a loop. 

```
COUNT : {
  count @x @y = 0;
  count @x @y += grid @(x+1) @(y+1);
  count @x @y += grid @( x ) @(y+1);
  count @x @y += grid @(x-1) @(y+1);
  count @x @y += grid @(x+1) @( y );
  count @x @y += grid @(x-1) @( y );
  count @x @y += grid @(x+1) @(y-1);
  count @x @y += grid @( x ) @(y-1);
  count @x @y += grid @(x-1) @(y-1);
}
```

`UPDATE` will update the corresponding cell. 

> 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
> 2. Any live cell with two or three live neighbours lives on to the next generation.
> 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
> 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

We can summarize these rules to be that cells are live iff three neighbors are alive or two neighbors are alive and it is originally alive. 
This is the boolean expression `count @x @y == 3 || count @x @y == 2 && grid @x @y`. 

```
UPDATE : grid @x @y = count @x @y == 3 || count @x @y == 2 && grid @x @y; 
```

Finally, the `SHOW` procedure puts `#` if `grid @x @y` is active and `.` otherwise. 

```
SHOW : put = grid @x @y ? '#' : '.'; 
```

Our full code is: 

```
INITIALIZE : {
  n = read;
  x = 0;
  while (x < n) {
    y = 0;
    while (y < n) {
      grid @x @y = random; 
      y++;
    }
    x++;
  }
}

COUNT : {
  count @x @y = 0;
  count @x @y += grid @(x+1) @(y+1);
  count @x @y += grid @( x ) @(y+1);
  count @x @y += grid @(x-1) @(y+1);
  count @x @y += grid @(x+1) @( y );
  count @x @y += grid @(x-1) @( y );
  count @x @y += grid @(x+1) @(y-1);
  count @x @y += grid @( x ) @(y-1);
  count @x @y += grid @(x-1) @(y-1);
}

COUNT_ALL : {
  x = 0;
  while (x < n) {
    y = 0;
    while (y < n) {
      COUNT;
      y++;
    }
    x++;
  }
}

UPDATE : grid @x @y = count @x @y == 3 || count @x @y == 2 && grid @x @y; 

UPDATE_ALL : {
  x = 0;
  while (x < n) {
    y = 0;
    while (y < n) {
      UPDATE;
      y++;
    }
    x++;
  }
}

SHOW : put = grid @x @y ? '#' : '.'; 

SHOW_ALL : {
  put = 10; put = 10; put = 10; put = 10; put = 10; put = 10; put = 10; put = 10; put = 10; put = 10; \ clear \
  x = 0;
  while (x < n) {
    y = 0;
    while (y < n) {
      SHOW;
      y++;
    }
    x++;
    put = 10; \ add newline \
  }
}

ADVANCE : {
  COUNT_ALL;
  UPDATE_ALL;
  SHOW_ALL;
}

MAIN : {
  INITIALIZE; 
  while (1) ADVANCE;
}
```

If the `random` extension is not available, one can exchange `random` for `(x % 3 * y + x + 3 * y % 7) % 2;` and get quite similar results. 

### Proof of Turing Completeness: the brainfuck program

We can implement brainfuck in our language. Following common brainfuck convention, we read the program until we encounter a `!`, 
which delimits the brainfuck program from the input to the program. 

In `MAIN`, we'll call `INITIALIZE` and `RUN`. 

```
MAIN : {
  INITIALIZE;
  RUN;
}
```

`INITIALIZE` will `READ` the program and `PAIR` all the brackets. 

```
INITIALIZE : {
  READ;
  PAIR;
}
```

`READ` is simple: 

```
READ : {
  index = 0;
  flag = 1; \ indicates whether a '!' is met \
  while (flag) {
    next = get;
    program @index = next;
    if (next == '!') flag = 0; \ break from loop \
    index++; 
  }
  length = index - 1; \ `length` will store length of program \
}
```

If we enable debug mode and set `PAIR : {}` and `RUN : {}`, we can verify that our program is working with the input `abcde!abcde`:

```
index: 6
flag: 0
next: 33
program.0: 97
program.1: 98
program.2: 99
program.3: 100
program.4: 101
program.5: 33
length: 5
```

Now let us write `PAIR`, which will require a queue. 

```
PAIR : {
  index = 0;
  while (index < length) {
    if (program @index == '[') HEAP_PUSH;
    if (program @index == ']') {
      HEAP_POP;
      reference @index = return;
      reference @return = index;
    }
    index++; 
  }
}
```

The logic of this module is actually quite simple: we push `[` into the stack, and pop them when we have a `]` to match. 
Now we have to implement `HEAP_PUSH` and `HEAP_POP`. 

```
HEAP_PUSH : {
  \ push onto `heap` with size `size` \
  heap @size = index; 
  size++; 
}
```

```
HEAP_POP : {
  \ pop from `heap` with size `size` \
  size--;
  return = heap @size;
}
```

Notice how `HEAP_POP` doesn't actually erase anything from `heap`. These values are simply told to be removed
via the decrement of `size` and can be overwritten. 

We can test this on the input `[[][]][]!`. 

```
INDEX 0 1 2 3 4 5 6 7 8
CHAR  [ [ ] [ ] ] [ ] !
```

It is clear that `reference` should be: 

```
INDEX 0 1 2 3 4 5 6 7
REF   5 2 1 4 3 0 7 6
```

Running our program in debug mode gives:

```
...
reference.2: 1
reference.1: 2
reference.4: 3
reference.3: 4
reference.5: 0
reference.0: 5
reference.7: 6
reference.6: 7
```

Since we don't assign to `reference` in index order, the variables aren't created in that order. Reordering gives:

```
reference.0: 5
reference.1: 2
reference.2: 1
reference.3: 4
reference.4: 3
reference.5: 0
reference.6: 7
reference.7: 6
```

This is what we expect. 

Now we go on to implement `RUN`. We'll use `counter` for our program counter (indexing the character of the program
we are running) and `pointer` for the pointer on our `tape`. 

```
RUN : {
  while (counter < length) {
    if (program @counter == '+') tape @pointer ++; \ use { tape @pointer ++; tape @pointer %= 256; } for 8-bit wrapping memory \
    if (program @counter == '-') tape @pointer --; 
    if (program @counter == '>') pointer++; 
    if (program @counter == '<') pointer--;
    if (program @counter == ',') tape @pointer = get;
    if (program @counter == '.') put = tape @pointer;
    counter++; 
  }
}
```

The cases for `[` and `]` are a little more complex and we'll leave them for later. 
To test this, we'll use the input: `,+.>++++++++++.!a`. We should expect the output to be `b`. 
We also should have `pointer = 1`, `tape @0 = 98`, and `tape @1 = 10`. 

```
b
index: 15
flag: 0
next: 33
program.0: 44
...
program.15: 33
length: 15
tape.0: 98
counter: 15
pointer: 1
tape.1: 10
```

This is in accordance with our expectations. 

To implement `[` and `]`, recognize that `[` will set `pointer` to `reference @pointer` if the current cell is zero, 
and `]` will set `pointer` to `reference @pointer` if the current cell is non-zero. 

For instance, with the program `+++[-]!`, the states will be: 

```
+ + + [ - ]  tape @0 = 1
^

+ + + [ - ]  tape @0 = 2
  ^

+ + + [ - ]  tape @0 = 3
    ^

+ + + [ - ]  tape @0 = 3, continue
      ^

+ + + [ - ]  tape @0 = 2
        ^

+ + + [ - ]  tape @0 = 2, go back
          ^

+ + + [ - ]  tape @0 = 1
        ^

+ + + [ - ]  tape @0 = 1, go back
          ^

+ + + [ - ]  tape @0 = 0
        ^

+ + + [ - ]  tape @0 = 0, continue
          ^

+ + + [ - ]  tape @0 = 0, halt
            ^
```

We can now implement the rest of `RUN`: 

```
RUN : {
  while (counter < length) {
    if (program @counter == '+') tape @pointer ++; 
    if (program @counter == '-') tape @pointer --; 
    if (program @counter == '>') pointer++; 
    if (program @counter == '<') pointer--;
    if (program @counter == '[') counter = tape @pointer ? counter : reference @counter; 
    if (program @counter == ']') counter = tape @pointer ? reference @counter : counter; 
    if (program @counter == ',') tape @pointer = get;
    if (program @counter == '.') put = tape @pointer;
    counter++; 
  }
}
```

We can now test it on `+++[-]!`, and see that `tape.0` is indeed now `0`. 

Now, we can test it on the famous Hello World program: 

```
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.!
```

Which works beautifully: 

```
Hello World!
index: 111
flag: 0
next: 33
length: 111
heap.0: 10
size: 0
return: 10
reference.41: 10
reference.10: 41
tape.0: 0
counter: 111
pointer: 4
tape.1: 87
tape.2: 100
tape.3: 33
tape.4: 10
```

(Omitting all the `program.xxx` entries.) 

## Maze BFS

For a maze BFS, we’ll first read in the maze. Suppose that the maze is $N\times M$, and the start of the maze is at $(0, 0)$ and the end of the maze is at $(N-1,M-1)$. The input would be two integers $N$ and $M$, follows by the maze, which is $N$ lines of $M$ characters each. 

The `MAIN` sketch is as follows: 

```
MAIN : {
  INITIALIZE; 
  while (!error && !found) PROCESS;
  if (found) SHOW; 
}
```

Here, `error` will be raised if all the nodes have been explored and there is no path, and `found` will be true if a solution has been found. 

Let’s start by sketching the `INITIALIZE` function. We first have to read in the maze, which is straightforward enough: 

```
READ : {
  n = read; 
  m = read;
  x = 0;
  while (x < n) {
    y = 0;
    while (y < m) {
      maze @x @y = get;
      available @x @y = maze @x @y == '.'; 
      y++;
    }
    x++;
  }
}
```

Let’s try inputting: 

```
10 10
...#.#.#.#
....#.....
.....##..#
....#..##.
..#.##.#..
...#....##
#.#.......
........#.
.#.....#..
...#......
```

and see the debug information. (We’ll let `INITIALIZE : READ;`, `PROCESS : ERROR;`, and `SHOW : ERROR;`.) 

```
{
    'n': 10,
    'm': 10,
    'x': 10,
    'y': 10,
    'maze.0.0': 46,
    'available.0.0': 1,
    'maze.0.1': 46,
    'available.0.1': 1,
    'maze.0.2': 46,
    'available.0.2': 1,
    'maze.0.3': 35,
    'available.0.3': 0,
    'maze.0.4': 46,
    'available.0.4': 1,
    'maze.0.5': 35,
    'available.0.5': 0,
    'maze.0.6': 46,
    'available.0.6': 1,
    'maze.0.7': 35,
    'available.0.7': 0,
    ...
    'maze.9.7': 46,
    'available.9.7': 1,
    'maze.9.8': 46,
    'available.9.8': 1,
    'maze.9.9': 46,
    'available.9.9': 1,
    'error': 1
}

```

This is as we expected. Now, we can complete `INITIALIZE`. 

We’ll use a queue for our BFS since we don’t have recursion: 

```
PUSH : {
  \ push `next` into `queue` from `start` to `end` \
  queue @end @'x' = next @'x'; 
  queue @end @'y' = next @'y';
  end++; 
}
```

```
POP : {
  \ pop from `queue` from `start` to `end` to `return` \
  if ( start == end ) ERROR; 
  return @'x' = queue @start @'x';
  return @'y' = queue @start @'y';
  start++;
}
```

Where we’ll have `ERROR` as: 

```
ERROR : {
  \ print error message and set `error` \
  put = 'E'; 
  put = 'R'; 
  put = 'R'; 
  put = 'O'; 
  put = 'R'; 
  put = 10; \ newline \
  error = 1; 
}
```

The way our queue works is different from most other language’s implementations. In many other languages, queues are made from linked lists. 

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/07e772ed-f8c7-45d7-b953-e61360018aca/7aca3594-3412-499d-8ef7-0a5955d8aae5/image.png)

In a standard linked list like shown above, we have a reference of the first node, which has a reference to the next node, etc. We also have a reference to the last node, which next reference is `null`. When popping, we simply return the value of the first node, and update the `first` reference. Similarly, when pushing, we simply reference a new node from what is initially our last node and update the `last` reference. 

However, here, we simply use an infinitely long array (the inbuilt for *mandrill++* references). 

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/07e772ed-f8c7-45d7-b953-e61360018aca/10a82f91-2d90-409e-adc8-0dbd8c4902c2/image.png)

To pop, we simply increment `start`, and to push, we simply increment `end`! This is much easier (although not quite as practical in some other languages). 

`INITIALIZE` will be: 

```
INITIALIZE : {
  READ; 
  next @'x' = 0;
  next @'y' = 0;
  PUSH;
  available @0 @0 = 0; 
}
```

To avoid cluttering up stuff, let’s test the program on the (much simpler) maze:

```
2 2
..
#.
```

```
{
    'n': 2,
    'm': 2,
    'x': 2,
    'y': 2,
    'maze.0.0': 46,
    'available.0.0': 0,
    'maze.0.1': 46,
    'available.0.1': 1,
    'maze.1.0': 35,
    'available.1.0': 0,
    'maze.1.1': 46,
    'available.1.1': 1,
    'next.120': 0,
    'next.121': 0,
    'queue.0.120': 0,
    'queue.0.121': 0,
    'end': 1,
    'error': 1
}
```

As we expected. 

Now, let us implement `PROCESS`. We’ll `POP` from the queue, get all of its neighbors, and `REGISTER` them. 

```
PROCESS : {
  POP; 
  found = return @'x' + 1 == n && return @'y' + 1 == m;
  if (!error && !found) {
    next @'x' = return @'x';
    next @'y' = return @'y' + 1;
    REGISTER; 
    next @'y' = return @'y' - 1;
    REGISTER; 
    next @'y' = return @'y';
    next @'x' = return @'x' + 1;
    REGISTER; 
    next @'x' = return @'x' - 1;
    REGISTER; 
  }
}
```

Setting `REGISTER` to error as well and debugging, you will see that `found` does get set when the maze is 1 by 1, which is a good sign. (It still errors since `SHOW` is error.) 

The logic of `REGISTER` is easy enough: 

```
REGISTER : {
  x = next @'x'; 
  y = next @'y';
  if (available @x @y) {
    available @x @y = 0;
    parent @x @y @'x' = return @'x'; 
    parent @x @y @'y' = return @'y'; 
    PUSH; 
  }
}
```

Now, our debug information is: 

```
{
    'n': 2,
    'm': 2,
    'x': -1,
    'y': 1,
    'maze.0.0': 46,
    'available.0.0': 0,
    'maze.0.1': 46,
    'available.0.1': 0,
    'maze.1.0': 35,
    'available.1.0': 0,
    'maze.1.1': 46,
    'available.1.1': 0,
    'next.120': -1,
    'next.121': 1,
    'queue.0.120': 0,
    'queue.0.121': 0,
    'end': 3,
    'return.120': 1,
    'return.121': 1,
    'start': 3,
    'parent.0.1.120': 0,
    'parent.0.1.121': 0,
    'queue.1.120': 0,
    'queue.1.121': 1,
    'parent.1.1.120': 0,
    'parent.1.1.121': 1,
    'queue.2.120': 1,
    'queue.2.121': 1,
    'found': 1,
    'error': 1
}
```

Which does solve the maze. 

This leaves `SHOW`: 

```
SHOW : {
  x = n - 1;
  y = m - 1;
  maze @x @y = 'x';
  while (x || y) {
    x_ = parent @x @y @'x'; 
    y_ = parent @x @y @'y';
    x = x_;
    y = y_;
    maze @x @y = 'x';
  }
  PRINT; 
}
```

```
PRINT : {
  x = 0;
  while (x < n) {
    y = 0;
    while (y < m) {
      put = maze @x @y;
      y++;
    }
    put = 10;
    x++;
  }
}
```

Now let’s try this again:

```
10 10
...#.#.#.#
....#.....
.....##..#
....#..##.
..#.##.#..
...#....##
#.#.......
........#.
.#.....#..
...#......
```

```
xx.#.#.#.#
.x..#.....
.x...##..#
.x..#..##.
.x#.##.#..
.x.#....##
#x#.......
.xxxxxx.#.
.#....x#..
...#..xxxx
```

Nice! Now let’s try a $60\times60$: 

```
60 60
..##..#..#.#..#...................#..............##.#.#.##..
...#.......#...#..##..#........#.....##...#...#.........#...
#....###.#...#.#.......##..#..............##..#....#.##..#..
........##.#.#..#.........##...#.###..#.##..#..#..#.#..#....
...#.#....#......#......#................#......#.#....#.#..
#.#.......##.#.....#....#..#....#...........##...#..........
......#..#....#.....#....#.......#...#...#....#..#....#.....
#...#...#..#.#........#...#...........#..#.##.....#.#.....#.
..###.......#..##.#....#......#...#....#.#.#...........#....
...........#.#.#.#.....#..............#.....##........#.....
#..#...##..........#..#......#.#......#.#.......#...##......
#.....#......#.##.#..#.....#..#..#......#..........#........
...#.#.......#......#...##..#..#...##....#.##..........#.##.
#......#..##....#.#.#.......................#...##...#......
..#.#.#..#........#........##.##...............#.#......#...
..#.#........#....##.............#.#....#......#...#........
..#......#...#..#..##..........###........#....#........#...
.........##.##..#.....#...#....#......#........###......#...
.....##..#.....#.....#..#.##......#.###..####....#.##..#.#..
..##...#.........#.#.....##.......#.......#.##.......#.#...#
........#....####..........##..##.#.......#.......#...#...##
.#...#....##....#..........#.....##..#...................#.#
.#..#.##..#.....#................###........#.####..........
#..........#.#..#...#.#..#..#...##..#..................##...
........###.#......#........##.#....#..#..#....#...##.......
.......##.#.......#.....#......##........#.#....#.....##....
.#......#....##..##.......................##.....#.##......#
...#.....#..#...#...#.#.#.####.##...#.#.......#.#..........#
.#....#........###....#...#..##.#.........#.......#.....#.#.
..#.......#.#.#..###........#.#......#..#.#.........##.....#
#.............##...#.#....#..#.....#....#...#.##..#..#.#.#.#
.#.........#.#.....##.#.....###...#..#.#.#...#.....#....####
......#....#..#...#...#.........#...#...#....#......#.......
............##.....##..#.#..#.....#.....................##..
......#.#...#..#....#..#......#...#...#.......#..#........#.
.....#.....#..##.#........#.........#.#.#..###.........#.#..
.#...#.##..##....#......##..##...#.....#.#.#...##...#..#....
..........#...#.......#.....#........#........#...........#.
.....#..#.#....###..#....#.#...#....#.........#....###......
..#.####..#.........#........#....#.....#.......#..#....#...
#.#....##..#..#...#...#..#..#......#..#.#....#...#...#..#..#
..#.........#.#..............#..##..##.....#.....#....#.....
.#...#....#.#.........#...#......#......##.##.#.#...........
..........#.#............##..............#.##...##.##.....#.
.........##.#....###.##...#..##..............#...#....#....#
.#.........#.#.#....##....#............#.#..#........#..#...
.#.......##.....#....#.#..#.#.#...#.#..###.##...#.##...#..##
.#.......#......##..#..##........##..#.##..#.........##..#..
..#..##..........##.............#........#.#......#....#.#..
..##............#.#..............##.......##..#......#..##..
..........#.............#...#..#.##...........#..##.....##..
............#....#...#..#.........##.....#.##.....#........#
#..#.#.........##............#....#.....##..#........#.#....
..###...#...#.##.#..##.#......#..#..#...#.....#.....#.....##
##.#..#....#.............#..#....#..#......##....#..#..##...
..#..#....##....#...##.....#.......#...##.......##.#.#......
...#...#.........#....##.#.#........#.....#..##...#....#.#..
......#...#.#...#.....#........##.#......##..#....##..#.....
........#.##....#..#.........#...#..#....#.#.....#...#....#.
###.#.#.#.##....##....#.....##.#...##......#...........#....
```

```
xx##..#..#.#..#...................#..............##.#.#.##..
.xx#.......#...#..##..#........#.....##...#...#.........#...
#.xxx###.#...#.#.......##..#..............##..#....#.##..#..
....xxxx##.#.#..#.........##...#.###..#.##..#..#..#.#..#....
...#.#.x..#......#......#................#......#.#....#.#..
#.#....x..##.#.....#....#..#....#...........##...#..........
......#x.#....#.....#....#.......#...#...#....#..#....#.....
#...#..x#..#.#........#...#...........#..#.##.....#.#.....#.
..###..xxxx.#..##.#....#......#...#....#.#.#...........#....
..........x#.#.#.#.....#..............#.....##........#.....
#..#...##.xxxxxxxx.#..#......#.#......#.#.......#...##......
#.....#......#.##x#..#.....#..#..#......#..........#........
...#.#.......#...xxx#...##..#..#...##....#.##..........#.##.
#......#..##....#.#x#.......................#...##...#......
..#.#.#..#........#xxxxxxxx##.##...............#.#......#...
..#.#........#....##......xxxxx..#.#....#......#...#........
..#......#...#..#..##.........x###........#....#........#...
.........##.##..#.....#...#...x#......#........###......#...
.....##..#.....#.....#..#.##..x...#.###..####....#.##..#.#..
..##...#.........#.#.....##...x...#.......#.##.......#.#...#
........#....####..........##.x##.#.......#.......#...#...##
.#...#....##....#..........#..x..##..#...................#.#
.#..#.##..#.....#.............x..###........#.####..........
#..........#.#..#...#.#..#..#.x.##..#..................##...
........###.#......#........##x#....#..#..#....#...##.......
.......##.#.......#.....#.....x##........#.#....#.....##....
.#......#....##..##...........xxxxxxxxxxxx##.....#.##......#
...#.....#..#...#...#.#.#.####.##...#.#..xxxxx#.#..........#
.#....#........###....#...#..##.#.........#..xxxxx#.....#.#.
..#.......#.#.#..###........#.#......#..#.#......x..##.....#
#.............##...#.#....#..#.....#....#...#.##.x#..#.#.#.#
.#.........#.#.....##.#.....###...#..#.#.#...#...xx#....####
......#....#..#...#...#.........#...#...#....#....x.#.......
............##.....##..#.#..#.....#...............x.....##..
......#.#...#..#....#..#......#...#...#.......#..#x.......#.
.....#.....#..##.#........#.........#.#.#..###....x....#.#..
.#...#.##..##....#......##..##...#.....#.#.#...##.x.#..#....
..........#...#.......#.....#........#........#...x.......#.
.....#..#.#....###..#....#.#...#....#.........#...x###......
..#.####..#.........#........#....#.....#.......#.x#....#...
#.#....##..#..#...#...#..#..#......#..#.#....#...#x..#..#..#
..#.........#.#..............#..##..##.....#.....#x...#.....
.#...#....#.#.........#...#......#......##.##.#.#.x.........
..........#.#............##..............#.##...##x##.....#.
.........##.#....###.##...#..##..............#...#xxx.#....#
.#.........#.#.#....##....#............#.#..#.......x#..#...
.#.......##.....#....#.#..#.#.#...#.#..###.##...#.##x..#..##
.#.......#......##..#..##........##..#.##..#........x##..#..
..#..##..........##.............#........#.#......#.xxx#.#..
..##............#.#..............##.......##..#......#xx##..
..........#.............#...#..#.##...........#..##....x##..
............#....#...#..#.........##.....#.##.....#....xxx.#
#..#.#.........##............#....#.....##..#........#.#.x..
..###...#...#.##.#..##.#......#..#..#...#.....#.....#....x##
##.#..#....#.............#..#....#..#......##....#..#..##xxx
..#..#....##....#...##.....#.......#...##.......##.#.#.....x
...#...#.........#....##.#.#........#.....#..##...#....#.#.x
......#...#.#...#.....#........##.#......##..#....##..#....x
........#.##....#..#.........#...#..#....#.#.....#...#....#x
###.#.#.#.##....##....#.....##.#...##......#...........#...x
```

Let’s time how long a $100\times100$ takes: 

```
python3.10 smain.py program.man < in > out
1.27s user 0.03s system 99% cpu 1.301 total
```

Not bad! 

Let’s upgrade to $1000\times1000$. This will be hard. 

```
116.42s user 0.70s system 99% cpu 1:57.44 total
```

Dare we try $3000$? 

```
1076.15s user 14.91s system 99% cpu 18:14.33 total
```

Yah… we’re not pushing that.

# Extensions

Although this language is turing complete and very versatile, there is still room for improvement on additional features that are relatively easy to implement: 

- Special variable names (as in Perl) that keeps information of the program.
- Some `true` and `false` aliases. (Variables that can be evaluated but not assigned.)
- The ability to read in a string (i.e. detect a newline).
- The ability to import procedures from elsewhere.
- A standard library of useful mathematical functions such as fractions.
- A standard library of useful data structures such as heaps.
- A way to keep track of time.

Apart from these, there are more complicated extensions that students with enough willpower may try to attempt: 

- Local scope.
- Functions, classes, and more.
- Recursion.
- Structs.
- Maybe even functions as first-class citizens.
