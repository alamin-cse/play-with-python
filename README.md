# play-with-python

Here I will play with **Python** from ["Head First Python"](http://www.headfirstlabs.com/books/hfpython/book).



## here are the bullets points to remember.

### chapter 1:

1. Python comes with a built-in IDE called IDLE, which
lets you create, edit, and run your Python code—all
you need to do is type in your code, save it, and then
press F5.
2. IDLE interacts with the Python interpreter, which
automates the compile-link-run process for you. This
lets you concentrate on writing your code.
3. The interpreter runs your code (stored in a file) from
top to bottom, one line at a time. There is no notion of
a **main()** function/method in Python.
4. Python comes with a powerful standard library, which
provides access to lots of reusable modules (of which
**datetime** is just one example).
5. There is a collection of standard data structures
available to you when you're writing Python
programs. The list is one of them, and is very similar
in notion to an array.
6. The type of a variable does not need to be declared.
When you assign a value to a variable in Python, it
dynamically takes on the type of the data it refers to.
7. You make decisions with the **if/elif/else**
statement. The **if**, **elif**, and **else** keywords
precede blocks of code, which are known in the
Python world as “suites.”
8. It is easy to spot suites of code, as they are always
indented. Indentation is the only code grouping
mechanism provided by Python.
9. In addition to indentation, suites of code are also
preceded by a colon (:). This is a syntactical
requirement of the language.
10. When trying to determine the code that they
need to solve a particular problem, Python
programmers often favor experimenting with code
snippets at the shell.
11. If you’re looking at the **>>>** prompt, you’re at the
Python Shell. Go ahead: type in a single Python
statement and see what happens when it runs.
12. The shell takes your line of code and sends it to
the interpreter, which then executes it. Any results
are returned to the shell and are then displayed
on screen.
13. The **for** loop can be used to iterate a fixed
number of times. If you know ahead of time how
many times you need to loop, use **for**.
14. When you don’t know ahead of time how often
you’re going to iterate, use Python’s **while** loop
(which we have yet to see, but—don’t worry—we
will see it in action later).
15. The **for** loop can iterate over any sequence
(like a list or a string), as well as execute a fixed
number of times (thanks to the **range** function).
16. If you need to pause the execution of your
program for a specified number of seconds, use
the **sleep** function provided by the standard
library’s **time** module.
17. You can import a specific function from a module.
For example, **from time import sleep**
imports the sleep function, letting you invoke it
without qualification.
18. If you simply import a module—for example,
**import time**—you then need to qualify the
usage of any of the module’s functions with the
module name, like so: time.sleep().
19. The **random** module has a very useful function
called **randint** that generates a random
integer within a specified range.
20. The shell provides two interactive functions that
work at the **>>>** prompt. The **dir** function lists
an object’s attributes, whereas **help** provides
access to the Python docs.
21. Indentation takes a little time to get used to. Every
programmer new to Python complains about
indentation at some point, but don’t worry: soon
you’ll not even notice you’re doing it.
22. If there’s one thing that you should never, ever
do, it’s mix tabs with spaces when indenting
your Python code. Save yourself some future
heartache, and don’t do this.
23. The **range** function can take more than one
argument when invoked. These arguments let you
control the start and stop values of the generated
range, as well as the step value.
24. The **range** function’s step value can also be
specified with a negative value, which changes the
direction of the generated range