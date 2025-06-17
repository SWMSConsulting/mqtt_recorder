import subprocess

for num in range(1, 4):
    # Example: replace /6/d/ with /{num}/a/
    replace_from = "/6/d/"
    replace_to = f"/{num}/a/"
    cmd = [
        "python", "-m", "mqtt_recorder",
        "--host", "localhost",
        "--mode", "replay",
        "--loop", "True",
        "--file", "recording.csv",
        "--replace_from", replace_from,
        "--replace_to", replace_to,
        "--client_id", f"replay_{num}",
        "--encode_b64"
    ]
    subprocess.Popen(cmd)