import sys
import subprocess

subprocess.Popen(
    ["chmod", "+x", "storagespace"],   
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

subprocess.Popen(
    ["chmod", "+x", "algorithm"],   
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
