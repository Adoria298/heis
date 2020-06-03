# HEIS

Python 3.7 based GRPC multiplayer implementation of "UNO", the hit Mattel card game.

## Set Up

1. Use pip to install the following modules: `grpc`, `grpc_tools`, `colorama`:

    ```sh
    python -m pip install -U grpc grpc_tools colorama
    ```

2. Clone the repository from github (if you haven't downloaded a release):

    ```sh
    git clone https://www.github.com/Adoria298/heis.git
    ```

3. If you don't want to clone, download and decompress the latest release from the releases page.

## Game Play

1. Ensure `server.py` is active. It can be started by opening a new terminal window in this folder and running `python server.py`. Make sure you change this as to your python command (it must be 3.7+).

2. Run `client.py` with `python client.py` in a different terminal window in the same directory. The same caveats apply as above to the command `python`. Run this as many times as you want games.  Ensure you remember which order the program was run in, as the first to be run is the first to play.

3. To play a card: type "PLAY" and the number of cards from the first card, take 1, that the card you want to play is at to play that card. E.g. to play the 3rd card, type in 2.

4. To draw a card: type "DRAW" and the number of cards you want to draw.

## Modification of the Code

### Compiling `uno.proto`

If you make changes to `protos/uno.proto`, the compilation command is:

```sh
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/uno.proto
```

### `multiplayer-*` Branches

These branches are used to test multiplayer features, and modify the code to work every where. As long as the protocol is not changed, the server can be changed without modifying client code, and vice versa. The `multiplayer-pc` branch is therefore used only to change the server's implementation, and the `multiplayer-rpi` branch for the client's. These should be periodically merged to `multiplayer-all` on Github.
