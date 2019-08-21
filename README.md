tdd_demo
===============
This is a repo I generated to help explain test driven design to some coworkers.


## What is TDD
Test-Driven Design, or TDD, is a programming dogma that is followed in varying degrees by some organizations.  Simply explained, TDD instructs you to think about what you're going to write, then write test cases that prove that what you're going to write will work, then you implement the thing you're writing, and use those unit tests to prove or disprove that your code is functioning as it should.

The concept emphasizes the idea that you should be writing small chunks of code, and then testing those small chunks work.  You shouldn't be writing humungous monoliths that haven't had their assumptions tested.

Good software design emphasizes the KISS principle (Keep it simple, stupid) and this is embodied in the concept that functions should do one thing at a time.

### Example
I want to bake a cake
### Implementation, Bad
```cake = make_cake()```
### Implementation, Better
```
   oven.preheat()
   ingredients.gather()
   ingredients.combine()
   oven.insert(ingredients)
   oven.timer()
   cake = oven.remove()
```

In the above examples, we can assume that make_cake() is a monolith function that does all of the steps at once.  This is difficult to test, because then you have to know every edge case that might go wrong in baking your cake.  In the second example, we've broken down the making of the cake into smaller, distinct algorithmic parts that are more easily testable.

That's not to say that you might not have all of the "better" commands inside of a make_cake() function to make your top-level code easier to read, but, each element of the business logic really needs to be testable, so you'd still want to have unit tests for all of those individual steps.


## Step by step
  1. I'm going to write a program, tdd_demo, that executes arbitrary multiplication and produces an answer.
  1. I'm going to write a unit test case in the tests/ subfolder that will test that my function properly handles multiplication.
  1. I'm going to write the actual arbitrary multiplication function
  1. I'm then going to execute the unit tests to confirm that my function works.
  1. I'm optionally going to execute a code coverage report to see how much of my program is actually covered by available unit tests.

## How to use this repo
### install
  1. clone repo
  1. execute `pip install --user -e .` to install the repo as a symlink

### usage
  1. run `tox` to create a specific virtual env that installs your whole project, and then runs the specified tests.
