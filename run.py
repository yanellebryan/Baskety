import os
import subprocess
import sys

def main():
    # Define the project directory
    project_root = os.path.dirname(os.path.abspath(__file__))
    baskety_dir = os.path.join(project_root, 'Baskety')

    # Check if directory exists
    if not os.path.exists(baskety_dir):
        print(f"Error: Directory '{baskety_dir}' does not exist.")
        return

    print(f"Starting Baskety POS System from {baskety_dir}...")
    
    try:
        # Run Django Server
        subprocess.run([sys.executable, 'manage.py', 'runserver'], cwd=baskety_dir)
            
    except KeyboardInterrupt:
        print("\nStopping server...")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
