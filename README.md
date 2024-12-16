
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

## Organization of _mandrill++_ 

_mandrill++_ can define procedures with capitalized letters and underscores (but not a single `_`). 
By default, the `MAIN` procedure is called at the end. Statements can also be written outside procedure definitions: 
in these cases, these statements are implicitly contained within a `MAIN` procedure. Procedures can build on
previous procedures and can also override. For instance, 
```
A : {
  a++;
}
A : {
  A;
  A;
}
A : {
  A;
  A;
}
A : {
  A;
  A;
}
```
defines a procedure `A` which executes `a++;` 8 times. 

