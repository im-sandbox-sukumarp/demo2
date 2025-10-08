#!/usr/bin/env python3
"""
Test file for GitHub push protection - contains fake API tokens
This file is intentionally created to test security scanning
"""

import os

# These are FAKE tokens for testing push protection
# DO NOT USE THESE IN REAL APPLICATIONS

# Fake OpenAI API key (clearly fake format)
OPENAI_API_KEY = "sk-test-fake-token-this-is-not-real-123456789abcdef"

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYzAbCdEfGhI"
AWS_REGION = "us-east-1"

# Fake GitHub token (clearly fake)
GITHUB_TOKEN = "ghp_fake-github-token-for-testing-123456789abcdef"

# GitLab token pattern for testing
GITLAB_TOKEN = "glpat-12345678901234567890"

# Fake database connection string
DATABASE_URL = "postgresql://testuser:fakepassword@localhost:5432/testdb"

def main():
    """
    This is just a test function - these tokens are fake
    """
    print("Testing push protection with fake credentials")
    print(f"Using fake OpenAI key: {OPENAI_API_KEY[:10]}...")
    
if __name__ == "__main__":
    main()
