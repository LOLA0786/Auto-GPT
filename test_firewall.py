from autogpt.app import execute_command

# ✅ Normal command
print("\n--- Normal Command ---")
result1 = execute_command("execute_shell", {"command_line": "ls"})
print("Result:", result1)

# 🚨 Sensitive command
print("\n--- Sensitive Command ---")
result2 = execute_command("execute_shell", {"command_line": "read password.txt"})
print("Result:", result2)
