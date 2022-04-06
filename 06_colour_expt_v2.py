# Source: https://stackoverflow.com/questions/45782766/color-python-output-given-rrggbb-hex-value

class Color_It():
    
    def __init__(self, red, green, blue, text):
        self.red = red
        self.green = green
        self.blue = blue
        self.text = text

    def get_color_escape(self, red, green, blue):
        return '\033[{};2;{};{};{}m'.format(38, red, green, blue)
    
    def print_colour(self):
        all_coloured = self.get_color_escape(self.red, self.green, self.blue) + self.text + '\033[0;0m'
        return all_coloured
        
# Main Routine goes here...
error_1 = Color_It(255, 100, 100, "Oops, you messed up")
message_2 = Color_It(0, 255, 255, "This is another message")

print(error_1.print_colour())
print(message_2.print_colour())
print("whee")