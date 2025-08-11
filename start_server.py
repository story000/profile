#!/usr/bin/env python3
"""
Portfolio Server Startup Script
Run this script to start the portfolio website with FastAPI backend.
"""

import subprocess
import sys
import os
from pathlib import Path

def install_requirements():
    """Install required packages"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False
    return True

def start_server():
    """Start the FastAPI server"""
    try:
        print("🚀 Starting portfolio server...")
        print("📁 Server will serve files from current directory")
        print("🌐 Portfolio will be available at: http://localhost:8000")
        print("📊 API documentation at: http://localhost:8000/docs")
        print("\nPress Ctrl+C to stop the server\n")
        
        subprocess.run([sys.executable, "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"])
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to start server: {e}")

def main():
    """Main function"""
    print("🎯 Portfolio Website Startup")
    print("=" * 30)
    
    # Check if we're in the right directory
    if not Path("portfolio_config.yaml").exists():
        print("❌ portfolio_config.yaml not found in current directory")
        print("Please run this script from the portfolio directory")
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    # Start server
    start_server()

if __name__ == "__main__":
    main()