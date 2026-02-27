"""
AI Documentation Function - Single Function for Documentation Generation
This module provides a simple function to generate documentation for any repository.
"""

import os
import subprocess
import tempfile
import shutil
from datetime import datetime
import git
from aisystemdoc.doc_generator import generate_docs

def generate_ai_documentation(repo_url: str, repo_name: str = None) -> dict:
    """
    Generate AI documentation for a repository.
    
    Args:
        repo_url: GitHub repository URL
        repo_name: Optional repository name (extracted from URL if not provided)
    
    Returns:
        Dictionary with processing results
    """
    try:
        # Extract repo name from URL if not provided
        if not repo_name:
            repo_name = repo_url.split('/')[-1].replace('.git', '')
        
        print(f"🚀 Starting AI documentation generation for: {repo_name}")
        print(f"📥 Repository URL: {repo_url}")
        
        # Create temporary directory for cloning
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_repo_path = os.path.join(temp_dir, repo_name)
            
            print(f"📁 Cloning repository to: {temp_repo_path}")
            
            # Clone repository
            try:
                repo = git.Repo.clone_from(repo_url, temp_repo_path)
                print("✅ Repository cloned successfully")
            except Exception as e:
                return {
                    "status": "error",
                    "message": f"Failed to clone repository: {str(e)}",
                    "repo_name": repo_name
                }
            
            # Generate documentation
            print("🤖 Generating AI documentation...")
            try:
                doc_success = generate_docs(temp_repo_path)
                if doc_success:
                    print("✅ Documentation generated successfully")
                else:
                    print("⚠️ Documentation generation completed with warnings")
            except Exception as e:
                return {
                    "status": "error", 
                    "message": f"Documentation generation failed: {str(e)}",
                    "repo_name": repo_name
                }
            
            # Check if README was created/updated
            readme_path = os.path.join(temp_repo_path, "README.md")
            readme_exists = os.path.exists(readme_path)
            readme_size = os.path.getsize(readme_path) if readme_exists else 0
            
            # Get git status
            try:
                repo = git.Repo(temp_repo_path)
                is_dirty = repo.is_dirty(untracked_files=True)
                
                if is_dirty:
                    print("📝 Committing documentation changes...")
                    
                    # Add all changes
                    repo.git.add(A=True)
                    
                    # Commit changes
                    commit_message = f"Update documentation by AI system - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                    repo.git.commit('-m', commit_message)
                    
                    print("✅ Changes committed locally")
                    
                    # Push changes back to GitHub
                    print("🚀 Pushing changes to GitHub...")
                    try:
                        origin = repo.remote(name='origin')
                        origin.push()
                        print("✅ Changes pushed to GitHub successfully")
                        pushed = True
                    except Exception as push_error:
                        print(f"⚠️ Push failed: {str(push_error)}")
                        pushed = False
                else:
                    print("ℹ️ No changes to commit")
                    pushed = True
                    
            except Exception as git_error:
                return {
                    "status": "error",
                    "message": f"Git operations failed: {str(git_error)}",
                    "repo_name": repo_name
                }
            
            # Return success result
            result = {
                "status": "success",
                "repo_name": repo_name,
                "repo_url": repo_url,
                "documentation_generated": doc_success,
                "readme_exists": readme_exists,
                "readme_size_bytes": readme_size,
                "changes_committed": is_dirty,
                "pushed_to_github": pushed,
                "timestamp": datetime.now().isoformat(),
                "message": "AI documentation generated and processed successfully"
            }
            
            print(f"🎉 Documentation process completed for {repo_name}")
            print(f"📊 Results: Generated={doc_success}, Pushed={pushed}")
            
            return result
            
    except Exception as e:
        return {
            "status": "error",
            "message": f"Unexpected error: {str(e)}",
            "repo_name": repo_name or "unknown"
        }

def quick_documentation(repo_url: str) -> str:
    """
    Quick documentation generation with simple status message.
    
    Args:
        repo_url: GitHub repository URL
        
    Returns:
        Status message string
    """
    result = generate_ai_documentation(repo_url)
    
    if result["status"] == "success":
        return f"✅ Documentation generated for {result['repo_name']} - Pushed to GitHub: {result['pushed_to_github']}"
    else:
        return f"❌ Failed to generate documentation for {result['repo_name']}: {result['message']}"

# Example usage and testing
if __name__ == "__main__":
    print("🤖 AI Documentation Function - Test")
    print("=" * 50)
    
    # Test with your repository
    test_repo_url = "https://github.com/Dharshiniganesan15/demoo.git"
    
    print(f"🧪 Testing with: {test_repo_url}")
    print()
    
    # Generate documentation
    result = generate_ai_documentation(test_repo_url)
    
    print("📊 Full Result:")
    for key, value in result.items():
        print(f"  {key}: {value}")
    
    print()
    print("🎯 Quick usage:")
    print("from ai_documentation_function import generate_ai_documentation")
    print("result = generate_ai_documentation('https://github.com/user/repo.git')")
    print("print(result['status'])  # 'success' or 'error'")
