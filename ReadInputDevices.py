import evdev
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
print("am I alive")
for device in devices:
    print(device.fn, device.name, device.phys)
