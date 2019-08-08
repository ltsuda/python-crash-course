def make_shirt(size='L', message='I Love Python'):
    """ Make a shirt with a message """
    print(f"The shirts' size is {size.title()}, "
          f"and '{message}' is written on it")


make_shirt('M')
make_shirt(size='L')
make_shirt(size='p', message='Just Do It')
