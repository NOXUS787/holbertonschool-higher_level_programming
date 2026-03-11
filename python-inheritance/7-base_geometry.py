def integer_validator(self, name, value):
    """Validate value as a positive integer"""
    if type(value) is not int:
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
