"""
Uses code based on protocol buffers file `uno.proto` to create a GRPC server.
"""
import protos.py.uno_pb2 as uno_pb2
import protos.py.uno_pb2_grpc as uno_pb2_grpc

# manually check files compiled correctly
print(help(uno_pb2))
print(help(uno_pb2_grpc))