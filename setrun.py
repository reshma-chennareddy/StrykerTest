import subprocess
import os

def install_dependencies():
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

def start_services():
    subprocess.Popen(["uvicorn", "service_a:app", "--host", "127.0.0.1", "--port", "8000"])
    subprocess.Popen(["uvicorn", "service_b:app", "--host", "127.0.0.1", "--port", "8001"])

if __name__ == "__main__":
    install_dependencies()
    start_services()
