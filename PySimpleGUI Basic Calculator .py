import PySimpleGUI as sg

sg.theme("DarkAmber")

layout = [[sg.InputText("", size=(22, 5), key="input")],
          [sg.Button("AC", size=(3, 2)), sg.Button("CE", size=(3, 2)), sg.Button(".", size=(3, 2)), sg.Button("/", size=(3, 2))],
          [sg.Button("7", size=(3, 2)), sg.Button("8", size=(3, 2)), sg.Button("9", size=(3, 2)), sg.Button("*", size=(3, 2))],
          [sg.Button("4", size=(3, 2)), sg.Button("5", size=(3, 2)), sg.Button("6", size=(3, 2)), sg.Button("-", size=(3, 2))],
          [sg.Button("3", size=(3, 2)), sg.Button("2", size=(3, 2)), sg.Button("1", size=(3, 2)), sg.Button("+", size=(3, 2))],
          [sg.Button("00", size=(3, 2)), sg.Button("0", size=(3, 2)), sg.Button("=", size=(8, 2))]
          ]

window = sg.Window("Calculator", layout)

# Event Loop and Button Functions:
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    # Update input field based on button clicks
    elif event in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "00"):
        current_input = values["input"]
        window["input"].update(current_input + event)

    # Clear input field (AC) or clear last digit (CE)
    elif event in ("AC", "CE"):
        if event == "AC":
            window["input"].update("")
        else:  # "CE"
            current_input = values["input"][:-1]
            window["input"].update(current_input)

    # Handle operators (+, -, *, /)
    elif event in ("+", "-", "*", "/"):
        current_input = values["input"]
        # Ensure valid expression before evaluation
        if current_input[-1] not in ("+", "-", "*", "/"):
            window["input"].update(current_input + event)

    # Evaluate expression on "=" button click
    elif event == "=":
        try:
            expression = values["input"]
            result = eval(expression)  # Improved using eval()
            window["input"].update(result)
        except (SyntaxError, ZeroDivisionError) as e:
            window["input"].update("Error: " + str(e))

window.close()
