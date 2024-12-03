
def draw_custom_triangle(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        if i == height:
            print(spaces + '-' * (2 * i ))
        else:
            print(spaces + '/' + ' ' * (2 * i - 2) + '\\' )

draw_custom_triangle(6)