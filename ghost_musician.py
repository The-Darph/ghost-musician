pkg install python
mkdir -p ~/ghost-midi-test
cd ~/ghost-midi-test
cat > index.html <<'EOF'
<!doctype html>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ghost Musician MIDI Test</title>
<h1>Ghost Musician MIDI Test</h1>
<button id="connect">Find MIDI outputs</button>
<p><label>MIDI output <select id="port"></select></label></p>
<p><label>Channel <input id="channel" type="number" min="1" max="16" value="1"></label></p>
<button id="play" disabled>Play test note</button>
<p id="status" role="status"></p>
<script>
const byId = id => document.getElementById(id);
let midi;

byId('connect').onclick = async () => {
  try {
    midi = await navigator.requestMIDIAccess();
    const outputs = [...midi.outputs.values()];
    byId('port').replaceChildren(...outputs.map(output =>
      new Option(output.name || 'Unnamed MIDI output', output.id)
    ));
    byId('play').disabled = outputs.length === 0;
    byId('status').textContent = outputs.length
      ? 'Choose the OP-1 Field, then play a note.'
      : 'No MIDI outputs detected. Check the cable and reconnect.';
  } catch (error) {
    byId('status').textContent = error.message;
  }
};

byId('play').onclick = async () => {
  const channel = byId('channel').valueAsNumber;
  if (!Number.isInteger(channel) || channel < 1 || channel > 16) {
    byId('status').textContent = 'Enter a MIDI channel from 1 to 16.';
    return;
  }
  try {
    const output = midi.outputs.get(byId('port').value);
    if (!output) throw new Error('MIDI output disconnected. Find outputs again.');
    await output.open();
    const time = performance.now();
    output.send([0x90 + channel - 1, 60, 90], time);
    output.send([0x80 + channel - 1, 60, 0], time + 400);
    byId('status').textContent = `Sent middle C on channel ${channel}.`;
  } catch (error) {
    byId('status').textContent = error.message;
  }
};
</script>
EOF
python -m http.server 8000 --bind 127.0.0.1