def detect_mistakes(equation):

    mistakes = []

    if "+-" in equation or "-+" in equation:
        mistakes.append("Possible sign error")

    if "*(" in equation:
        mistakes.append("Check multiplication distribution")

    if "/" in equation:
        mistakes.append("Be careful when dividing both sides")

    if not mistakes:
        mistakes.append("No common algebra mistakes detected")

    return mistakes