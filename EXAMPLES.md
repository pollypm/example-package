# Example Configurations

This directory contains example `.install.polly.json` configurations for different package types.

## Script Package Example
```json
{
  "installType": "script",
  "entryPoint": [
    "chmod +x main.py",
    "echo 'Setting up script package...'"
  ]
}
```

## Executable Package Example
```json
{
  "installType": "executable",
  "installExecutablePath": "/usr/local/bin/myapp",
  "entryPoint": [
    "chmod +x myapp",
    "cp myapp /usr/local/bin/myapp",
    "echo 'Executable installed to /usr/local/bin/myapp'"
  ]
}
```

## Library Package Example
```json
{
  "installType": "library",
  "entryPoint": [
    "python3 -m pip install -e .",
    "echo 'Python library installed'"
  ]
}
```

## Complex Installation Example
```json
{
  "installType": "executable",
  "installExecutablePath": "/usr/local/bin/complex-app",
  "entryPoint": [
    "echo 'Installing dependencies...'",
    "python3 -m pip install -r requirements.txt",
    "echo 'Compiling application...'",
    "make build",
    "echo 'Installing executable...'",
    "cp build/complex-app /usr/local/bin/complex-app",
    "chmod +x /usr/local/bin/complex-app",
    "echo 'Creating config directory...'",
    "mkdir -p /etc/complex-app",
    "cp config/default.conf /etc/complex-app/",
    "echo 'Installation complete!'"
  ]
}
```

## Important Notes

- **Commands run sequentially**: If any command fails, installation stops
- **Working directory**: Commands execute in the package directory
- **Permissions**: Commands run with the same privileges as Polly (typically sudo)
- **Path handling**: Use absolute paths when copying files to system locations
- **Error handling**: Keep commands simple and predictable
- **Validation**: Test your entry point commands before publishing
