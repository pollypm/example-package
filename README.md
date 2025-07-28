# Polly Example Package

This is a demonstration package showing the proper structure and metadata requirements for creating Polly-compatible packages.

## Package Files

### `.install.polly.json` (Required)
This is the core metadata file that Polly uses to understand how to install your package.

**Required fields:**
- `install`: a list of commands to be executed sequentially when the package is installed.
- `uninstall`: a list of commands to be executed sequentially when the package is uninstalled.

### `.polly.json` (Optional)
Additional metadata for package discovery and information display.

## Install File Format

```json
{
  "install": [
    "echo Run commands here when the package is installed!"
  ],
  "uninstall": [
    "echo Run commands here when the package is uninstalled!"
  ]
}
```

## Usage

1. **Test the example:**
   ```bash
   python3 main.py
   ```

2. **Use as template:**
   - Copy this directory structure
   - Modify `.install.polly.json` with your commands
   - Update `.polly.json` with your package information
   - Replace `main.py` with your application code

## Notes

- Install/uninstall commands are executed in the package directory during installation
- Commands run with the privleges you give them, use `sudo` to run as root
- Use absolute paths in when possible
- Test your package structure before publishing

## Learn More

- [Polly Documentation](https://github.com/pollypm/polly/wiki)
- [Package Development Guide](https://github.com/pollypm/polly/wiki/Package-Development)
- [Polly Repository](https://github.com/pollypm/polly)
