## Twelvetone Editor

Randomly generates a *tone row* (12-tone, *serialism*) and performs some basic transformations.

Type `./make.sh` to compile, then `./twelvetone.sh` to run the program.

### How it Works
When you enter a command at the `twelvetone>` prompt, the row is edited.
If you want to reverse your changes, you must use the inverse command, e.g.,
*flip* again will undo *flip*, 3 *rotate* commands to undo a *rotate* command.

### Component Tools

- `twelvetone.sh`
- `play-new-row.sh`
- `tonerow`
- `listfreqs.jar`
- `choose_player.py`
- `draw_row.py`
- `write_ogg.py`
- `flip.pl`
- `mirror.pl`
- `rotate.pl`

### Known Bugs
- Pitch-shift feature is non-functional