# UnoPy

Python 3.7 based GRPC multiplayer implementation of "UNO", the hit Mattel card game.

## Running

1. Ensure `server.py` is active. It can be started by opening a new terminal window in this folder and running `python server.py`. Make sure you change this as to your python command (it must be 3.7+).

2. Run `client.py` with `python client.py` in a different terminal window in the same directory. The same caveats apply as above to the command `python`. Run this as many times as you want games.  Ensure you remember which order the program was run in, as the first to be run is the first to play.

3. Type in the number of cards from the first card, take 1, that the card you want to play is at to play that card. E.g. to play the 3rd card, type in 2.

## Modification of the Code

### Compiling `uno.proto`

If you make changes to `protos/uno.proto`, the compilation command is:

````sh
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/uno.proto
````
