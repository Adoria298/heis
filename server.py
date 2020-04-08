"""
Uses code based on protocol buffers file `uno.proto` to create a GRPC server.
"""
import uno_pb2 as uno_pb2
import uno_pb2_grpc as uno_pb2_grpc

from deck import Deck

# manually check files compiled correctly
#print(help(uno_pb2))
#print(help(uno_pb2_grpc))

if __name__ == "__main__":
    from pprint import pprint
    pprint(Deck().cards)