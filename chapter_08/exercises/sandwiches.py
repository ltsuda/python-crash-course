def make_sandwiches(*items):
    """Summarize the sandwiches we are about to make."""
    print(f"\nMaking a sandwich with the following items:")
    for item in items:
        print(f'- {item}')


make_sandwiches('melted chesse')
make_sandwiches('chicken', 'salad', 'extra chesse')
