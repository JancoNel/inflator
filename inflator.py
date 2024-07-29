import subprocess
import time
import os

# Paths and filenames
repo_path = 'C:/Users/Hannes Nel/Downloads/Desktop/cod3e/inflator'
file_path = os.path.join(repo_path, 'yourfile.py')
version1_content = '# Version 1 content'
version2_content = '# Version 2 content'

def write_file(content):
    with open(file_path, 'w') as f:
        f.write(content)

def run_git_command(commands):
    result = subprocess.run(commands, cwd=repo_path, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout

def commit_file(version):
    write_file(version)
    run_git_command(['git', 'add', file_path])
    run_git_command(['git', 'commit', '-m', f'Update to {version}'])
    run_git_command(['git', 'push', 'origin', 'main'])  # Adjust branch name if necessary

def main():
    while True:
        commit_file(version1_content)
        time.sleep(10)
        print("Did number 1")
        commit_file(version2_content)
        print("Did number 2")
        time.sleep(10)

if __name__ == "__main__":
    main()
