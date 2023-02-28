'''
Given the mapping a = 1, b = 2, ... z = 26,
and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3,
since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable.
For example, '001' is not allowed.
'''


def count_num_ways(msg) -> int:
    num_ways = len(msg)
    length = len(msg)
    for idx, str in enumerate(msg):
        if idx == 0 and str == "0":
            raise ValueError
        if idx > 0 and idx <= length:
            pair = msg[idx-1] + msg[idx]
            print(pair)
            if pair[0] != "0" and int(pair) > 0 and int(pair) <= 26:
                num_ways += 1
        if msg[idx] == "0":
            num_ways -= 1
    return num_ways


print(count_num_ways("3200023"))
