# src/protocol_handler.py
def fetch_protocol(tea_type):
    protocol_file = f"protocols/{tea_type}_tea.md"
    try:
        with open(protocol_file, "r") as file:
            return file.read()
    except FileNotFoundError:
        return None

def execute_protocol(protocol):
    print("Brewing instructions:")
    print(protocol)  # Simply print out the protocol for demonstration purposes
