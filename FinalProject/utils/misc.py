def calculate_average(previous_average, new_value, size):
    if size <= 1:
        return new_value
    else:
        return previous_average + (1 / size) * (new_value - previous_average)