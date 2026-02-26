"""
Smart Webhook Feature Module
This module demonstrates the webhook-based documentation system functionality.
"""

import json
import hashlib
from datetime import datetime
from typing import Dict, Any, Optional

class WebhookProcessor:
    """
    Processes GitHub webhooks for automatic documentation updates.
    """
    
    def __init__(self, webhook_secret: str):
        self.webhook_secret = webhook_secret
        self.processed_commits = []
    
    def verify_webhook_signature(self, payload: str, signature: str) -> bool:
        """
        Verify GitHub webhook signature for security.
        
        Args:
            payload: The webhook payload body
            signature: The X-Hub-Signature-256 header
            
        Returns:
            True if signature is valid, False otherwise
        """
        expected_signature = "sha256=" + hashlib.sha256(
            (self.webhook_secret + payload).encode('utf-8')
        ).hexdigest()
        
        return hmac.compare_digest(expected_signature, signature)
    
    def analyze_commit_changes(self, commit_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze commit changes to determine if documentation update is needed.
        
        Args:
            commit_data: GitHub commit information
            
        Returns:
            Analysis results with change detection
        """
        added_files = commit_data.get('added', [])
        modified_files = commit_data.get('modified', [])
        removed_files = commit_data.get('removed', [])
        
        # Check if documentation-relevant files changed
        code_extensions = {'.py', '.js', '.ts', '.java', '.html', '.css', '.md'}
        
        relevant_changes = []
        
        for file_list in [added_files, modified_files]:
            for file_path in file_list:
                if any(file_path.endswith(ext) for ext in code_extensions):
                    relevant_changes.append(file_path)
        
        return {
            'has_relevant_changes': len(relevant_changes) > 0,
            'relevant_files': relevant_changes,
            'total_changes': len(added_files) + len(modified_files) + len(removed_files),
            'analysis_timestamp': datetime.now().isoformat()
        }
    
    def generate_documentation_update(self, repo_name: str, commit_hash: str) -> Dict[str, Any]:
        """
        Generate documentation update for the repository.
        
        Args:
            repo_name: Name of the repository
            commit_hash: Git commit hash
            
        Returns:
            Documentation update information
        """
        update_info = {
            'repo_name': repo_name,
            'commit_hash': commit_hash,
            'update_type': 'automatic',
            'generated_at': datetime.now().isoformat(),
            'status': 'pending',
            'files_updated': ['README.md'],
            'ai_analysis': 'Changes detected in core functionality requiring documentation update'
        }
        
        # Simulate AI processing
        update_info['ai_confidence'] = 0.85
        update_info['estimated_quality'] = 'high'
        
        return update_info
    
    def process_webhook_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process incoming webhook payload and coordinate documentation update.
        
        Args:
            payload: GitHub webhook payload
            
        Returns:
            Processing results
        """
        try:
            # Extract repository and commit information
            repo_data = payload.get('repository', {})
            commits = payload.get('commits', [])
            
            if not commits:
                return {'status': 'no_commits', 'message': 'No commits found in webhook'}
            
            latest_commit = commits[0]
            repo_name = repo_data.get('name', 'unknown')
            commit_hash = latest_commit.get('id', 'unknown')
            
            # Analyze changes
            analysis = self.analyze_commit_changes(latest_commit)
            
            # Generate documentation update if needed
            doc_update = None
            if analysis['has_relevant_changes']:
                doc_update = self.generate_documentation_update(repo_name, commit_hash)
            
            # Record processing
            processing_result = {
                'status': 'success',
                'repo_name': repo_name,
                'commit_hash': commit_hash,
                'analysis': analysis,
                'documentation_update': doc_update,
                'processed_at': datetime.now().isoformat()
            }
            
            self.processed_commits.append(processing_result)
            
            return processing_result
            
        except Exception as e:
            return {
                'status': 'error',
                'error_message': str(e),
                'processed_at': datetime.now().isoformat()
            }

class DocumentationGenerator:
    """
    Generates documentation using AI analysis.
    """
    
    def __init__(self, ai_model: str = "gemini-2.5-flash"):
        self.ai_model = ai_model
        self.generation_history = []
    
    def analyze_code_structure(self, file_paths: list) -> Dict[str, Any]:
        """
        Analyze code structure for documentation generation.
        
        Args:
            file_paths: List of code file paths
            
        Returns:
            Code structure analysis
        """
        structure = {
            'total_files': len(file_paths),
            'file_types': {},
            'complexity_score': 0,
            'documentation_needs': []
        }
        
        for file_path in file_paths:
            # Determine file type
            if file_path.endswith('.py'):
                structure['file_types']['python'] = structure['file_types'].get('python', 0) + 1
                structure['complexity_score'] += 2
            elif file_path.endswith('.js'):
                structure['file_types']['javascript'] = structure['file_types'].get('javascript', 0) + 1
                structure['complexity_score'] += 1.5
            elif file_path.endswith('.html'):
                structure['file_types']['html'] = structure['file_types'].get('html', 0) + 1
                structure['complexity_score'] += 1
            elif file_path.endswith('.css'):
                structure['file_types']['css'] = structure['file_types'].get('css', 0) + 1
                structure['complexity_score'] += 0.5
        
        # Determine documentation needs
        if structure['complexity_score'] > 5:
            structure['documentation_needs'].append('comprehensive_api_docs')
        if structure['file_types'].get('python', 0) > 0:
            structure['documentation_needs'].append('function_documentation')
        if structure['file_types'].get('html', 0) > 0:
            structure['documentation_needs'].append('component_documentation')
        
        return structure
    
    def generate_readme_content(self, repo_name: str, structure: Dict[str, Any]) -> str:
        """
        Generate README.md content based on code structure analysis.
        
        Args:
            repo_name: Repository name
            structure: Code structure analysis
            
        Returns:
            Generated README content
        """
        readme_content = f"""# {repo_name}

## Overview
This repository contains a {structure['total_files']}-file project with mixed technology stack.

## Technology Stack
"""
        
        for file_type, count in structure['file_types'].items():
            readme_content += f"- {file_type.title()}: {count} files\n"
        
        readme_content += f"""
## Complexity Score: {structure['complexity_score']}/10

## Documentation Needs
"""
        
        for need in structure['documentation_needs']:
            readme_content += f"- {need.replace('_', ' ').title()}\n"
        
        readme_content += """
## Installation
```bash
# Clone the repository
git clone <repository-url>
cd <repository-name>

# Install dependencies
# Add installation instructions here
```

## Usage
```python
# Add usage examples here
```

## Features
- Automated documentation generation
- Smart webhook integration
- AI-powered code analysis
- Real-time updates

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License
MIT License - see LICENSE file for details

---
*This documentation was automatically generated by the AI Documentation System.*
"""
        
        return readme_content

# Example usage and testing
if __name__ == "__main__":
    # Create webhook processor
    processor = WebhookProcessor("demo_webhook_secret")
    
    # Example webhook payload
    example_payload = {
        "repository": {
            "name": "demoo",
            "clone_url": "https://github.com/user/demoo.git"
        },
        "commits": [
            {
                "id": "abc123def456",
                "added": ["smart_webhook_feature.py"],
                "modified": ["main.py"],
                "removed": []
            }
        ]
    }
    
    # Process the webhook
    result = processor.process_webhook_payload(example_payload)
    print("Webhook Processing Result:")
    print(json.dumps(result, indent=2))
    
    # Create documentation generator
    doc_gen = DocumentationGenerator()
    
    # Analyze code structure
    structure = doc_gen.analyze_code_structure(["smart_webhook_feature.py", "main.py"])
    print("\nCode Structure Analysis:")
    print(json.dumps(structure, indent=2))
    
    # Generate README
    readme = doc_gen.generate_readme_content("demoo", structure)
    print("\nGenerated README Content:")
    print(readme)
