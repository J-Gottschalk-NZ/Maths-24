# Source: https://stackoverflow.com/questions/45782766/color-python-output-given-rrggbb-hex-value

def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(38, r, g, b)

# Changes colour...
print(get_color_escape(255, 125, 0) + 'Fancy colors!')

print("\033[3;32;40m Bright Green  \n")