import exercises.printing_functions as printer_3d

unprinted_models = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printer_3d.print_models(unprinted_models, completed_models)
""" print_models(unprinted_models[:], completed_models) if we need to use
the original list, so we send a copy of the list to the function."""
printer_3d.show_completed_models(completed_models)
