# A function can have documentation inside it.
def check_disk(usage):
    """
    Check Linux disk usage.

    Returns CRITICAL if usage is 90% or above.
    """

    if usage >= 90:
        return "CRITICAL"

    return "OK"
# print(check_disk.__doc__)