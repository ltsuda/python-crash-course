def build_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_info['manufacturer'] = manufacturer.title()
    car_info['model'] = model.title()

    return car_info


car = build_car(
    'VW', 'Up', color='black', tow_package=True)
print(car)
