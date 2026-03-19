def agent_execute(command_name, arguments):
    print(f"\nAgent wants to execute: {command_name} {arguments}")

    cmd_str = str(command_name).lower() + " " + str(arguments).lower()

    # --- Agent Firewall ---
    if "password" in cmd_str or "secret" in cmd_str:
        print("🚨 Agent Firewall: BLOCKED sensitive action")
        return "BLOCKED"

    print("✅ Allowed")
    return "EXECUTED"


# Simulated agent actions

# Normal
agent_execute("execute_shell", {"command_line": "ls"})

# Unsafe
agent_execute("execute_shell", {"command_line": "read password.txt"})
