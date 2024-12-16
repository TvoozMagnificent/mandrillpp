
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

The amazing thing with variables is that they can be reused. [Try][a = 5; a = a + 1; write = a;] the following program: 

```
a = 5;
a = a + 1;
write = a;
```



[write = 42 * 69;]: https://tio.run/##5Vrrc9vGEf/Ov@KkGRuESFGi82pAUbbTOq3bxEnTNGlLcTgQcJQQEY8cQVmKxL/d2b0XDoenPP3QmeoDCd7t7eO3e3u3C2X3@XWafPIhY@kV82MyJ@zw8PDDexblFH58@oIckc@/nJEPMDoYDEK6JlES0iQfbnMWJVeuRxjNdywhzkXiTH5Jo2ToPBKHjMgmSihZp0w8RAmBFWrVZJttonyIa1x3sEnTm10G4h4GBP6chF45Htn48WXoE98jx/5YTIyM4TG59IgPci7l5HF18lhPHlUnj/TkSXXy5ETPPqvOPtOTZ/bklERroDgjl4RutpScSsLzBsJzm3A@b6Ccz23SgybSgwrpWRPpWYX0vIn0vEL6/HkDqZ@ENu3jYwMtRIhtVy1lkuZAXSJ8WSYck8ADXpwrpwvGg/1gEGz87Zb8mN7QxOPrMIpXqyiJ8tVquKWb9Zjk9xkdk1t/s6Pzd2lCIa5xYoLjEJj4NRMjnAaG@LfBjtGMSXbFplg7XOzwQTPbj8lDwWfvOgYL@qvWJ82vKSv4GLrMxZz4hTibWqlJoZxhePQbZY3Gy82vbC5ygXySlgc7xmDnw/ipHMmR9RYGFkvN@4rmCoTg2md@kFMGFCbnhcluaXEfzcl0puzWHDT7jNIbC@Rm1hgKJeZnZAPeMBe4IlLQ5yUZq4Te5X0FjaYVUaNpT2FBmmx3MVVxiIi6wlP4Bw6kLBfD6F7BDTFwNY2pHaLvmr5Y8aXSEL2kcGUdQzBFEURbrq2GQISz8@a7r516ejgIRsdOEZgFli7qL@ksfgI4CYQkcSG1147XyZ1E2zC6ghPFtTVNYmcMWglXTmI/D66Hzun0xSeffvb5F3/4Eo6fRjv8ywBAvLqOfrnZxEma/cq2@e72/d39byvHFhOFIMYU0ba4WeTrr/74pzdf//kvb//6t2@@fffd93//4R8//vOnn//17/9URWbMEtm22G3x1tHJs7P5@YFTjnPOdJVmlPl5yoaN64fuw/7VS2/m9PFpI5fnj63r65nBEf6iliMEmnNx4XjGnpiZVgVpHOMdxp3Zm0dulyauh85hmSkmKLWLJG8Y0eKUyrCukGVGZsrCIa4wkDHZt2mHG1x4XqQOZLOlubHL@Sxo5zh66P11tKHmpkf05UpPLhjN7VxiZBlOUpZfBIlMl5f@lpJ5nSHCdD4/MuZ18pQ6of/mjkiWSGwZrP1nZTXDOMH2QMVBBnnU5oF@shjUqFEJI2nJg5PABF5gx5IIP8ciQuBjvygWLXuk6lye0rZKMvM3B6gwmo@KOwEajfnZM8/oiZ9lNAmH4nyZdbMtXTw4C3WR@mqTBjeNd4kA1AkZnmFyB8jfIEs9dl@auIjhRfIwPBwfQqQE12w4PXVdUV/IAoSzc3mFwR95iWGKdPcXiXG/onc02OXqoKXJrYFyMxNPjE/UalwngXi93UZXCQZiIxq3PgNRdxmjQJtqUG550oBPmSYKChgufnQDVaiAaKnKTIpw92Nr0NCkPzYbFSbAcpL4scTA2DMbvlN4zYh7jUVVeROKV1JfAogiwrnj6O1U5Zbtcs0L3d/Kr4UhTC82S2VCEwPp0bfr5rhOkzDKYSHc0cZkrcNbDWN8q2d1O8bCQT6v4Xk963bo27XtSM216s68OrR29@1uJXJpcV9V/MuIYBo5FRlYMq7bAj9j8umD2SXu6D6gcUIY59/deHEFngCZ0GPfM/SNA6UNJs9QvQ6lNxB1jSBt72MoXI98drVV@OAzQIBfKnwQKtEmWeACUW7AA@Yr2T7hvhLVsMfn5FpONucj3XiiqjacuFIg2ZaOQVuRjOFBZ1FulQ41bpeugKwMpFA1Y9U8hNbJ8AiFWPjXSlTA/0DX7ak5CptSchTCzyjssWVBSK/kC7J6mLxSqUpnWn3lwFS24p5fobnwU3ZDNEe@pgnAUvoGLzoT7NLxppxQz8qpEsOffBm7ORRxxWWyBlFkruBEM/B3N3zAX7ZHVvsOcCr3tBU/Khj1Q6eY5Lqy@/JAsZuxjQQyJ2iOp5/Q2QmcOcYNiJ8edwHN8iorqf1paULW6orl4nTJS5tjXWyeOiV6THPTQVXDG9k5UIxcXk1rtjeCrcHVgyUjm1eyi7lRueaz8G6WZfMM6wv23rJEA1hrspIeYB6iTxyvls/U4iMhA7Ua3Ai30P8FLwrcsC4zLO2GrYe5xjYWZi8NBD5iQ6/kDv0eq7fmA0bc3l3PatmJh8bWXobp8GFf19Yr1Q6CTf@OHqfv7ObVcW1r5kkbBXxGj2rMTxq3vdnW1mSbtZRsGeLeUoMKDrVFGV@6ylga0HDHaEPdlbGyLGOBJRXjpNzMm5m7DKd1@xgbRzWdEQWNRM9zXFeHwoIz4E1lfZUWGm3z2NxtiL/uIi@cb1@/fedYK/gtyUZRjtpdyqJ2XCy7EMaMAJto4eyxIkesl57moMrfiuZuQ@1foLV3vFqA9mZPTXpN1K26/rRs5BI/shH7RO/NuPfKsbRQrIQfW4U81Dc9GtxoHH4VTlHo1EnS7yucaG1l/S7bhtw2vI@XAwtru6Y1Ll@T18XujKznwm8LK81bEVGojFHeEBW8DywIUOK6dbcYkQN1H1oki8t2xPgG@DjQnoqYqsZqUJOKiwIsUBVeY2DztQyuygVJIo7Qml4jpiyYLKIIX0mitv31L@0Ao00i9RJdmQaJPI2MRujJ42NMIx8lgJdSmilcIsakPDc13z3I/VPQT5eqDYq3LpNP0bYvttZ/GZw23Tlwdm7j0qzcVk0aGOKV1M8H7aVlW@z3D7WJ@mXdlrAMf1mXB4RWbcfgun4BasmRAr5jwuzNK@23D/GUdVjra5DazH003pi8UeiLfTQRb7PZ2MawUze/0xVJkMZZD/X4vwY8QT1udKd@Qnpr175Q4aBLg6pZbmvwasPN4K3qY7sz7oCLp5szzDbn@HE254/8c84/D@aYhHS0dSEZ93F03KF1HFbeMdQrLtLkUxSM@3g67grErHyYtKl4hCqePEVFwbxTSU7WMxqTuDkc@dnevaeGDZcOcbg/7QhwzSMACVsiv0DaMN3P0/j/wHZupm18jdvtTV8sa4lONOxVg2GvhJLAFhuMVngK9t27vPARuS1eVMt7orxyYF/QvK5rZLAzh5PSQwPdOtD/UTRU/9cy0a8v3UHOKNaioisxlJW5UBxmscnBGwtIpirEUtP8w@8
[a = 5; a = a + 1; write = a;]: https://tio.run/##5VpZc@PGEX7nr4BUtQtApCjRjhMbFLS7ttfJJvHa8RmbYrEgYijBIg4PQK1kib990z0XBoNTW3lIVfRAgjM9fXzd0zPdUHZfXKfJx@8zml7RILZ8ix4eHr4P4OGT@Qi/AmtszeajdzQqCP6cvweC0WgUko0VJSFJCicvaJRcuZ5FSbGjiWVfJPb0tzRKHPvRsmH9NkqItUkpf4gSC1bIVdM820aFg2tcd7RN05tdBnIeRhb82Qm5sj1rG8SXYWAFnnUcTPjEWBueWJce0/NSTB7XJ4/V5FF98khNntQnT07U7LP67DM1eWZOzqxoAxRn1qVFtjmxTgXheQvhuUno@y2Uvm@SHrSRHtRIz9pIz2qk522k5zXS589bSIMkNGkfH1toIUJMuxopk7QA6grhiyrhxFp7wItxZXTryWg/Gq23QZ5bP6Q3JPHYOozi1SpKomK1cnKy3Uys4j4jE@s22O6I/zZNCMQ1TkxxHAITv@Z8hNHAEPvW2FGSUcGu3BQbm4l1HhSz/cR6KPnsXVtjQX5X@qTFNaElH00Xn8/xX4izrpWc5Mpphkd/ENpqvMgD0uYyLYgnYfl6RynsfBg/FSMFss5hYLFUvK9IIUFYXwc0WBeEAoXOeaGzWxrcxz5kHmm34qDYZ4TcGCC3s8ZQqDA/s7bgDX2ByyMFfV6RsUrIXTFU0HhWEzWeDRS2TpN8FxMZh4ioyz2Ff@BAQgs@jO7l3BADV9Ho2iH6ru6LFVsqDFFLSlc2MQRTJEGUM20VBDyc7dfffGU308NBMD62y8AssXRRf0Fn8OPACSAEiQupvXG8Se40ysPoCk4U19Q0ie0JaMVdOY2DYn3t2Kezjz7@0yd//sunn8Hx02pHcLkGEK@uo99utnGSZr/TvNjdvru7/2Nlm2KiEMToIroWt4t89fkXX77@6q9/e/P3f/zz67fffPuv777/4ceffv73L7/WRWbUENm12O3w1tHJszP//MCuxjljukozQoMipU7resd92L984c3tIT5t5fL8sXN9MzM4wj9q5AiBZl9c2J62J@a6Ves0jvEO487NzSO2SxvXQ/uwyhQTlNxFgjeMKHFSZVhXytIjM6Whgys0ZHT2XdrhBuee56kD2eSk0HY5mwXtbFsNvbuOtkTf9Ii@WOmJBWPfzCValmEkVfllkIh0eRnkxPKbDOGms/mxNq@Sp9AJ/efbPFkisWGw8p@R1TTjONsDGQcZ5FGTB/rJYNCgRi2MhCUPdgITeIGdCCL8nPAIgY/9oly0HJCqC3FKmyqJzN8eoNxoNsrvBGg05mdPP6OnQZaRJHT4@TLvZ1u5eDAW8iL1@TZd37TeJdagTkjxDBM7QPwGWfKx/9LERDgXyYNzODmESFlfU2d26rq8vhAFCGPnsgqDPbISQxfp7i8S7X5F7sh6V8iDliS3GsrtTDw@PpWrcZ0A4lWeR1cJBmIrGrcBBVF3GSVAmypQblnSgE@RJkoKGC5/9ANVqoBoycpMiHD3E2NQ02Q4NlsZJsBymgSxwEDbM1u2U1ixiHuNRnV5U4JX0kAAiCJC37bVdqpzy3aF4oXu7@TXwRCmF9ulNKGNgfDom017XKdJGBWwEO5oE2ujwlsOY3zLZ3k7xsJBPG/geTPvd@ibjelIxbXuzqI@tHH33W61xNLyvir5VxHBNHLKM7Bg3LQFfsbkMwSzS9zRQ0BjhDDOvvvxYgo8ATKux35g6GsHShdMnqZ6E0qvIepaQcrvYyhcjwJ6lUt88Bm7LvAlwweh4m2SBS7g5QY8YL4S7RPmK14Ne2xOrGVkPhvpxxNVNeHElRzJrnQM2vJkDA8qizKrVKgxu1QFZGQgiaoeq/ohtEmcIxRi4N8oUQL/Hdl0p@YobEvJUQg/o3DAlgUhg5IvyBpg8kqmKpVp1ZUDU9mKeX6F5sJP0Q1RHNmaNgAr6Ru8aE@xS8eaclw9I6cKDH8KROwWUMSVl8kGRJG5hBPNwN/98AF/0R5Z7XvAqd3TVuyooCQI7XKS6UrvqwPlbsY2EsicojmeekJnJ3DmaDcgdnrcrUlW1FkJ7U8rE6JWlywXp0tW2hyrYvPUrtBjmpuN6hreiM6BZOSyalqxveFsNa4eLBmbvJJdzIwqFJ@Fd7OsmqdZX7L3lhUawFqRVfQA8xB9y/Ya@cwMPgIyUKvFjXAL/V/wIscN6zLN0n7YBpirbWNu9lJD4AM29Ers0G@xems/YPjt3fWMlh1/aG3tZZgOH/ZNbb1K7cDZDO/oMfrebl4T165mnrCRw6f1qCbspHG7m21dTbZ5R8mWIe4dNSjn0FiUsaWrjKZrEu4oaam7MlqVpS0wpGKcVJt5c32X4bRqH2PjqKEzIqER6Hm266pQWDAGrKmsrtJco7yI9d2G@Ksu8sL@@tWbt7axgt2STBTFqNmlLGvHxbIPYcwIsIkW9h4rcsR66SkOsvytae621P4lWnvbawRor/fUhNd43arqT8NGJvEDG7FP9N6cea8aSwvJivuxU8hDc9OjxY3a4VfjFIV2kyT1vsKONkbW77PNYbbhfbwaWFjbta1x2ZqiKXbn1sbnflsYad6IiFJljPKWqGB9YE6AEjedu0WLHKj70CJRXHYjxjbAh4H2VMRkNdaAmlCcF2BrWeG1BjZbS@GqXJIk/Aht6DViyoLJMorwlSRqO1z/yg7Q2iRCL96VaZHI0sh4jJ48PsY08kECWCmlmMIlYmJV52b6uwexf0r62VK2QfHWpfMp2/bl1vovg9OlOwPOzG1MmpHb6kkDQ7yW@tmgubRqi/n@oTFRv2jaEobhL5ryANeq6xjcNC9ALRlSwHdiUXPzCvvNQzylPdYGCqQucx@1NyavJfp8H03522w6MTHs1S3odUWyTuNsgHrsXwOeoB4zulc/Lr2za1@qcNCnQd0stzN4leF68Nb1Md0Z98DF0s0ZZptz/Djz2SP79NnngY9JSEVbH5LxEEfHPVrHYe0dQ7PiPE0@RcF4iKfjvkDMqodJl4pHqOLJU1TkzHuVZGQDozGJ28ORne39e8ppuXTww/1pR4CrHwFI2BH5JdKa6UGRxv8HtjMzTeMb3G5u@nJZR3SiYS9bDHvJlQS22GA0wpOz79/lpY@s2/JFtbgniisH9gX167pCBjtzOCk8NFKtA/UfRY78v5apen3pjgpKsBblXQlHVOZccZjFJgdrLCCZrBArTfP3/wE









