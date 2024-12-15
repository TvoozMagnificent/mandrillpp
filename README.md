
# _mandrill++_

_mandrill++_ is a Python re-implementation of mandrill, introducing many more _exciting_ features. 

## Overview

The original _mandrill_ language (**not** _mandrill++_, and also not the enhanced _mandrill_ language in this repository) was designed to be as simple to implement of a language (using standard methods) as possible. This introduced features like:

- not much abstraction (no functions, classes, etc.)
- redundant grammar (many mandatory braces, mandatory `else` structures after `if` structures, etc.)
- no data structure (not even arrays!)
- no types (just integers.)

The _mandrill++_ language changes this. In _mandrill++_, we provide more elegant pieces of grammar, more constructs, and Macros that helps eliminate the redundancy within your code. However, _mandrill++_ is still designed to be a simplistic language. _mandrill++_ strives to be simplistic yet usable (to the general public), instead of being unnecessarily obfuscated for the sake of easy implementation. In this documentation, we will show you how to write in (**not** implement) _mandrill++_ (not assuming any previous experience in _mandrill_ or even programming). Programmers who find the entire tutorial wordy can skip ahead to the information dump and examples section. 

## Intro: Your First Program

Why would one study programming? Well, programming is a way to showcase your logical thinking ability and automate monotonous or purely logical tasks. Here's your first program:

```mandrill
write = 42 * 69; 
```

what do you think is the output? [Try It Online.][write = 42 * 69;] (Note: You'll see some code lying around, but you can collapse the _Header_ and _Footer_ portions of the page to get a better viewing experience.) Now try changing 69 to, say, 200, and try and predict the output. What if you put

```mandrill
write = 123456789 * 987654321;
```

? Isn't the program a little more convenient? 

As you move on, we'll show you how programming isn't just a glorified calculator but a powerful tool.

## Variables

What is the meaning of `write = 42 * 69`? Well, we can take it apart bit by bit:

![image](https://github.com/user-attachments/assets/01bbe402-86d6-4a1d-a285-428536efc8d8)

Therefore, `write = 42 * 69;` evaluates the expression `42 * 69` which is `2898`, and assigns it to the variable named `write`. Now, the variable `write` is synonymous with the value `2898`. 

There's only one thing to note here: since `write` is a special variable, values assigned to it gets printed out. This is why you see the answer on the screen. Normally, variable values are not shown on the screen. As an example, change `write` to any other variable of your choice, like `michael`, and try again. Note that variables can only constitute of lowercase letters and underscores - this convention is from _mandrill_. 



[write = 42 * 69;]: https://tio.run/##5Vpbd9vGEX7nr1jpHBuASNGik6YNKMp2Wqd12zhpmiZtKR4eiFhKiIhLFqBsR@Jvd2f2hsXiKrdv1QMJ7s7O5ZvZ2Z2Bsg/FTZp89jFj6TULYrIg7Pj4@OM7FhUUfnz@nJyQL76cf4TB0WgU0i2JkpAmhZsXLEquPZ8wWuxZQpzLxJn@nEaJ6zwQh4zJLkoo2aZMPEQJgRVq1TTPdlHh4hrPG@3S9HafgbT7EYE/J6HXjk92QXwVBiTwyWkwERNjY3hCrnwSgJwrOXlanzzVkyf1yRM9@aw@@eyZnn1Sn32iJ8/tyRmJtkBxTq4I3eWUnEnCixbCC5twsWihXCxs0qM20qMa6Xkb6XmN9KKN9KJG@vRpC2mQhDbtw0MLLUSIbVcjZZIWQF0hfFElnJCND7w4V063mYwOo9FmF@Q5@SG9pYnP12EUr9dREhXrtZvT3XZCig8ZnZC7YLeni7dpQiGucWKK4xCY@DUXI5wGhvi3wY7RjEl25abYOlyse6@ZHSbkvuRz8ByDBf1F65MWN5SVfAxdFmJO/EKcTa3UpFDOMDz6lbJW4@XeVzaXqUA@Scs3e8Zg58P4mRwpkHUOA8uV5n1NCwXC5iZgwaagDChMzkuT3criPl6Q2VzZrTlo9hmltxbI7awxFCrMz8kOvGEu8ESkoM8rMtYJfV8MFTSe1USNZwOFbdIk38dUxSEi6glP4R84kLJCDKN7BTfEwNM0pnaIvmf6Ys2XSkP0ktKVTQzBFEUQ5VxbDYEIZ@f1t187zfRwEIxPnTIwSyw91F/SWfwEcBIISeJBam8cb5I7jfIwuoYTxbM1TWJnAloJV07joNjcuM7Z7Plnn//mi9/@7ks4flrtCK42AOL1TfTz7S5O0uwXlhf7u3fvP/y6dmwxUQhiTBFdi9tFvvrq9394/fUf//Tmz3/56zdvv/3ub9///Yd//PjTP//177rIjFkiuxZ7Hd46efbkfHFx5FTjnDNdpxllQZEyt3W9690fXr7w584Qn7ZyefrQub6ZGRzhzxs5QqA5l5eOb@yJuWnVJo1jvMN4c3vzyO3SxvXYOa4yxQSldpHkDSNanFIZ1pWyzMhMWejiCgMZk32XdrjBhedF6kA2OS2MXc5nQTvH0UPvbqIdNTc9oi9X@nLBeGHnEiPLcJKq/DJIZLq8CnJKFk2GCNP5/NiY18lT6oT@WzgiWSKxZbD2n5XVDOME2yMVBxnkUZsH@sli0KBGLYykJfdOAhN4gZ1IIvyciAiBj8OyXLQakKoLeUrbKsnM3x6gwmg@Ku4EaDTmZ988o6dBltEkdMX5Mu9nW7l4cBbqIvXVLt3ctt4lNqBOyPAMkztA/gZZ6rH/0sRFuJfJvXs8OYZI2dwwd3bmeaK@kAUIZ@fxCoM/8hLDFOkdLhPjfkXf082@UActTe4MlNuZ@GJ8qlbjOgnEqzyPrhMMxFY07gIGot5njAJtqkG540kDPmWaKClguPzRD1SpAqKlKjMpwjtMrEFDk@HY7FSYAMtpEsQSA2PP7PhO4SUj7jUW1eVNKV5JAwkgiggXjqO3U51bti80L3R/J78OhjC93K2UCW0MpEffbNvjOk3CqICFcEebkK0ObzWM8a2e1e0YCwf5vIXn7bzfoW@2tiM117o7i/rQ1jt0u5XIpeV9VfGvIoJp5ExkYMm4aQv8hMlnCGZXuKOHgMYJYZx/9@PFFXgEZEKPw8DQNw6ULph8Q/UmlF5D1LWClH@IoXA9Cdh1rvDBZ4AAv1T4IFSiTbLEBaLcgAfMV7J9wn0lqmGfz8m1nGzBR/rxRFVtOHGlQLIrHYO2IhnDg86i3CodatwuXQFZGUihasaqeQhtE/cEhVj4N0pUwH9Pt92pOQrbUnIUws8oHLBlQcig5AuyBpi8VqlKZ1p95cBUtuaeX6O58FN2QzRHvqYNwEr6Bi86U@zS8aacUM/KqRLDHwMZuwUUceVlsgFRZK7gRDPwdz98wF@2R9aHHnBq97Q1PyoYDUKnnJQE2C4C3lNU29dP6NQEzhbjpmOU2YpqebbiVcmprhPPnAo9ZqhZZUSkiltZ9CtGHi@ENdtbwdbg6sOSsc0r2cdcz0LzWfq3q6rGhkEle39lo6DJKnqAeQgccfxGPjOLj/QVqNXiAbhA/pcOECZjNWQo2W/xAE2NzSM0XhnKf8I2Wst98R3WTO1pXdyZPd9qlImH1oZahkno/tDUTKvc2AWb4X00Tt/bQ2vi2tVCkzYK@IzO0ITnd6@7xdXV2pp3FEoZ4t5R@QkOjaUQX7rOWLqh4Z7RlmonY1VZxgJLKsZJtYU2NzcITuumLbZrGvoRChqJnu94ng6FJWfAW7n6Ais0yovY3ECIv@7dLp1vXr1561gr@N3ERlGO2r3BsmJbrvoQxk0Om2jpHLAORqxXvuagis6a5l5LxV2idXD8RoAOZidLek1Ui7rqs2zkEj@x/flI782596qxtFSshB87hdw3txpa3GicWzVOUeg0SdJvCZxoayXsPttcbhvegquBhRVV2xqPrymaYndOtgvht6WV5q2IKFXGKG@JCt59FQQocdu5W4zIgWoLLZIlXTdifAN8GmiPRUzVQA2oScVF2bNRdVVrYPO1DC6oJUkijtCGDh@mLJgsowhfBKK2w/Wv7ACjOSH1Er2QFok8jYzH6MnTU0wjnySAFzCaKVwiJqQ6NzM7/nL/lPSzlWo@4oXJ5FM2y8ut9T8Gp0t3Dpyd27g0K7fVkwaGeC3180F7adUWu@vfmKhfNG0Jy/AXTXlAaNV1DG6bF6CWHCngOyHM3rzSfvsQT1mPtYEGqcvcB@M9xWuFvthHU/EOmU1sDHt1C3pdkWzSOBugHn8h/wj1uNG9@gnpnb3yUoWjPg3qZnmdwasNN4O3ro/tzrgHLp5uzjHbXODH@YI/8s8F/zxaYBLS0daHZDzE0XGP1nFY6@w3Ky7S5GMUjId4Ou4LxKx6mHSpeIIqPnuMioJ5r5KcbGA0JnF7OPKzvX9PuS2XDnG4P@4I8MwjAAk7Ir9E2jA9KNL4/8B2bqZtfIPb7U1fLuuITjTsZYthL4WSwBbbelZ4Cvb9u7z0EbkrXw/Le6K8cmA3zryua2SwH4aT0kMj3TrQ/8fjqv8mmeqXht6oYBRrUdGVcGVlLhSHWWxy8MYCkqkKsdKq/vgf










