# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodeable. For example, '001' is not allowed.

def count_decoders(message: str) -> int:
    return decode(message, len(message))


def decode(message: str, offset: int) -> int:
    if offset == 0:
        return 1

    s = len(message) - offset
    res = decode(message, offset-1)

    if offset >= 2 and int(message[s: s+2]) < 27:
        res += decode(message, offset-2)
    return res


if __name__ == "__main__":
    assert count_decoders('111') == 3
    assert count_decoders('121') == 3
    assert count_decoders('666') == 1
    assert count_decoders('424') == 2
