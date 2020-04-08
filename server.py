"""
Uses code based on protocol buffers file `uno.proto` to create a GRPC server.
"""
# proto3 generated code
import uno_pb2
import uno_pb2_grpc
# homemade code
from deck import Deck


if __name__ == "__main__":
    from pprint import pprint
    pprint(Deck().cards)