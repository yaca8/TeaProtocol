# src/user_input.py
def get_tea_type():
    tea_types = ["green", "black", "herbal"]  # Supported tea types
    print("Available tea types:", ", ".join(tea_types))
    tea_type = input("Enter your preferred tea type: ").lower()
    if tea_type in tea_types:
        return tea_type
    else:
        return None
