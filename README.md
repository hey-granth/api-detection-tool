[//]: # (i sometimes mistakenly push my API keys onto github without adding it onto gitignore file. Since it;s really tough to clean the commit history and remove it from github, i have planned to make a python api detection tool which warns me if i accidentally add a file with any sensitive api key info to git bash on the terminal itself.)

# API Key Detector

## Overview

API Key Detector is a sophisticated security tool designed to prevent accidental exposure of sensitive credentials during Git commits. By implementing intelligent scanning mechanisms, the tool helps developers maintain robust security practices and protect confidential access tokens.

## Key Features

### Advanced Secret Detection
- Multi-pattern secret identification
- Comprehensive scanning of staged Git files
- Support for various credential formats (API keys, tokens, environment variables)
- Configurable detection strategies

### Flexible Integration
- Seamless Git pre-commit hook integration
- Command-line interface for manual scanning
- Lightweight and non-intrusive design

### Intelligent Filtering
- Automatic exclusion of large files
- Skip logic for binary and non-source files
- Configurable ignore patterns

---
## Installation

### Prerequisites
- Python 3.8+
- Git 2.0+

### Package Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/api-key-detector.git

# Navigate to project directory
cd api-key-detector

# Install the package
pip install .
```

## Configuration

### Detection Patterns
Customize secret detection by modifying patterns in `src/api_key_detector/core.py`. The default configuration supports:
- Generic long-string patterns
- Service-specific key formats (Stripe, AWS)
- Environment variable detection
- URL-based key identification

### Git Hook Setup
1. Copy the pre-commit hook script:
```bash
cp git_hooks/pre_commit.py .git/hooks/pre_commit
chmod +x .git/hooks/pre_commit
```

---
## Usage

### Automatic Git Hook Detection
- Automatically runs before each commit
- Blocks commits containing potential secrets
- Provides detailed error messages

### Manual Scanning
```bash
# Scan staged files
python -m api_key_detector

# Bypass detection (use with caution)
git commit --no-verify
```

## Best Practices

1. Always review detected potential secrets
2. Use environment variable management tools
3. Rotate credentials regularly
4. Never commit sensitive information directly

## Troubleshooting

### Common Issues
- False positives in detection
- Performance with large repositories
- Compatibility with different Git workflows

*Solution*: Customize detection patterns and filtering logic in the configuration files.

---
## Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Write comprehensive tests
5. Submit a pull request

### Reporting Issues
- Use GitHub Issues
- Provide detailed reproduction steps
- Include relevant configuration and environment details

## Security

This tool is designed to enhance security awareness. It is not a comprehensive security solution and should be used as part of a broader security strategy.

---
## Contact

Maintainer: [Granth Agarwal](https://gtithub.com/hey-granth)

Email: [heygranth@gmail.com](mailto:heygranth@gmail.com)