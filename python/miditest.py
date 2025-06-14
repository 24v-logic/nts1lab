import rtmidi
from time import sleep

midi_channel = 1

midiout = rtmidi.MidiOut()


for port_index, available_port in enumerate(midiout.get_ports()):
    print(port_index, available_port)
    if available_port == "NTS-1 digital kit:NTS-1 digital kit NTS-1 digital 32:0":
        print("found port", port_index)
        midiout.open_port(port_index)
        break

note_on = [0x91, 60, 110]
note_off = [0x91,60,0]

midiout.send_message(note_on)
sleep(0.5)
midiout.send_message(note_off)
sleep(0.1)

midiout.close_port()
