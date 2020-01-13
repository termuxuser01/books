import shlex
import subprocess   

def run(command):
    try:
        #split the command itself from its arguments
        result = subprocess.check_output(shlex.split(command), stderr=subprocess.STDOUT )#turn errors to stdout to display errors in commands
        return 0, result
    except subprocess.CalledProcessError as e:
        return e.returncode, e.output


for path in ('/', '/poop'):
    status, out = run(f'ls "{path}"')
    if status == 0:
        print('<success>')
    else:
        print(f'<Error: {status}')
    print(out)

