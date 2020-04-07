# UnoPy

Python 3.7 based GRPC multiplayer implementation of "UNO", the hit Mattel card game.

## Compiling `uno.proto`

If you make changes to `protos/uno.proto`, the compilation command is:

````sh
python -m grpc_tools.protoc -I./protos --python_out=./protos/py --grpc_python_out=./protos/py ./protos/uno.proto
````
