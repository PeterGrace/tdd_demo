Feature: Showing the multiplication of two numbers

  Scenario: run a proper example
     Given we have tdd_demo installed
      When we execute with arguments 7, 7
      Then we should get 49 on stdout
