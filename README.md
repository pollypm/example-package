# Polly Example Package

This is a demonstration package showing the proper structure and metadata requirements for creating Polly-compatible packages.

## 📋 Required Files

### `.install.polly.json` (Required)
This is the core metadata file that Polly uses to understand how to install your package.

**Required fields:**
- `installType`: Must be one of `"executable"`, `"library"`, or `"script"`
- `entryPoint`: Array of shell commands to run during installation

**Conditional requirements:**
- If `installType` is `"executable"`, you must also include `installExecutablePath`

### `.polly.json` (Optional)
Additional metadata for package discovery and information display.

## 🔧 Install Types

### `"script"`
For packages that are scripts or need setup commands to run.
```json
{
  "installType": "script",
  "entryPoint": [
    "chmod +x main.py",
    "echo 'Setup complete'"
  ]
}
```

### `"executable"`
For packages that should be installed as system executables.
```json
{
  "installType": "executable",
  "installExecutablePath": "/usr/local/bin/myapp",
  "entryPoint": [
    "chmod +x main.py",
    "cp main.py /usr/local/bin/myapp"
  ]
}
```

### `"library"`
For packages that are libraries or modules.
```json
{
  "installType": "library",
  "entryPoint": [
    "pip install -e .",
    "echo 'Library installed'"
  ]
}
```

## 🚀 Usage

1. **Test the example:**
   ```bash
   python3 main.py
   ```

2. **Use as template:**
   - Copy this directory structure
   - Modify `.install.polly.json` with your requirements
   - Update `.polly.json` with your package information
   - Replace `main.py` with your application code

## 📝 Notes

- Entry point commands are executed in the package directory during installation
- Commands run with the same privileges as the Polly installation (typically requires sudo)
- Use absolute paths in entry point commands when possible
- Test your package structure before publishing

## 🔗 Learn More

- [Polly Documentation](https://github.com/pollypm/polly/wiki)
- [Package Development Guide](https://github.com/pollypm/polly/wiki/Package-Development)
- [Polly Repository](https://github.com/pollypm/polly)
