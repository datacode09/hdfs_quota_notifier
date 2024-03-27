import subprocess

def execute_hdfs_command(path):
    command = f"hdfs dfs -count -q {path}"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        error = stderr.decode('utf-8')
        raise Exception(f"Error executing HDFS command: {error}")

    return stdout.decode('utf-8')

def parse_hdfs_output(output):
    lines = output.strip().split('\n')
    parsed_data = []

    for line in lines:
        parts = line.split()
        if len(parts) >= 8:  # Assuming at least 8 columns based on the output format
            parsed_data.append({
                'QUOTA': parts[0],
                'REM_QUOTA': parts[1],
                'SPACE_QUOTA': parts[2],
                'REM_SPACE_QUOTA': parts[3],
                'DIR_COUNT': parts[4],
                'FILE_COUNT': parts[5],
                'CONTENT_SIZE': parts[6],
                'PATHNAME': ' '.join(parts[7:])  # Pathname might contain spaces
            })

    return parsed_data

def format_for_email(parsed_data):
    email_content = "HDFS Directory Statistics:\n\n"
    for item in parsed_data:
        email_content += f"Pathname: {item['PATHNAME']}\n"
        email_content += f"Quota: {item['QUOTA']}, Remaining Quota: {item['REM_QUOTA']}, Space Quota: {item['SPACE_QUOTA']}, Remaining Space Quota: {item['REM_SPACE_QUOTA']}\n"
        email_content += f"Directory Count: {item['DIR_COUNT']}, File Count: {item['FILE_COUNT']}, Content Size: {item['CONTENT_SIZE']}\n\n"

    return email_content

# Example usage
path = "/your/hdfs/path"
output = execute_hdfs_command(path)
parsed_data = parse_hdfs_output(output)
email_content = format_for_email(parsed_data)
print(email_content)
 
