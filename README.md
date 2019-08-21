tdd_demo
===============
This is a repo I generated to help explain test driven design to some coworkers.


# What is TDD
=============
Test-Driven Design, or TDD, is a programming dogma that is followed in varying degrees by some organizations.  Simply explained, TDD instructs you to think about what you're going to write, then write test cases that prove that what you're going to write will work, then you implement the thing you're writing, and use those unit tests to prove or disprove that your code is functioning as it should.

# Step by step
  1. I'm going to write a program, tdd_demo, that executes arbitrary multiplication and produces an answer.
  1. I'm going to write a unit test case in the tests/ subfolder that will test that my function properly handles multiplication.
  1. I'm going to write the actual arbitrary multiplication function
  1. I'm then going to execute the unit tests to confirm that my function works.
  1. I'm optionally going to execute a code coverage report to see how much of my program is actually covered by available unit tests.

