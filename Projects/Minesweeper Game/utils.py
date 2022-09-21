import settings


def height_percentage(percentage):
    return (settings.HEIGHT / 100) * percentage


def width_percentage(percentage):
    return (settings.WIDTH / 100) * percentage


# print(height_percentage(25))
# print(width_percentage(25))
