from vulnerability_types import VulnerabilityResult
import os
import sys
from ai_validator import analyze_vulnerability_with_gpt
from pathlib import Path

API_KEY = os.environ["OPENAPI_TOKEN"]

def validate_file_content(file_path):
    if file_path.suffix != ".rs":
        print("Not a Rust file.")
        return

    with open(file_path, 'r') as file:
        content = file.read()

    return analyze_vulnerability_with_gpt(API_KEY, content, file_path)

if __name__ == "__main__":
    suffix = "src/lib.rs"
    bug_free = "programs/bug-free-contract-1/"
    non_bug_free = "programs/buggy-contract-1/"

    results = []

    file_path_bug_free = Path(bug_free + suffix)
    file_path_buggy = Path(non_bug_free + suffix)
    results.append(validate_file_content(file_path_bug_free))
    results.append(validate_file_content(file_path_buggy))

    print(results)
