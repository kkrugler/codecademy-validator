import codecademy
import os.path

SUCCESS_COLOR = '\033[92m'
WARNING_COLOR = '\033[91m'
NORMAL_COLOR = '\033[0m'

# TODO Use more compatible color method (e.g., via https://pypi.python.org/pypi/colorama)?
# (ANSI) SUCCESS_COLOR is pretty ugly right now anyway.
def print_test_result(result_message, color=NORMAL_COLOR):
    print color
    print result_message
    print NORMAL_COLOR

def try_code(solution_filename, sct_filename, is_expect_pass = True):

    print("\n=========================================================")
    if (is_expect_pass):
        verb = "passes"
    else:
        verb = "fails"
    print("Checking whether %s %s expectations in %s..." % (solution_filename, verb, sct_filename))

    codecademy.SINGLETON.__init__()
    codecademy.SINGLETON.eval(solution_filename);

    sct_code = ""
    for line in open(sct_filename).readlines():
        sct_code += "    " + line

    context = """from codecademy import SINGLETON

def test():
    CC = SINGLETON
    error = CC.error
    code = CC.code
%s

SINGLETON.setResult(test())
""" % sct_code

    exec(context) in codecademy.SINGLETON.globals

    if is_expect_pass:
        if codecademy.SINGLETON.result == True:
            print_test_result("Test passed as expected.", SUCCESS_COLOR)
        else:
            print_test_result("TEST FAILURE! " + str(codecademy.SINGLETON.result), WARNING_COLOR)
            return False
    else:
        if codecademy.SINGLETON.result == True:
            print_test_result("EXPECTATION FAILURE! Test should not have passed.", WARNING_COLOR)
            return False
        else:
            print_test_result("Test failed as expected.", SUCCESS_COLOR)

    return True

def test_exercises(exercise_names):
    is_all_as_expected = True
    is_missing_some_support = False
    for exercise_name in exercise_names:
        default_filename = "%s_default.py" % exercise_name
        solution_filename = "%s.py" % exercise_name
        sct_filename = "%s_sct.py" % exercise_name

        if (not os.path.exists(sct_filename)):
            is_missing_some_support = True
            print_test_result("Warning! No SCT exists yet for %s." % exercise_name, WARNING_COLOR)

        if (not os.path.exists(solution_filename)):
            is_missing_some_support = True
            print_test_result("Warning! No solution exists yet for %s." % exercise_name, WARNING_COLOR)
        elif (os.path.exists(sct_filename)):
            is_all_as_expected &= try_code(solution_filename, sct_filename)

        if  (   os.path.exists(default_filename)
            and os.path.exists(sct_filename)):
            is_all_as_expected &= try_code(default_filename, sct_filename, False)

    print
    if (is_missing_some_support):
        print_test_result("Warning! More support required for full validation.", WARNING_COLOR)
    if (is_all_as_expected):
        if (is_missing_some_support):
            print_test_result("However, everything tested behaved as expected.", SUCCESS_COLOR)
        else:
            print_test_result("SUCCESS! Everything behaved as expected.", SUCCESS_COLOR)
    else:
        print_test_result("AT LEAST ONE EXPECTATION WAS VIOLATED!", WARNING_COLOR)
    return is_all_as_expected
