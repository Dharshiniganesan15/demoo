#!/usr/bin/env python3
"""
Start server with single automatic git push
"""

import os
import subprocess
import time
import sys
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run a command and return the result."""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error running {cmd}: {result.stderr}")
            return False
        print(f"Success: {cmd}")
        if result.stdout:
            print(f"Output: {result.stdout.strip()}")
        return True
    except Exception as e:
        print(f"Exception running {cmd}: {e}")
        return False

def main():
    """Main function to start server with single git push."""
    # Get the demoo directory
    demoo_dir = Path(__file__).parent
    project_root = demoo_dir.parent
    
    print(f"Project root: {project_root}")
    print(f"Demoo directory: {demoo_dir}")
    
    # Change to demoo directory for git operations
    os.chdir(demoo_dir)
    
    # 1. Add all changes
    print("\n=== Adding changes to git ===")
    if not run_command("git add ."):
        print("Failed to add changes")
        return False
    
    # 2. Commit changes
    print("\n=== Committing changes ===")
    commit_message = f"Auto-update documentation - {time.strftime('%Y-%m-%d %H:%M:%S')}"
    if not run_command(f'git commit -m "{commit_message}"'):
        print("No changes to commit or commit failed")
    
    # 3. Push to git (only once!)
    print("\n=== Pushing to git (once) ===")
    if not run_command("git push"):
        print("Failed to push to git")
        return False
    
    print("\n=== Git push completed successfully! ===")
    
    # 4. Start the server
    print("\n=== Starting FastAPI server ===")
    os.chdir(project_root)
    
    # Start the server
    try:
        import uvicorn
        print("Starting server on http://localhost:8000")
        print("Webhook URL: https://da3b21fd5fff.ngrok-free.app/webhook/git")
        print("Press Ctrl+C to stop the server")
        
        # Run the server
        uvicorn.run(
            "backend.app:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
        
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"Error starting server: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()
