import subprocess
from typing import List
from pathlib import Path

def get_get_staged_files() -> List[Path]:
    try:
        staged_files = subprocess.run(['git', 'diff', '--staged', '--name-only'], capture_output=True, text=True, check=True)
        return [Path(file) for file in staged_files.stdout.split('\n') if file]

    except subprocess.CalledProcessError as e:
        print(f'Error getting staged files: {e}')
        return []

def skip_file(file_path: Path) -> bool:
    skip_patterns = ['node_modules', 'venv', '.git', '.idea', '.vscode', '.egg-info', '.pytest_cache', '__pycache__', '.tox', '.mypy_cache', '.serverless', '.terraform', '.k8s', '.helm', '.docker', '.github', '.gitlab', '.circleci', '.travis', '.azure-pipelines', '.jenkins', '.sonarqube', '.nyc_output', '.serverless', 'env', '.venv']
    skip_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.mp4', '.mp3', '.avi', '.mov', '.wav', '.aif', '.zip', '.tar', '.gz', '.7z', '.rar', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.key', '.psd', '.ai', '.sketch', '.exe', '.dll', '.so', '.app', '.apk', '.dmg', '.iso', '.bin', '.jar', '.war', '.ear', '.swf', '.fla', '.flv', '.wmv', '.avi', '.mov', '.mpg', '.mpeg', '.mkv', '.webm', '.m4v', '.m4a', '.flac', '.ogg', '.wav', '.mp3', '.mp4', '.m4v', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.webm', '.m4a', '.flac', '.ogg', '.wav', '.mp3', '.mp4', '.m4v', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.webm', '.m4a', '.flac', '.ogg', '.wav', '.mp3', '.mp4', '.m4v', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.webm', '.m4a', '.flac', '.ogg', '.wav', '.mp3', '.mp4', '.m4v', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.webm', '.m4a', '.flac', '.ogg', '.wav', '.mp3', '.mp4', '.m4v', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.webm', '.m4a', '.flac', '.ogg', '.wav', '.mp3', '.mp4', '.m4v', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.webm', '.m4a', '.flac', '.ogg', '.wav', '.mp3', '.mp4', '.m4v', '.mov', '.avi', '.', '.wmv', '.flv', '.mkv', '.webm', '.m4a', '.flac', '.ogg', '.wav', '.mp3', '.mp4', '.m4v', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.webm', '.m4a', '.flac', '.ogg', '.wav', '.mp3', '.mp4', '.m4v', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.webm', '.m4a', '.flac', '.ogg', '.wav', '.mp3', '.mp4', '.m4v', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.webm', '.m4a', '.flac', '.ogg', '.wav', '.mp3', '.mp4', '.m4v', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.webm', '.m4a', '.flac', '.ogg', '.wav', '.mp3', '.mp4', '.m4v', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.webm', '.m4a', '.flac', '.ogg', '.wav', '.mp3', '.mp4', '.m4v', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.webm', '.m4a', '.flac', '.ogg', '.wav', '.mp3', '.mp4', '.m4v', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.webm', '.m4a', '.flac', '.ogg', '.wav', '.mp3', '.mp4', '.m4v', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.webm', '.m4a', '.flac', '.ogg', '.wav', '.mp3', '.mp4', '.m4v', '.mov', '.avi', '.wmv', '.flv', '.mkv', '.webm', '.m4a', '.flac', '.ogg', '.wav', '.mp3', '.mp4', '.m4v', '.mov', '.avi']

    return any([pattern in str(file_path) for pattern in skip_patterns]) or file_path.suffix.lower() in skip_extensions