import subprocess
proc = subprocess.Popen(['python', 'prepare_data_app.py'],
                            stdin = subprocess.PIPE,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE
                        )

(out, err) = proc.communicate()
print out
# proc2 = subprocess.Popen(['python', 'run_testing_app.py', shell=True],
#                             stdin = subprocess.PIPE,
#                             stdout = subprocess.PIPE,
#                             stderr = subprocess.PIPE
#                         )
output  = subprocess.check_call(['python run_testing_app.py'], shell=True)
print "Hello"
# print out2   
print "Hello2"