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



    # --- MATH & UPDATING VARIABLES ---

    # You can add to existing numbers
    logic_points = logic_points + 5

    # or use a shortcut called 'increment' (+=)
    logic_points += 5
    # You can even combine strings (Text)
    status_update = "Progressing " + "Fast"
    print(f"Updated Logic Points: {logic_points}")
    print(f"Current Status: {status_update}")

    # --- INTERACTIVE INPUT ---

    # The input() command pasues the program and waits for the user to type something.
    favorite_hobby = input("Enter a hobby you're currently into: ")

    # Now we use that variable in a sentance
    print(f"Adding {favorite_hobby} to Solo's profile...")
    
    # You can even 'concatenate' strings with a plus sign
    print("Roadmap Lesson 1: " + "Complete.")
    
