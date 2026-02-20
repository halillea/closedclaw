#!/usr/bin/env python3
"""Test recall quality with sample queries."""

import subprocess
import sys

test_queries = [
    "what does Bill want",
    "memory system decisions",
    "CapyBot status",
    "what was built today",
]

print("🧪 Memory Recall Quality Test\n")

for query in test_queries:
    print(f"Query: '{query}'")
    print("-" * 40)
    result = subprocess.run(
        ["python3", "scripts/recall.py", query, "--max", "3"],
        capture_output=True, text=True, cwd="/home/ubuntu/clawd/skills/memory"
    )
    # Just show first 200 chars of output
    output = result.stdout[:300] if result.stdout else "(no results)"
    print(output)
    print()

print("✅ Test complete")
