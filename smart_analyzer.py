"""
Smart Code Analyzer - Advanced AI-Powered Code Analysis Tool
This module provides intelligent code analysis capabilities with multiple analysis modes.
"""

import os
import re
import ast
import json
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from pathlib import Path

@dataclass
class CodeMetrics:
    """Data class for storing code metrics"""
    total_lines: int
    code_lines: int
    comment_lines: int
    blank_lines: int
    functions: int
    classes: int
    complexity_score: float
    documentation_coverage: float

@dataclass
class FunctionInfo:
    """Data class for function information"""
    name: str
    line_number: int
    parameters: List[str]
    docstring: Optional[str]
    complexity: int
    decorators: List[str]

@dataclass
class ClassInfo:
    """Data class for class information"""
    name: str
    line_number: int
    methods: List[FunctionInfo]
    base_classes: List[str]
    docstring: Optional[str]

class SmartCodeAnalyzer:
    """
    Advanced AI-powered code analyzer with multiple analysis capabilities.
    """
    
    def __init__(self, gemini_api_key: str = None):
        self.gemini_api_key = gemini_api_key
        self.supported_extensions = {'.py', '.js', '.ts', '.java', '.html', '.css'}
        self.analysis_results = {}
    
    def analyze_repository(self, repo_path: str) -> Dict[str, Any]:
        """
        Analyze entire repository comprehensively.
        
        Args:
            repo_path: Path to the repository
            
        Returns:
            Complete analysis results dictionary
        """
        print(f"🔍 Starting comprehensive repository analysis...")
        print(f"📁 Repository path: {repo_path}")
        
        results = {
            'repository_path': repo_path,
            'analysis_timestamp': datetime.now().isoformat(),
            'files_analyzed': 0,
            'total_files': 0,
            'file_types': {},
            'code_metrics': {},
            'functions': [],
            'classes': [],
            'security_issues': [],
            'performance_suggestions': [],
            'documentation_quality': {},
            'complexity_analysis': {},
            'ai_insights': None
        }
        
        # Find all code files
        code_files = self._find_code_files(repo_path)
        results['total_files'] = len(code_files)
        
        print(f"📊 Found {len(code_files)} code files")
        
        # Analyze each file
        for file_path in code_files:
            try:
                file_analysis = self._analyze_file(file_path)
                if file_analysis:
                    self._merge_file_analysis(results, file_analysis)
                    results['files_analyzed'] += 1
            except Exception as e:
                print(f"⚠️ Error analyzing {file_path}: {str(e)}")
        
        # Generate AI insights if API key available
        if self.gemini_api_key:
            results['ai_insights'] = self._generate_ai_insights(results)
        
        # Calculate overall metrics
        results['summary'] = self._calculate_summary_metrics(results)
        
        print(f"✅ Analysis complete: {results['files_analyzed']}/{results['total_files']} files processed")
        
        return results
    
    def _find_code_files(self, repo_path: str) -> List[str]:
        """Find all supported code files in repository."""
        code_files = []
        repo_path = Path(repo_path)
        
        for file_path in repo_path.rglob('*'):
            if file_path.is_file() and file_path.suffix in self.supported_extensions:
                # Skip common non-source directories
                if any(skip in str(file_path) for skip in ['__pycache__', 'venv', '.git', 'node_modules', 'target', 'build']):
                    continue
                code_files.append(str(file_path))
        
        return code_files
    
    def _analyze_file(self, file_path: str) -> Optional[Dict[str, Any]]:
        """Analyze individual code file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            file_ext = Path(file_path).suffix
            relative_path = os.path.relpath(file_path)
            
            analysis = {
                'file_path': relative_path,
                'file_type': file_ext,
                'size_bytes': len(content.encode('utf-8')),
                'lines': len(content.splitlines()),
                'metrics': None,
                'functions': [],
                'classes': [],
                'imports': [],
                'security_issues': [],
                'complexity_indicators': []
            }
            
            # Language-specific analysis
            if file_ext == '.py':
                analysis.update(self._analyze_python_file(content, file_path))
            elif file_ext in ['.js', '.ts']:
                analysis.update(self._analyze_javascript_file(content, file_path))
            elif file_ext == '.java':
                analysis.update(self._analyze_java_file(content, file_path))
            elif file_ext == '.html':
                analysis.update(self._analyze_html_file(content, file_path))
            elif file_ext == '.css':
                analysis.update(self._analyze_css_file(content, file_path))
            
            # Calculate basic metrics
            analysis['metrics'] = self._calculate_basic_metrics(content)
            
            return analysis
            
        except Exception as e:
            print(f"❌ Error analyzing file {file_path}: {str(e)}")
            return None
    
    def _analyze_python_file(self, content: str, file_path: str) -> Dict[str, Any]:
        """Analyze Python file specifically."""
        try:
            tree = ast.parse(content)
            analysis = {
                'functions': [],
                'classes': [],
                'imports': [],
                'complexity_score': 0
            }
            
            # Extract imports
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        analysis['imports'].append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ''
                    for alias in node.names:
                        analysis['imports'].append(f"{module}.{alias.name}")
            
            # Extract functions and classes
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    func_info = self._extract_function_info(node, content)
                    analysis['functions'].append(func_info)
                    analysis['complexity_score'] += func_info['complexity']
                
                elif isinstance(node, ast.ClassDef):
                    class_info = self._extract_class_info(node, content)
                    analysis['classes'].append(class_info)
            
            # Security analysis
            analysis['security_issues'] = self._analyze_python_security(content)
            
            return analysis
            
        except SyntaxError as e:
            return {'syntax_error': str(e), 'functions': [], 'classes': [], 'imports': []}
    
    def _extract_function_info(self, node: ast.FunctionDef, content: str) -> Dict[str, Any]:
        """Extract detailed function information."""
        lines = content.splitlines()
        
        # Get parameters
        parameters = []
        for arg in node.args.args:
            parameters.append(arg.arg)
        
        # Get docstring
        docstring = ast.get_docstring(node)
        
        # Calculate complexity (simplified cyclomatic complexity)
        complexity = 1
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.Try)):
                complexity += 1
        
        # Get decorators
        decorators = []
        for decorator in node.decorator_list:
            if isinstance(decorator, ast.Name):
                decorators.append(decorator.id)
            elif isinstance(decorator, ast.Attribute):
                decorators.append(ast.unparse(decorator))
        
        return {
            'name': node.name,
            'line_number': node.lineno,
            'parameters': parameters,
            'docstring': docstring,
            'complexity': complexity,
            'decorators': decorators,
            'has_docstring': docstring is not None,
            'line_count': node.end_lineno - node.lineno + 1 if hasattr(node, 'end_lineno') else 0
        }
    
    def _extract_class_info(self, node: ast.ClassDef, content: str) -> Dict[str, Any]:
        """Extract detailed class information."""
        # Get base classes
        base_classes = []
        for base in node.bases:
            if isinstance(base, ast.Name):
                base_classes.append(base.id)
        
        # Get docstring
        docstring = ast.get_docstring(node)
        
        # Extract methods
        methods = []
        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                method_info = self._extract_function_info(item, content)
                methods.append(method_info)
        
        return {
            'name': node.name,
            'line_number': node.lineno,
            'base_classes': base_classes,
            'docstring': docstring,
            'methods': methods,
            'has_docstring': docstring is not None,
            'method_count': len(methods)
        }
    
    def _calculate_basic_metrics(self, content: str) -> CodeMetrics:
        """Calculate basic code metrics."""
        lines = content.splitlines()
        total_lines = len(lines)
        
        code_lines = 0
        comment_lines = 0
        blank_lines = 0
        
        for line in lines:
            stripped = line.strip()
            if not stripped:
                blank_lines += 1
            elif stripped.startswith('#') or stripped.startswith('//') or stripped.startswith('/*') or stripped.startswith('*'):
                comment_lines += 1
            else:
                code_lines += 1
        
        # Simple complexity calculation
        complexity_indicators = ['if', 'for', 'while', 'try', 'except', 'elif', 'else']
        complexity_score = sum(content.count(indicator) for indicator in complexity_indicators)
        
        # Documentation coverage
        docstring_count = content.count('"""') + content.count("'''") + content.count('/*')
        documentation_coverage = (docstring_count / max(total_lines, 1)) * 100
        
        return CodeMetrics(
            total_lines=total_lines,
            code_lines=code_lines,
            comment_lines=comment_lines,
            blank_lines=blank_lines,
            functions=0,  # Will be filled by language-specific analysis
            classes=0,     # Will be filled by language-specific analysis
            complexity_score=complexity_score,
            documentation_coverage=documentation_coverage
        )
    
    def _analyze_python_security(self, content: str) -> List[Dict[str, Any]]:
        """Analyze Python code for security issues."""
        security_issues = []
        
        # Check for dangerous functions
        dangerous_patterns = {
            r'eval\s*\(': {'severity': 'high', 'issue': 'Use of eval() function'},
            r'exec\s*\(': {'severity': 'high', 'issue': 'Use of exec() function'},
            r'shell=True': {'severity': 'medium', 'issue': 'Shell injection risk'},
            r'pickle\.loads?\s*\(': {'severity': 'medium', 'issue': 'Unsafe pickle usage'},
            r'subprocess\.call': {'severity': 'low', 'issue': 'Subprocess usage without validation'},
        }
        
        for pattern, info in dangerous_patterns.items():
            if re.search(pattern, content, re.IGNORECASE):
                security_issues.append({
                    'type': 'security_vulnerability',
                    'severity': info['severity'],
                    'issue': info['issue'],
                    'pattern': pattern
                })
        
        return security_issues
    
    def _analyze_javascript_file(self, content: str, file_path: str) -> Dict[str, Any]:
        """Analyze JavaScript/TypeScript file."""
        return {
            'functions': self._extract_js_functions(content),
            'classes': self._extract_js_classes(content),
            'imports': self._extract_js_imports(content),
            'security_issues': self._analyze_js_security(content)
        }
    
    def _analyze_java_file(self, content: str, file_path: str) -> Dict[str, Any]:
        """Analyze Java file."""
        return {
            'functions': self._extract_java_methods(content),
            'classes': self._extract_java_classes(content),
            'imports': self._extract_java_imports(content),
            'security_issues': self._analyze_java_security(content)
        }
    
    def _analyze_html_file(self, content: str, file_path: str) -> Dict[str, Any]:
        """Analyze HTML file."""
        return {
            'tags': self._extract_html_tags(content),
            'forms': self._extract_html_forms(content),
            'security_issues': self._analyze_html_security(content)
        }
    
    def _analyze_css_file(self, content: str, file_path: str) -> Dict[str, Any]:
        """Analyze CSS file."""
        return {
            'selectors': self._extract_css_selectors(content),
            'properties': self._extract_css_properties(content),
            'security_issues': []  # CSS typically has fewer security issues
        }
    
    def _extract_js_functions(self, content: str) -> List[Dict[str, Any]]:
        """Extract JavaScript functions."""
        functions = []
        pattern = r'(?:function\s+(\w+)\s*\(|(\w+)\s*:\s*function|const\s+(\w+)\s*=\s*(?:async\s+)?function)'
        matches = re.finditer(pattern, content)
        
        for match in matches:
            func_name = match.group(1) or match.group(2) or match.group(3)
            if func_name:
                functions.append({
                    'name': func_name,
                    'type': 'function',
                    'line_number': content[:match.start()].count('\n') + 1
                })
        
        return functions
    
    def _extract_js_classes(self, content: str) -> List[Dict[str, Any]]:
        """Extract JavaScript classes."""
        classes = []
        pattern = r'class\s+(\w+)(?:\s+extends\s+(\w+))?'
        matches = re.finditer(pattern, content)
        
        for match in matches:
            classes.append({
                'name': match.group(1),
                'base_classes': [match.group(2)] if match.group(2) else [],
                'line_number': content[:match.start()].count('\n') + 1
            })
        
        return classes
    
    def _extract_js_imports(self, content: str) -> List[str]:
        """Extract JavaScript imports."""
        imports = []
        patterns = [
            r'import\s+.*?\s+from\s+[\'"]([^\'"]+)[\'"]',
            r'import\s+[\'"]([^\'"]+)[\'"]',
            r'require\s*\(\s*[\'"]([^\'"]+)[\'"]\s*\)'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, content)
            imports.extend(matches)
        
        return list(set(imports))
    
    def _analyze_js_security(self, content: str) -> List[Dict[str, Any]]:
        """Analyze JavaScript security issues."""
        security_issues = []
        
        dangerous_patterns = {
            r'eval\s*\(': {'severity': 'high', 'issue': 'Use of eval()'},
            r'innerHTML\s*=': {'severity': 'medium', 'issue': 'Potential XSS vulnerability'},
            r'document\.write': {'severity': 'medium', 'issue': 'Potential XSS vulnerability'},
            r'setTimeout\s*\(\s*["\']': {'severity': 'low', 'issue': 'String in setTimeout'}
        }
        
        for pattern, info in dangerous_patterns.items():
            if re.search(pattern, content, re.IGNORECASE):
                security_issues.append({
                    'type': 'security_vulnerability',
                    'severity': info['severity'],
                    'issue': info['issue']
                })
        
        return security_issues
    
    def _extract_java_methods(self, content: str) -> List[Dict[str, Any]]:
        """Extract Java methods."""
        methods = []
        pattern = r'(?:public|private|protected)?\s*(?:static)?\s*(?:\w+\s+)*(\w+)\s*\([^)]*\)\s*(?:throws\s+[\w\s,]+)?\s*\{'
        matches = re.finditer(pattern, content)
        
        for match in matches:
            methods.append({
                'name': match.group(1),
                'type': 'method',
                'line_number': content[:match.start()].count('\n') + 1
            })
        
        return methods
    
    def _extract_java_classes(self, content: str) -> List[Dict[str, Any]]:
        """Extract Java classes."""
        classes = []
        pattern = r'(?:public\s+)?(?:abstract\s+)?(?:final\s+)?class\s+(\w+)(?:\s+extends\s+(\w+))?(?:\s+implements\s+([\w\s,]+))?'
        matches = re.finditer(pattern, content)
        
        for match in matches:
            classes.append({
                'name': match.group(1),
                'base_classes': [match.group(2)] if match.group(2) else [],
                'interfaces': [i.strip() for i in match.group(3).split(',')] if match.group(3) else [],
                'line_number': content[:match.start()].count('\n') + 1
            })
        
        return classes
    
    def _extract_java_imports(self, content: str) -> List[str]:
        """Extract Java imports."""
        pattern = r'import\s+(?:static\s+)?([\w\.\*]+);'
        return re.findall(pattern, content)
    
    def _analyze_java_security(self, content: str) -> List[Dict[str, Any]]:
        """Analyze Java security issues."""
        security_issues = []
        
        dangerous_patterns = {
            r'Runtime\.getRuntime\(\)\.exec': {'severity': 'high', 'issue': 'Command execution'},
            r'Class\.forName\s*\(': {'severity': 'medium', 'issue': 'Reflection usage'},
            r'System\.getProperty': {'severity': 'low', 'issue': 'System property access'}
        }
        
        for pattern, info in dangerous_patterns.items():
            if re.search(pattern, content, re.IGNORECASE):
                security_issues.append({
                    'type': 'security_vulnerability',
                    'severity': info['severity'],
                    'issue': info['issue']
                })
        
        return security_issues
    
    def _extract_html_tags(self, content: str) -> List[str]:
        """Extract HTML tags."""
        pattern = r'<(\w+)(?:\s+[^>]*)?>'
        return list(set(re.findall(pattern, content)))
    
    def _extract_html_forms(self, content: str) -> List[Dict[str, Any]]:
        """Extract HTML forms."""
        forms = []
        pattern = r'<form[^>]*>(.*?)</form>'
        matches = re.finditer(pattern, content, re.DOTALL | re.IGNORECASE)
        
        for match in matches:
            form_content = match.group(1)
            inputs = re.findall(r'<input[^>]*>', form_content, re.IGNORECASE)
            forms.append({
                'input_count': len(inputs),
                'line_number': content[:match.start()].count('\n') + 1
            })
        
        return forms
    
    def _analyze_html_security(self, content: str) -> List[Dict[str, Any]]:
        """Analyze HTML security issues."""
        security_issues = []
        
        dangerous_patterns = {
            r'javascript:': {'severity': 'high', 'issue': 'JavaScript protocol'},
            r'<script[^>]*>': {'severity': 'medium', 'issue': 'Script tag usage'},
            r'onclick\s*=': {'severity': 'low', 'issue': 'Inline event handler'}
        }
        
        for pattern, info in dangerous_patterns.items():
            if re.search(pattern, content, re.IGNORECASE):
                security_issues.append({
                    'type': 'security_vulnerability',
                    'severity': info['severity'],
                    'issue': info['issue']
                })
        
        return security_issues
    
    def _extract_css_selectors(self, content: str) -> List[str]:
        """Extract CSS selectors."""
        pattern = r'([.#]?[\w-]+)\s*\{'
        return list(set(re.findall(pattern, content)))
    
    def _extract_css_properties(self, content: str) -> List[str]:
        """Extract CSS properties."""
        pattern = r'([a-zA-Z-]+)\s*:'
        return list(set(re.findall(pattern, content)))
    
    def _merge_file_analysis(self, results: Dict[str, Any], file_analysis: Dict[str, Any]):
        """Merge individual file analysis into overall results."""
        file_ext = file_analysis['file_type']
        results['file_types'][file_ext] = results['file_types'].get(file_ext, 0) + 1
        
        results['functions'].extend(file_analysis.get('functions', []))
        results['classes'].extend(file_analysis.get('classes', []))
        results['security_issues'].extend(file_analysis.get('security_issues', []))
    
    def _generate_ai_insights(self, results: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Generate AI-powered insights using Gemini API."""
        try:
            import google.generativeai as genai
            genai.configure(api_key=self.gemini_api_key)
            model = genai.GenerativeModel("gemini-2.5-flash")
            
            # Prepare analysis summary for AI
            summary = {
                'total_files': results['files_analyzed'],
                'file_types': results['file_types'],
                'total_functions': len(results['functions']),
                'total_classes': len(results['classes']),
                'security_issues_count': len(results['security_issues'])
            }
            
            prompt = f"""
            Analyze this code repository summary and provide insights:
            
            {json.dumps(summary, indent=2)}
            
            Provide insights on:
            1. Code quality assessment
            2. Security recommendations
            3. Performance suggestions
            4. Documentation improvements
            5. Best practices recommendations
            
            Respond with JSON format.
            """
            
            response = model.generate_content(prompt)
            return {
                'ai_insights': response.text,
                'generated_at': datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"⚠️ AI insights generation failed: {str(e)}")
            return None
    
    def _calculate_summary_metrics(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate overall summary metrics."""
        return {
            'total_files_analyzed': results['files_analyzed'],
            'total_functions_found': len(results['functions']),
            'total_classes_found': len(results['classes']),
            'total_security_issues': len(results['security_issues']),
            'most_common_file_type': max(results['file_types'].items(), key=lambda x: x[1])[0] if results['file_types'] else None,
            'analysis_quality': 'high' if results['files_analyzed'] > 0 else 'low',
            'has_ai_insights': results['ai_insights'] is not None
        }
    
    def generate_analysis_report(self, results: Dict[str, Any]) -> str:
        """Generate comprehensive analysis report."""
        report = []
        report.append("# 🔍 Smart Code Analysis Report")
        report.append(f"Generated: {results['analysis_timestamp']}")
        report.append(f"Repository: {results['repository_path']}")
        report.append("")
        
        # Summary
        summary = results['summary']
        report.append("## 📊 Summary")
        report.append(f"- **Files Analyzed:** {summary['total_files_analyzed']}")
        report.append(f"- **Functions Found:** {summary['total_functions_found']}")
        report.append(f"- **Classes Found:** {summary['total_classes_found']}")
        report.append(f"- **Security Issues:** {summary['total_security_issues']}")
        report.append(f"- **Most Common File Type:** {summary['most_common_file_type']}")
        report.append("")
        
        # File types
        report.append("## 📁 File Types")
        for file_type, count in results['file_types'].items():
            report.append(f"- **{file_type}:** {count} files")
        report.append("")
        
        # Security issues
        if results['security_issues']:
            report.append("## 🚨 Security Issues")
            for issue in results['security_issues'][:5]:  # Show top 5
                report.append(f"- **{issue.get('severity', 'unknown').upper()}:** {issue.get('issue', 'Unknown issue')}")
            report.append("")
        
        # AI Insights
        if results['ai_insights']:
            report.append("## 🤖 AI Insights")
            report.append(results['ai_insights'].get('ai_insights', 'No insights available'))
            report.append("")
        
        return "\n".join(report)

# Example usage and testing
if __name__ == "__main__":
    print("🔍 Smart Code Analyzer - Advanced Analysis Tool")
    print("=" * 60)
    
    # Initialize analyzer
    analyzer = SmartCodeAnalyzer()
    
    # Analyze current directory
    current_dir = "."
    print(f"📁 Analyzing directory: {current_dir}")
    
    # Perform analysis
    results = analyzer.analyze_repository(current_dir)
    
    # Generate report
    report = analyzer.generate_analysis_report(results)
    
    print("\n📊 Analysis Results:")
    print(f"✅ Files analyzed: {results['summary']['total_files_analyzed']}")
    print(f"🔧 Functions found: {results['summary']['total_functions_found']}")
    print(f"🏛️ Classes found: {results['summary']['total_classes_found']}")
    print(f"🚨 Security issues: {results['summary']['total_security_issues']}")
    
    print("\n📄 Full Report:")
    print("-" * 40)
    print(report)
    
    # Save report to file
    with open("code_analysis_report.md", "w", encoding="utf-8") as f:
        f.write(report)
    
    print("\n💾 Report saved to: code_analysis_report.md")
    print("🎉 Analysis complete!")
