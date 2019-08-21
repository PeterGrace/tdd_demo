from subprocess import run
from behave import *
from pprint import pprint


@given('we have tdd_demo installed')
def step_impl(context):
    pass


@when('we execute with arguments {first}, {second}')
def step_impl(context, first, second):
    rs = run(["tdd_demo", first, second], capture_output=True)
    context.stdout = rs.stdout
    context.stderr = rs.stderr
    context.returncode = rs.returncode



@then('we should get {value} on stdout')
def step_impl(context, value):
    # because we get stdout as a bytes string, we need to convert it to ascii and then remove the trailing \n (rstrip does this for us)
    val = context.stdout.decode("ascii").rstrip()
    try:
        assert val == value
    except AssertionError as ex:
        print(f"val is |{val}|, value is |{value}|")
        raise ex

@then('we should get a non-zero return code')
def step_impl(context):
    try:
        assert context.returncode != 0
    except AssertionError as ex:
        print(f"returncode is {context.returncode}\nstdout is {context.stdout}\nstderr is {context.stderr}")
        raise ex
