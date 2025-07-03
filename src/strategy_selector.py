from src.strategies import moving_average, rsi

def get_strategy(name):
    if name == "moving_average":
        return moving_average.apply_strategy
    elif name == "rsi":
        return rsi.apply_strategy
    else:
        raise ValueError(f"Strategy '{name}' is not available.")
