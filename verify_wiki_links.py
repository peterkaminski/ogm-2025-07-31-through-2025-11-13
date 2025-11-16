#!/usr/bin/env python3
"""
Verify all internal wiki links in markdown files.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# Base directory
BASE_DIR = Path("/home/user/ogm-2025-07-31-through-2025-11-13/wiki")

# Regular expression to match markdown links: [text](url)
LINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

# Pattern to match headers for anchor verification
HEADER_PATTERN = re.compile(r'^#{1,6}\s+(.+)$', re.MULTILINE)

def get_anchor_from_header(header_text):
    """Convert header text to anchor format (lowercase, hyphens, no special chars)"""
    # Remove markdown formatting
    text = re.sub(r'[*_`]', '', header_text)
    # Convert to lowercase
    text = text.lower()
    # Replace spaces with hyphens
    text = re.sub(r'\s+', '-', text)
    # Remove special characters except hyphens
    text = re.sub(r'[^a-z0-9\-]', '', text)
    # Remove duplicate hyphens
    text = re.sub(r'-+', '-', text)
    # Remove leading/trailing hyphens
    text = text.strip('-')
    return text

def extract_anchors_from_file(file_path):
    """Extract all valid anchor targets from a markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        headers = HEADER_PATTERN.findall(content)
        anchors = set()
        for header in headers:
            anchor = get_anchor_from_header(header)
            if anchor:
                anchors.add(anchor)
        return anchors
    except Exception as e:
        return set()

def is_internal_link(url):
    """Check if URL is an internal wiki link (not external http/https)"""
    url = url.strip()
    # Exclude external links
    if url.startswith('http://') or url.startswith('https://'):
        return False
    # Exclude mailto links
    if url.startswith('mailto:'):
        return False
    # Exclude anchor-only links (same page)
    if url.startswith('#'):
        return False
    return True

def resolve_link_path(source_file, link_url):
    """Resolve relative link path to absolute path"""
    # Remove anchor if present
    if '#' in link_url:
        file_part, anchor_part = link_url.split('#', 1)
    else:
        file_part = link_url
        anchor_part = None

    # Get directory of source file
    source_dir = Path(source_file).parent

    # Resolve the path
    target_path = (source_dir / file_part).resolve()

    return target_path, anchor_part

def find_all_markdown_files(base_dir):
    """Find all markdown files in directory and subdirectories"""
    md_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):
                md_files.append(Path(root) / file)
    return sorted(md_files)

def verify_links():
    """Main function to verify all links"""
    all_files = find_all_markdown_files(BASE_DIR)

    print(f"Found {len(all_files)} markdown files to check\n")
    print("=" * 80)

    total_links = 0
    broken_links = []

    for md_file in all_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"ERROR reading {md_file}: {e}")
            continue

        # Find all links
        matches = LINK_PATTERN.findall(content)

        for link_text, link_url in matches:
            # Skip external links
            if not is_internal_link(link_url):
                continue

            total_links += 1

            # Resolve the link
            target_path, anchor = resolve_link_path(md_file, link_url)

            # Check if file exists
            if not target_path.exists():
                broken_links.append({
                    'source': str(md_file.relative_to(BASE_DIR)),
                    'link_text': link_text,
                    'link_url': link_url,
                    'issue': 'FILE_NOT_FOUND',
                    'target': str(target_path)
                })
                continue

            # If there's an anchor, verify it exists
            if anchor:
                anchors = extract_anchors_from_file(target_path)
                if anchor not in anchors:
                    broken_links.append({
                        'source': str(md_file.relative_to(BASE_DIR)),
                        'link_text': link_text,
                        'link_url': link_url,
                        'issue': 'ANCHOR_NOT_FOUND',
                        'target': str(target_path.relative_to(BASE_DIR)),
                        'anchor': anchor,
                        'available_anchors': sorted(list(anchors))[:5]  # Show first 5 available
                    })

    # Print results
    print("\n" + "=" * 80)
    print("VERIFICATION RESULTS")
    print("=" * 80)
    print(f"\nTotal internal links checked: {total_links}")
    print(f"Broken links found: {len(broken_links)}")

    if broken_links:
        print("\n" + "=" * 80)
        print("BROKEN LINKS DETAILS")
        print("=" * 80)

        # Group by issue type
        by_type = defaultdict(list)
        for link in broken_links:
            by_type[link['issue']].append(link)

        for issue_type, links in sorted(by_type.items()):
            print(f"\n{issue_type} ({len(links)} issues):")
            print("-" * 80)
            for link in links:
                print(f"\n  Source: {link['source']}")
                print(f"  Link: [{link['link_text']}]({link['link_url']})")
                if issue_type == 'FILE_NOT_FOUND':
                    print(f"  Target: {link['target']}")
                    print(f"  Issue: File does not exist")
                elif issue_type == 'ANCHOR_NOT_FOUND':
                    print(f"  Target: {link['target']}")
                    print(f"  Anchor: #{link['anchor']}")
                    if link['available_anchors']:
                        print(f"  Available anchors (first 5): {', '.join(['#' + a for a in link['available_anchors']])}")
    else:
        print("\n✓ All links verified successfully!")

    return len(broken_links) == 0

if __name__ == '__main__':
    success = verify_links()
    exit(0 if success else 1)
