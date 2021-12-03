# executing an external command and getting its output
import subprocess

out_bytes = subprocess.check_output(['netstat', '-a'])
out_text = out_bytes.decode('utf-8')

if __name__ == '__main__':
    print(out_text)
