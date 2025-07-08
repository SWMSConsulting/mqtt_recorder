import subprocess
import sys

python_exe = sys.executable  # Automatically uses the current Python interpreter

procs = []
for num in range(1, 4):
    # Example: replace /6/d/ with /{num}/a/
    replace_from = "/6/d/"
    replace_to = f"/{num}/c/"
    cmd = [
        python_exe, "-m", "mqtt_recorder",
        "--host", "95.216.77.248",
        "--mode", "replay",
        "--loop", "True",
        "--file", "recording2.csv",
        "--replace_from", replace_from,
        "--replace_to", replace_to,
        "--client_id", f"replay_{num}",
        "--encode_b64"
    ]
    procs.append(subprocess.Popen(cmd))

# Wait for all subprocesses to finish
for p in procs:
    p.wait()