import subprocess

def test_yi2():
    command = ['python', 'cache_simulator.py', '-v', '-s', '1', '-E', '1', '-b', '1', '-t', 'traces/yi2.trace']
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=False, encoding='utf-8')
    stdout, stderr = process.communicate()
    with open("yi2_output.txt", "r") as f:
        reference_output = f.read()
        assert stdout == reference_output

def test_yi():
    command = ['python', 'cache_simulator.py', '-v', '-s', '4', '-E', '2', '-b', '4', '-t', 'traces/yi.trace']
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=False, encoding='utf-8')
    stdout, stderr = process.communicate()
    with open("yi_output.txt", "r") as f:
        reference_output = f.read()
        assert stdout == reference_output

def test_dave():
    # Define the command you want to run
    command = ['python', 'cache_simulator.py', '-v', '-s', '2','-E', '1', '-b', '4', '-t', 'traces/dave.trace']

    # Use Popen to run the command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=False, encoding='utf-8')

    # Wait for the process to finish and get the output
    stdout, stderr = process.communicate()

    with open("dave_output.txt", "r") as f:
        reference_output = f.read()
        print(reference_output)
        print(stdout)
        assert stdout == reference_output

def test_trans1():
    command = ['python', 'cache_simulator.py', '-v', '-s', '2', '-E', '1', '-b', '3', '-t', 'traces/trans.trace']
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=False, encoding='utf-8')
    stdout, stderr = process.communicate()
    with open("trans1_output.txt", "r") as f:
        reference_output = f.read()
        assert stdout == reference_output

def test_trans2():
    command = ['python', 'cache_simulator.py', '-v', '-s', '2', '-E', '2', '-b', '3', '-t', 'traces/trans.trace']
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=False, encoding='utf-8')
    stdout, stderr = process.communicate()
    with open("trans2_output.txt", "r") as f:
        reference_output = f.read()
        assert stdout == reference_output

def test_trans3():
    command = ['python', 'cache_simulator.py', '-v', '-s', '2', '-E', '4', '-b', '3', '-t', 'traces/trans.trace']
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=False, encoding='utf-8')
    stdout, stderr = process.communicate()
    with open("trans3_output.txt", "r") as f:
        reference_output = f.read()
        assert stdout == reference_output

def test_trans4():
    command = ['python', 'cache_simulator.py', '-v', '-s', '5', '-E', '1', '-b', '5', '-t', 'traces/trans.trace']
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=False, encoding='utf-8')
    stdout, stderr = process.communicate()
    with open("trans4_output.txt", "r") as f:
        reference_output = f.read()
        assert stdout == reference_output

# def test_long():
#     command = ['python', 'cache_simulator.py', '-v', '-s', '5', '-E', '1', '-b', '5', '-t', 'traces/long.trace']
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=False, encoding='utf-8')
#     stdout, stderr = process.communicate()
#     with open("long_output.txt", "r") as f:
#         reference_output = f.read()
#         assert stdout == reference_output
