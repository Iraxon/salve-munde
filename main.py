import math

def digit_amputator(number_in, digits_to_get, digits_to_remove):
    """
    Digit Amputator v1.1.0

    Dependencies: Math

    The Digit Amputator removes digits before and
    after set points. It outputs a float made of whatever's left.
    """

    return (
        math.floor(number_in * 10 ** digits_to_get)
        - round(
            (math.floor(number_in * 10 ** digits_to_remove) / (10 ** digits_to_remove))
            * 10 ** digits_to_get
        )
    ) / 10 ** (digits_to_get - digits_to_remove)

def trigonometric_hash(number_in):
    """
    Trigonometric Hash v3.0.1

    Dependencies: Digit Amputator v1.x.x

    Inputs must be integers, preferrably positive.
    Negative inputs work, but they will have predictable
    relations with the hashes of their positive counterparts.

    These relationships will not cause visible artifacts for
    most procedural generation cases. They only
    matter for cryptography, for which negative inputs
    should be avoided altogether.

    This hash uses the sine function, some scaling, and
    Digit Amputator to output floats between zero and one.
    These can be multiplied to scale to any range.
    """

    unclamped_sin = math.sin(1024 + number_in)

    clamped_sin = (unclamped_sin + 1) / 2

    return digit_amputator(clamped_sin, 15, 5)

if __name__ == "__main__":
    print("Hello, there!")
    hash = trigonometric_hash(int(input("Pick an integer, any integer!\n> ")))
    print (f"It's trigonometric hash is {hash}.")
