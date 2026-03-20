# --- Python Environment: Operational ---
print("Git Environment: Verified")
print("Python Version: 3.10+")
print("Status: Ready for roadmap.sh development")

# A quick list of what I've configured
tools = ["Cursor", "Git Bash", "GitHub Sync"]
for tool in tools:
    print(f"Configured: {tool}")






    # ================================
    # LESSON 1: VARIABLES & DATA TYPES
    # ================================

    # String (Text)
    coder_name = "Solo"

    # Integer (Whole Numbers)
    logic_points = 10

    # Float (Decimal)
    accuracy_percent = 98.5

    # Boolean (True/False)
    is_environment_ready = True

    # --- THE CHALLENGE ---
    # We use an 'f' before the quotes to "format" the string.
    #It lets us drop variables into the string using { }
    print(f"{coder_name} has {logic_points} points and an accuracy of {accuracy_percent}%")
    print(f"Is the environment ready? {is_environment_ready}")
    