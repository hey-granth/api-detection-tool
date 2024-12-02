#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path

def run_api_detection_tool():
    try:
        result = subprocess.run([sys.executable, '-m', 'api-detection-tool'], capture_output=True, text=True, check=True)

        if result.returncode != 0:
            print(result.stderr)
            return False

    except Exception as e:
        print(f'Error running API detection tool: {e}')
        return False


def main():
    if not run_api_detection_tool():
        sys.exit(1)
    sys.exit(0)

if __name__ == '__main__':
    main()