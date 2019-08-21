from subprocess import run
from behave import *
from pprint import pprint


@given('we have tdd_demo installed')
def step_impl(context):
    pass


@when('we execute with arguments {first}, {second}')
def step_impl(context, first, second):
    rs = run(["tdd_demo", "7", "7"], capture_output=True)
    context.stdout=rs.stdout
    context.stderr=rs.stderr



@then('we should get {value} on stdout')
def step_impl(context, value):
    # because we get stdout as a bytes string, we need to convert it to ascii and then remove the trailing \n (rstrip does this for us)
    val = context.stdout.decode("ascii").rstrip()
    assert val == value
