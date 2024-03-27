import subprocess

# Define the HDFS command you want to execute
command = "hdfs dfs -count -q /path"  # Make sure to replace '/path' with your actual HDFS directory path

# Execute the command and capture the output
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
stdout, stderr = process.communicate()

# Decode the output and error (if any) from bytes to string
output = stdout.decode('utf-8')
error = stderr.decode('utf-8')

if process.returncode == 0:
    print("Command executed successfully:")
    print(output)
else:
    print("An error occurred while executing the command:")
    print(error)
