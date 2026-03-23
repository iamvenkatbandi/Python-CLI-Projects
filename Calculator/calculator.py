import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def calculate(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except:
        return "Error: Invalid expression"


history = []
last_result = None

while True:
    print("\n--- Advanced CLI Calculator ---")
    print("Type expression (e.g., 5 + 3)")
    print("Commands: history, clear, exit")
    
    if last_result is not None:
        print(f"Last Result: {last_result}")

    user_input = input(">>> ")

    # EXIT
    if user_input.lower() == "exit":
        print("Exiting calculator...")
        break

    # HISTORY
    elif user_input.lower() == "history":
        print("\n--- History ---")
        if not history:
            print("No calculations yet.")
        else:
            for item in history:
                print(item)

    # CLEAR SCREEN
    elif user_input.lower() == "clear":
        clear_screen()

    # CALCULATION
    else:
        # Use previous result if user types 'ans'
        if "ans" in user_input:
            if last_result is None:
                print("No previous result available.")
                continue
            user_input = user_input.replace("ans", str(last_result))

        result = calculate(user_input)

        print("Result:", result)

        # Save only valid results
        if not isinstance(result, str):
            history.append(f"{user_input} = {result}")
            last_result = result
