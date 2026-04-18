#!/usr/bin/env python3
import subprocess
import json
from datetime import datetime

def check_container_health():
    result = subprocess.run(['docker', 'stats', '--no-stream', '--format', 
                           '{{json .}}'], capture_output=True, text=True)
    
    for line in result.stdout.strip().split('\n'):
        if line:
            stats = json.loads(line)
            cpu = float(stats['CPUPerc'].rstrip('%'))
            mem = float(stats['MemPerc'].rstrip('%'))
            
            if cpu > 80 or mem > 85:
                print(f"[ALERT] {datetime.now()} - {stats['Name']}: "
                      f"CPU {cpu}% | MEM {mem}%")

if __name__ == "__main__":
    check_container_health()
