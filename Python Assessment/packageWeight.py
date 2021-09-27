def solve(width, height, length, mass):

    volume = width * height * length

    if volume >= 1000000 and mass >= 50:
        return "rejected"
    elif volume >= 1000000 or mass >= 50:
        return "special"
    else:
        return "standard"
