import re
import logging
from typing import List, Dict, Optional
from pathlib import Path

class APIKeyDetector:

    def __init__(self, log_level: int = logging.INFO):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        # secret key patterns
        self._secret_patterns = [
            r'[a-zA-Z0-9_-]{32,}',
            r'(?i)sk_(?:test|live)_[a-zA-Z0-9]+',
            r'(?i)live_[a-zA-Z0-9]{16}',
            r'(?i)secret_[a-zA-Z0-9,_-]{32,}',
            r'(?i)private_[a-zA-Z0-9]{16}',
            r'(?i)Bearer [a-zA-Z0-9_-]{32,}',
            r'(?i)Basic [a-zA-Z0-9_-]{32,}',
            r'AKIA[0-9A-Z]{16}',
            r'(?i)(api[_-]key|secret|token|password)[\s]*[=:]\s*[\'"]*([^\s\'"]+)',
            r'https?://[^/\s]+/[^\s]*?(?:key|token|secret)=[a-zA-Z0-9_-]+'
        ]

    def detect_secrets(self, content: str) -> List[Dict[str, str]]:
        secrets = []
        for pattern in self._secret_patterns:
            # find all matches while being case-insensitive
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                secrets.append({
                    'secret': match.group(0),
                    'line_number': content[match.start()].count('\n', 0, match.start()) + 1,
                    'pattern': pattern
                })

        return secrets

    def scan_folder(self, folder: Path) -> Optional[List[Dict[str, str]]]:
        secrets = []
        for file in folder.rglob('*'):
            if file.is_file():
                with open(file, 'r') as f:
                    content = f.read()
                    secrets += self.detect_secrets(content)
        return secrets

    def scan_file(self, file: Path) -> Optional[List[Dict[str, str]]]:
        try:
            # skips large and binary files
            if file.stat().st_size > 1024 * 1024:
                self.logger.warning(f'Skipping large file: {file}')
                return None

            content = file.read_text(encoding='utf-8')
            return self.detect_secrets(content)

        except (PermissionError, UnicodeDecodeError) as e:
            self.logger.error(f'Error reading file: {file}, {e}')
            return None
