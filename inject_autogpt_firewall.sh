#!/bin/bash

FILE="autogpt/app.py"

# Insert firewall check right after function definition
sed -i '/def execute_command(command_name: str, arguments):/a\
    # --- PrivateVault Agent Firewall ---\
    try:\
        cmd_str = str(command_name).lower() + " " + str(arguments).lower()\
        if "secret" in cmd_str or "password" in cmd_str:\
            print("🚨 Agent Firewall: BLOCKED sensitive command")\
            return "BLOCKED BY AGENT FIREWALL"\
    except Exception:\
        pass\
' $FILE

echo "✅ Agent Firewall injected into Auto-GPT"
