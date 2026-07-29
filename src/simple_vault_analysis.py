#!/usr/bin/env python3
"""
Simple Vault Analysis Script for Obsidian Markdown Files
"""

import os
import re
from collections import Counter

def find_markdown_files(root_path='.'):
    """Find all markdown files in the vault"""
    markdown_files = []
    
    for root, dirs, files in os.walk(root_path):
        # Skip .obsidian directory
        if '.obsidian' in root:
            continue
            
        for file in files:
            if file.endswith('.md') and not file.startswith('.'):
                full_path = os.path.join(root, file)
                markdown_files.append(full_path)
    
    return markdown_files

def extract_title(content):
    """Extract the title from markdown content (first H1 header)"""
    title_match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
    if title_match:
        return title_match.group(1).strip()
    else:
        # If no H1, use filename without extension
        return os.path.splitext(os.path.basename(file_path))[0]

def detect_language(content):
    """Simple language detection based on common words"""
    # This is a simplified approach - in reality you'd want to use 
    # a proper language detection library like langdetect
    
    # Count Italian words (simplified)
    italian_words = ['il', 'la', 'i', 'gli', 'le', 'un', 'una', 'dei', 'delle', 'del', 'al', 'alla']
    
    # Count English words
    english_words = ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of']
    
    # Simple word counting approach
    content_lower = content.lower()
    italian_count = sum(1 for word in italian_words if f' {word} ' in content_lower)
    english_count = sum(1 for word in english_words if f' {word} ' in content_lower)
    
    if italian_count > english_count:
        return "Italian"
    elif english_count > italian_count:
        return "English" 
    else:
        return "Mixed/Unknown"

def calculate_confidence(content):
    """Calculate confidence score based on content quality"""
    # Simple metrics for confidence
    lines = content.split('\n')
    total_lines = len(lines)
    
    if total_lines == 0:
        return 0.0
    
    # Count non-empty lines
    non_empty_lines = len([line for line in lines if line.strip()])
    
    # Check for basic markdown structure
    has_headers = bool(re.search(r'^#{1,6}\s+', content, re.MULTILINE))
    has_lists = bool(re.search(r'^[\s]*[\-\*\+]\s+', content, re.MULTILINE))
    has_links = bool(re.search(r'\[\[.*?\]\]', content))
    
    # Calculate confidence
    confidence = 0.0
    
    if non_empty_lines > 0:
        # Weighted based on content density
        density = non_empty_lines / total_lines
        confidence += min(density * 0.5, 0.5)
    
    if has_headers:
        confidence += 0.2
    if has_lists:
        confidence += 0.15
    if has_links:
        confidence += 0.15
        
    return round(min(confidence, 1.0), 3)

def analyze_file(file_path):
    """Analyze a single markdown file"""
    try:
        # Read file content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        title = extract_title(content)
        language = detect_language(content)
        confidence = calculate_confidence(content)
        
        return {
            'file_name': os.path.basename(file_path),
            'file_path': file_path,
            'title': title,
            'language': language,
            'confidence': confidence,
            'size': len(content)
        }
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def main():
    """Main analysis function"""
    print("Starting Obsidian Vault Analysis...")
    
    # Get all markdown files
    markdown_files = find_markdown_files()
    print(f"Found {len(markdown_files)} markdown files")
    
    # Analyze each file
    results = []
    
    for i, file_path in enumerate(markdown_files):
        print(f"Analyzing {i+1}/{len(markdown_files)}: {file_path}")
        result = analyze_file(file_path)
        if result:
            results.append(result)
    
    # Generate summary statistics
    languages = [r['language'] for r in results]
    confidences = [r['confidence'] for r in results]
    
    print("\n=== ANALYSIS SUMMARY ===")
    print(f"Total files analyzed: {len(results)}")
    print(f"Average confidence: {sum(confidences)/len(confidences):.3f}")
    print(f"Language distribution:")
    
    lang_count = Counter(languages)
    for lang, count in lang_count.most_common():
        print(f"  {lang}: {count}")
    
    # Show results
    print("\n=== FILE ANALYSIS RESULTS ===")
    print("File Name\t\t\tTitle\t\t\tLanguage\tConfidence")
    print("-" * 80)
    
    for result in results:
        file_name = result['file_name'][:20] + "..." if len(result['file_name']) > 20 else result['file_name']
        title = result['title'][:20] + "..." if len(result['title']) > 20 else result['title']
        print(f"{file_name:<25}\t{title:<25}\t{result['language']:<10}\t{result['confidence']}")
    
    # Show top 5 files by confidence
    print("\n=== TOP 5 FILES BY CONFIDENCE ===")
    sorted_results = sorted(results, key=lambda x: x['confidence'], reverse=True)
    for i, result in enumerate(sorted_results[:5]):
        print(f"{i+1}. {result['file_name']} - Confidence: {result['confidence']}")

if __name__ == "__main__":
    main()