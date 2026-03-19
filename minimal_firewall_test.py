def execute_command(command_name, arguments):
    cmd_str = str(command_name).lower() + " " + str(arguments).lower()

    # Agent Firewall
    if "password" in cmd_str:
        print("🚨 Agent Firewall: BLOCKED")
        return "BLOCKED"

    return "ALLOWED"

print("\n--- Normal ---")
print(execute_command("execute_shell", {"command_line": "ls"}))

print("\n--- Sensitive ---")
print(execute_command("execute_shell", {"command_line": "read password.txt"}))
