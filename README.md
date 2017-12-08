# play-with-python

Here I will play with **_Python_** from ["Head First Python"](http://www.headfirstlabs.com/books/hfpython/book).



## Here are the bullets points to remember.

### Chapter 1:

1. Python comes with a built-in IDE called IDLE, which
lets you create, edit, and run your Python code—all
you need to do is type in your code, save it, and then
press F5.
2. IDLE interacts with the Python interpreter, which
automates the compile-link-run process for you. This
lets you concentrate on writing your code.
3. The interpreter runs your code (stored in a file) from
top to bottom, one line at a time. There is no notion of
a **_main()_** function/method in Python.
4. Python comes with a powerful standard library, which
provides access to lots of reusable modules (of which
**_datetime_** is just one example).
5. There is a collection of standard data structures
available to you when you're writing Python
programs. The list is one of them, and is very similar
in notion to an array.
6. The type of a variable does not need to be declared.
When you assign a value to a variable in Python, it
dynamically takes on the type of the data it refers to.
7. You make decisions with the **_if/elif/else_**
statement. The **_if_**, **_elif_**, and **_else_** keywords
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
11. If you’re looking at the **_>>>_** prompt, you’re at the
Python Shell. Go ahead: type in a single Python
statement and see what happens when it runs.
12. The shell takes your line of code and sends it to
the interpreter, which then executes it. Any results
are returned to the shell and are then displayed
on screen.
13. The **_for_** loop can be used to iterate a fixed
number of times. If you know ahead of time how
many times you need to loop, use **_for_**.
14. When you don’t know ahead of time how often
you’re going to iterate, use Python’s **_while_** loop
(which we have yet to see, but—don’t worry—we
will see it in action later).
15. The **_for_** loop can iterate over any sequence
(like a list or a string), as well as execute a fixed
number of times (thanks to the **_range_** function).
16. If you need to pause the execution of your
program for a specified number of seconds, use
the **_sleep_** function provided by the standard
library’s **_time_** module.
17. You can import a specific function from a module.
For example, **_from time import sleep_**
imports the sleep function, letting you invoke it
without qualification.
18. If you simply import a module—for example,
**_import time_**-you then need to qualify the
usage of any of the module’s functions with the
module name, like so: time.sleep().
19. The **_random_** module has a very useful function
called **_randint_** that generates a random
integer within a specified range.
20. The shell provides two interactive functions that
work at the **_>>>_** prompt. The **_dir_** function lists
an object’s attributes, whereas **_help_** provides
access to the Python docs.
21. Indentation takes a little time to get used to. Every
programmer new to Python complains about
indentation at some point, but don’t worry: soon
you’ll not even notice you’re doing it.
22. If there’s one thing that you should never, ever
do, it’s mix tabs with spaces when indenting
your Python code. Save yourself some future
heartache, and don’t do this.
23. The **_range_** function can take more than one
argument when invoked. These arguments let you
control the start and stop values of the generated
range, as well as the step value.
24. The **_range_** function’s step value can also be
specified with a negative value, which changes the
direction of the generated range


### Chapter 2:

1. Lists are great for storing a collection of
related objects. If you have a bunch of
similar things that you’d like to treat as
one, a list is a great place to put them.
2. List are similar to arrays in other
languages. However, unlike arrays in
other languages (which tend to be fixed
in size), Python’s lists can grow and
shrink dynamically as needed.
3. In code, a list of objects is enclosed in
square brackets, and the list objects are
separated from each other by a comma.
4. An empty list is represented like this: **_[]_**.
5. The fastest way to check whether an
object is in a list is to use Python’s **_in_**
operator, which checks for membership.
6. Growing a list at runtime is possible
due to the inclusion of a handful of list
methods, which include **_append_**,
**_extend_**, and **_insert_**.
7. Shrinking a list at runtime is possible
due to the inclusion of the **_remove_** and
pop methods.