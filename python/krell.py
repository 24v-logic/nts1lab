#
#   This is a modified 'krell patch' designed for the korg NTS-1
#

import rtmidi
from time import sleep
from numpy import random

#   Create MidiOut object
midiout = rtmidi.MidiOut()

#   Find first available NTS-1 port
for port_index, available_port in enumerate(midiout.get_ports()):
    print(port_index, available_port)
    if available_port == "NTS-1 digital kit:NTS-1 digital kit NTS-1 digital 32:0":
        print("found port", port_index)
        midiout.open_port(port_index)
        break
#CC values for eg selection
eg_adsr = 0
eg_ahr = 127/5
eg_ar = 2*127/5
eg_arloop = 3* 127/5
eg_open = 4* 127/55

#   Set evelope function
def set_eg(eg = eg_ar):

    message = [0xB1, 14, eg]
    midiout.send_message(message)

#   Set envelope to attack-release
set_eg()

def set_osc_lfo(freq = 0, depth = 127/2):
    freq_message = [0xB1, 24, freq]
    depth_message = [0xB1, 26, depth]
    midiout.send_message(freq_message)
    midiout.send_message(depth_message)
#   Specify number of notes

n_notes = 64

#   Play random notes
for i in range(n_notes):
    note_value = random.randint(27, 100)
    velocity = random.randint(0,127)
    attack = random.randint(0,127)
    set_osc_lfo(note_value, (velocity + 127)/2)
    midiout.send_message([0xB1, 16, 127 - note_value])
    midiout.send_message([0xB1, 19, 127 - note_value])
    midiout.send_message([0x91, note_value, velocity])
    sleep((127- note_value)/127)
    midiout.send_message([0x81, note_value, 0])
