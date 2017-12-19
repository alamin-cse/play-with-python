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
8. Take care when copying one list to another. If you want to have another variable reference an existing list, use the assignment operator **_(=)_**. If you want to make a copy of the objects in an existing list and use them to initialize a new list, be sure to use the **_copy_** method instead.
9. Lists understand the square bracket notation,
which can be used to select individual objects
from any list.
10. Like a lot of other programming languages,
Python starts counting from zero, so the first
object in any list is at index location 0, the
second at 1, and so on.
11. Unlike a lot of other programming languages,
Python lets you index into a list from either end.
Using –1 selects the last item in the list, –2 the
second last, and so on.
12. Lists also provide slices (or fragments) of a list
by supporting the specification of start, stop,
and step as part of the square bracket notation.


### Chapter 3:


1. Think of a dictionary as a collection of rows, with each
row containing exactly two columns. The first column
stores a **_key_**, while the second contains a **_value_**.
2. Each row is known as a **_key/value pair_**, and a dictionary
can grow to contain any number of key/value pairs. Like
lists, dictionaries grow and shrink on demand.
3. A dictionary is easy to spot: it’s enclosed in curly braces,
with each key/value pair separated from the next by a
comma, and each key separated from its value by a
colon.
4. Insertion order is not maintained by a dictionary. The
order in which rows are inserted has nothing to do with
how they are stored.
5. Accessing data in a dictionary uses the **_square bracket
notation_**. Put a key inside square brackets to access its
associated value.
6. Python’s **_for_** loop can be used to iterate over a
dictionary. On each iteration, the key is assigned to the
loop variable, which is used to access the data value.
7. By default, every dictionary is unordered, as insertion
order is not maintained. If you need to sort a dictionary
on output, use the **_sorted_** built-in function.
8. The **_items_** method allows you to iterate over a
dictionary by row—that is, by key/value pair. On each
iteration, the **_items_** method returns the next key and
its associated value to your for **_loop_**.
9. Trying to access a nonexistent key in an existing
dictionary results in a **_KeyError_**. When a
**_KeyError_** occurs, your program crashes with a
runtime error.
10. You can avoid a **_KeyError_** by ensuring every key
in your dictionary has a value associated with it before
you try to access it. Although the **_in_** and **_not in_**
operators can help here, the established technique is to
use the **_setdefault_** method instead.
11. Sets in Python do not allow duplicates.
12. Like dictionaries, sets are enclosed in curly braces,
but sets do not identify key/value pairs. Instead, each
unique object in the set is separated from the next by a
comma.
13. Also like dictionaries, sets do not maintain insertion
order (but can be ordered with the **_sorted_** function).
14. You can pass any sequence to the set function
to create a set of elements from the objects in the
sequence (minus any duplicates).
15. Sets come pre-packaged with lots of built-in functionality,
including methods to perform **_union_**, **_difference_**, and
**_intersection_**.
