def fake_bin(x):
    y = ''
    for digit in x:
        if int(digit) < 5:
            y += '0'
        elif int(digit) >= 5:
            y += '1'
    return y
