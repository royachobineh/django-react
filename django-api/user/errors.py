from django.forms import ValidationError


def flatten_validation_error(error: ValidationError) -> dict:
    """
    Convert  validation error to an error dict.

    The key is the field name. The value is a string with an error. If there's
    more than one error, return the errors as separate sentences, but still
    as a single string.

    """
    ret = {}
    for error_item in error.errors.items():
      field_name = error_item[0]
      ret[field_name] = str(error_item[1])
    return {field_name: "".join(errors) for field_name, errors in ret.items()}