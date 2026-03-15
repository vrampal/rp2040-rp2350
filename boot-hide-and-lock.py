import usb_cdc
import usb_midi
import storage
import supervisor

# This must be run in boot.py and not code.py

# These lines will change vendor id, device id, hide storage and REPL
# WARNING: it will become IMPOSSIBLE to access or modify code.py or boot.py after reboot

# Mimic a Logitech Unifying Receiver
# see: https://devicehunt.com/view/type/usb/vendor/046D
supervisor.set_usb_identification(
    # Use an obsolete vid to not confuse Logitech drivers
    # normal Logitech vid is 0x046D
    vid=0x04E0,
    pid=0xC52B,
    manufacturer="Logitech, Inc.",
    product="Unifying Receiver"
)

# Disable storage
storage.disable_usb_drive()
# Disable REPL
usb_cdc.disable()
# Disable MIDI
usb_midi.disable()