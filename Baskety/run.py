import os
import sys
import subprocess
import platform

def run_command(command, cwd=None):
    """Executes a terminal command and returns the output."""
    try:
        subprocess.check_call(command, shell=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        sys.exit(e.returncode)

def get_python_executable():
    """Returns the path to the Python executable in the virtual environment."""
    if os.path.exists("venv"):
        if platform.system() == "Windows":
            return os.path.join("venv", "Scripts", "python.exe")
        else:
            return os.path.join("venv", "bin", "python")
    return sys.executable

def main():
    # 1. Determine Python executable
    python_exe = get_python_executable()
    print(f"Using Python: {python_exe}")

    # 2. Install dependencies
    if os.path.exists("requirements.txt"):
        print("Checking/Installing dependencies...")
        run_command(f"{python_exe} -m pip install -r requirements.txt")

    # 3. Apply migrations
    print("Applying database migrations...")
    run_command(f"{python_exe} manage.py migrate")

    # 4. Collect static files
    print("Collecting static files...")
    run_command(f"{python_exe} manage.py collectstatic --no-input")

    # 5. Start development server
    print("Starting development server...")
    try:
        run_command(f"{python_exe} manage.py runserver")
    except KeyboardInterrupt:
        print("\nStopping server...")

if __name__ == "__main__":
    main()
