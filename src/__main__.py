import sys
import logging
from pathlib import Path

from core import APIKeyDetector
from utils import get_git_staged_files, skip_file


def main():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    logger = logging.getLogger(__name__)

    try:
        detector = APIKeyDetector()
        staged_files = get_git_staged_files()
        detected_secrets = []
        for file in staged_files:
            if skip_file(file):
                logger.info(f"Skipping file: {file}")
                continue

            logger.info(f"Scanning file: {file}")
            secrets = detector.scan_file(file)
            if secrets:
                detected_secrets.extend(
                    [{**secret, "file": file} for secret in secrets]
                )

        if detected_secrets:
            logger.error("⚠️ Potential API keys detected:\n")
            for secret in detected_secrets:
                logger.error(
                    f'Secret detected in file: {secret["file"]}\nline: {secret["line_number"]}\npattern: {secret["pattern"]}'
                )
            print(
                "\nTo bypass this check, add the file path to .gitignore or skip the file using the skip_patterns in utils.py\nOr you can simply use the command: ```git commit --no-verify``` to bypass the pre-commit hook."
            )
            sys.exit(1)

        logger.info("✅ No API keys detected. Proceeding with commit...")
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
