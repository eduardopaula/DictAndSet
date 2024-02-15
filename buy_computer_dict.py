avaiable_parts = {"1": "computer",
                  "2": "monitor",
                  "3": "keyboard",
                  "4": "mouse",
                  "5": "hdmi cable",
                  "6": "dvd drive",
                  }

current_choice = None
while current_choice != "0":
    if current_choice in avaiable_parts:
        chosen_part = avaiable_parts[current_choice]
        print("Adding {}".format(chosen_part))
    else:
        for key, values in avaiable_parts.items():
            print(key, values, sep=": ")
        print("0: to finish")

    current_choice = input("> ")
