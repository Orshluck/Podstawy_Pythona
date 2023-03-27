import math
def number_of_panels(room_length, room_width, panel_length, panel_width, panels_per_package):
    room_area = (room_length * room_width) * 1.1 # zwiększ o 10% nie ma znaczenia w tym aspekcie
    print(f"Room area is {room_area}")
    panel_area = panel_length * panel_width # Ile paneli
    print(f"Panel size is {panel_area}")
    panels_needed = (room_area / panel_area)
    print(f"This requires at least : {panels_needed} panels")
    packages_needed = math.ceil(panels_needed / panels_per_package)
    print(f"Which is {packages_needed} packages")
    return packages_needed


x = number_of_panels(10,10,1,1,10)
print(x)