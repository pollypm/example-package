#!/usr/bin/env python3
"""
Polly Example Package

This is a simple example package that demonstrates how to create
a Polly-compatible package with proper metadata structure.
"""


def main():
    print("🎉 Hello from Polly Example Package!")
    print("📦 This package demonstrates the basic structure")
    print("   required for Polly packages.")
    print()
    print("📋 Required files:")
    print("   • .install.polly.json - Package installation metadata")
    print("   • main.py (or your entry point) - Your application code")
    print()
    print("🔧 Required metadata fields:")
    print("   • installType: 'executable', 'library', or 'script'")
    print("   • entryPoint: list of commands to run during installation")
    print("   • installExecutablePath: (required for executable type)")
    print()
    print("✨ Example package setup complete!")


if __name__ == "__main__":
    main()
