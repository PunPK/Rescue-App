from plyer import gps


def print_location(**kwargs):
    print("GPS Data:", kwargs)


gps.configure(on_location=print_location)
gps.start()
