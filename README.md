
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

The output is `359036568873322`, so our answer is `0.359036568873322`. This agrees with the answer given by the problem-setters. 

In our implementation, we use array references to get the job done. Of course, it is possible to evade them - 
that is left as an exercise to the reader. 

### Conway's Game of Life

To implement Conway's Game of Life, we introduce a new special variable: `random`. Evaluating `random` gives
either 0 or 1 with 1/2 chance/  

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

Our `ADVANCE` procedure will have 4 steps: 

```
ADVANCE : {
  COUNT_ALL;
  UPDATE_ALL;
  SHOW_ALL;
  sleep = 100;
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





