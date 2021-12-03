import subprocess

try:
    out_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'],
                                        stderr=subprocess.STDOUT)  # If you want both standard output and error
    # collected, use the stderr argument
except subprocess.CalledProcessError as e:
    out_bytes = e.output  # Output generated before error
    code = e.returncode  # Return code


try:
    out_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'],
                                        timeout=5)  # If you need to execute a command with a timeout
except subprocess.TimeoutExpired as e:
    out_bytes = e.output  # Output generated before error
    code = e.timeout  # Return code

if __name__ == '__main__':
    # out_bytes = subprocess.check_output('grep python | wc > out', shell=True)
    pass
