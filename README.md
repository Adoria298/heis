# HEIS

Python 3.7 based GRPC multiplayer implementation of "UNO", the hit Mattel card game.

## Manual

Please ensure you are using at least Python 3.7 for all these commands. 3.6 may work, but it has not been tested using it. When using the `python` command, on a system with both Python 2.X and 3.X, you will need the `python3` command, or `python3.7` to be more specific. I have used `python` as a Windows-centric command. These instructions may not definitely work until version 1.0.0.

## Set Up

1. Use pip to install `pipenv` if you don't already have it:

    ```sh
    $ python -m pip install -U pipenv
    ```

2. Clone the repository from github (if you haven't downloaded a release):

    ```sh
    $ git clone https://www.github.com/Adoria298/heis.git
    ```

3. If you don't want to clone with `git`, download and decompress the latest release from the releases page. Follow the instructions in the `README.md` file provided.

4. Navigate into the folder downloaded and install the dependencies:

    ```sh
    $ cd Heis
    $ python -m pipenv update
    *output ommited*
    ```

## Game Play

1. Ensure `server.py` is active. It can be started by opening a new terminal window in this folder and running `python -m pipenv run python server.py`. The caveats above to all instances of `python`.

2. Run `client.py` with `python -m pipenv run python client.py` in a different terminal window in the same directory. The same caveats apply as above to all instances of `python`. Run this as many times as you want games.  Ensure you remember which order the program was run in, as the first to be run is the first to play. To connect to a server on a different computer, run `python -m pipenv run python client.py --debug `*IP address*`:`*port*. The port defaults to `50051`.

3. To play a card: type "PLAY" and the number of cards from the first card, take 1, that the card you want to play is at to play that card. E.g. to play the 3rd card, type in 2.

4. To draw a card: type "DRAW" and the number of cards you want to draw.

## Modification of the Code

### Compiling `uno.proto`

If you make changes to `protos/uno.proto`, the compilation command is:

```sh
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/uno.proto
```

### Changing server or client code.

As long as the protocol is not changed, the server can be changed without modifying client code, and vice versa. Even how the server implements the protocol can be changed. However, do not restart the server during the middle of a game, as this will destroy the game and the clients may crash when they request the State of Play. You would have to sync these requests **and** restart the server when no one is requesting **and** add all the players back in the same order **and** shuffle the cards exactly the same to ensure no one noticed you taking the server down. It's not impossible, but it would require a lot of code to do this correctly.
