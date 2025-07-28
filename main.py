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
    print("📋 Package files:")
    print("   • .polly.json - Package metadata (optional)")
    print("   • .install.polly.json - Package installation metadata (required)")
    print("   • main.py (or your entry point) - Your application code")
    print()
    print("🔧 Required install file fields:")
    print("   • install - List of commands to run during installation")
    print("   • uninstall - List of commands to run during uninstallation")
    print()
    print("✨ Example package setup complete!")


if __name__ == "__main__":
    main()
