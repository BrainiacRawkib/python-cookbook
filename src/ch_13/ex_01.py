# accepting script input via redirection, pipes, or input files
import fileinput


with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')
