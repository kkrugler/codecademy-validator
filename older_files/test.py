from older_files import runner

runner = runner.CC

runner.eval("eliza_student.py");

funccode = ""
for line in open("eliza_test.py").readlines():
    funccode += "\t" + line


code = '''from runner import CC

def test():
%s

CC.setResult(test())
''' % funccode

exec(code)

if runner.result != True:
    print
    print "Test failed! " + str(runner.result)

