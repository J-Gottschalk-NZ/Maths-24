# Source: https://stackoverflow.com/questions/45782766/color-python-output-given-rrggbb-hex-value

def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(38, r, g, b)

# Changes colour...
def print_colour(r, g, b, text):
    print(get_color_escape(r, g, b) + text + '\033[0;0m')

print_colour(255, 255, 0, "Hello World")
print("oops")