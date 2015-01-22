import codecademy

exercise_names = ["section1-exercise1",
                  "section1-exercise2",
                  "section1-exercise3",
                  "section1-exercise4",

                  "section2-exercise1",
                  "section2-exercise2"]

runner = codecademy.CC
for exercise_name in exercise_names:

    solution_filename = "%s.py" % exercise_name
    sct_filename = "%s-sct.py" % exercise_name
    print("\ntesting whether %s meets expectations in %s..." % (solution_filename, sct_filename))

    runner.__init__()
    runner.eval(solution_filename);

    sct_code = ""
    for line in open(sct_filename).readlines():
        sct_code += "    " + line


    context = """from codecademy import CC

def test():
    error = CC.error
    code = CC.code
%s

CC.setResult(test())
""" % sct_code

    exec(context) in runner.globals

    if runner.result != True:
        print
        print "Test failed! " + str(runner.result)

