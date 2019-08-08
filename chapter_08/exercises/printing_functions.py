def print_models(unprinted, completed):
    """
    Simulate printing each design, until none are left.
    Move each design to completed list after printing.
    """
    while unprinted:
        current = unprinted.pop()
        print(f"Printing model: {current.title()}")
        completed.append(current)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print(f"\nThe following models have been printed.")
    for model in completed_models:
        print(model.title())
