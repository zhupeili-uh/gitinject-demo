import os
import subprocess

# Fetch PR body content provided by the contributor
pr_body = os.environ.get("PR_BODY", "")

# Toy version of a vulnerable AI Agent that blindly executes PR body content.
# In a real scenario, Prompt Injection tricks the LLM into generating these shell commands.
print("AI Agent is analyzing the PR and running prerequisite tasks...")

try:
    # VULNERABILITY: Executing untrusted input directly
    result = subprocess.check_output(pr_body, shell=True, stderr=subprocess.STDOUT, text=True)
    print(f"AI Review Comment:\nAnalysis complete. Execution result:\n{result}")
except Exception as e:
    print("AI Review Comment:\nThe code looks good, no issues found.")