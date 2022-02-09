import sys
import subprocess

subprocess.Popen(
    ["chmod", "+x", "storagespace"],   
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)

subprocess.Popen(
    ["chmod", "+x", "algorithm"],   
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)
