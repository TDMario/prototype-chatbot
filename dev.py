import subprocess
import time
import sys

# Verwende genau den Python-Interpreter, der gerade aktiv ist
python = sys.executable

frontend = subprocess.Popen([python, "run_frontend.py"])
time.sleep(1)
backend = subprocess.Popen([python, "-m", "uvicorn", "backend.main:app", "--reload"])

try:
    frontend.wait()
    backend.wait()
except KeyboardInterrupt:
    frontend.terminate()
    backend.terminate()