# Ghost Musician

> Ghost Musician is a generative MIDI player for the OP‑1 Field. It runs on a Galaxy Tab A7 Lite in Termux and has a local touch interface for play, stop, tempo,  note density, and variation. The goal is to generate recognizable phrases with enough variation to discover parts worth recording and looping through the TX‑6.

> The reason for using such an old, underpowered Android device is because I like to find uses for old tech and this old thing can be very musical and useful even if it is slow and barely usable by today's standards.

*Currently only works on Android, tested on Galaxy A7 Lite. iOS support to come in the future*

## Android Setup

*Verified on hardware: Termux served a page on 127.0.0.1:8000, and Chrome sent an audible test note to the OP‑1 Field over USB‑C after the Galaxy’s USB setting was switched from File Transfer to MIDI. Chrome handled MIDI in that test. Python’s role in playback is still open.

Next step: Build a repeating phrase with live touch controls, then test it on the Galaxy. Pull updates from GitHub in Termux with git pull --ff-only.

__Instructions assume use of Termux on Android__

1. In Termux, navigate to home directory (or one of your choosing) `cd ~`
2. Clone the repository (you may need to install git first via `pkg install git`): `git clone https://github.com/The-Darph/ghost-musician.git`
3. `cd ghost-musician` to enter directory
4. Run `bash ghost_musician.py`. Be sure to accept or install all packages at this point. Once complete, a server will be running locally.
5. Plug a USB C cable between your OP-1 Field and tablet. The original OP-1 is not guaranteed to work and may require a USB-C to USB A 2.0 adapter.
5. In Chrome, navigate to `http://127.0.0.1:8000`. Click the button to detect MIDI. Allow MIDI connections in Chrome, choose the USB peripheral from the list, then press the button to generate a middle C on the OP-1. OP-1 must be on a synth or drum.

If you encounter issues connecting or sending MIDI data, check your tablet's USB settings. You may need to set your tablet to send/receive MIDI data as the default is file transfers.

## iOS Setup

> iOS development is planned for a future update.

## Additional Features

In the future the following features will be added:

- BPM adjustment
- Key choice
- Velocity sliders
- Synth parameter randomization and controls via browser

The goal of this project is to allow you to set the OP-1 to play semi-randomly and adjust the randomness of some parameters live as it plays.