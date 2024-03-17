# src/main.py
from src import user_input, protocol_handler

def main():
    print("Welcome to TeaProtocol!")
    print("Please select your preferred type of tea:")
    tea_type = user_input.get_tea_type()
    if tea_type:
        protocol = protocol_handler.fetch_protocol(tea_type)
        if protocol:
            protocol_handler.execute_protocol(protocol)
        else:
            print("Sorry, the selected tea type is not supported.")
    else:
        print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
