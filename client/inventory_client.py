import sys
import grpc

sys.path.insert(1, "./../service/")
import bookstore_pb2_grpc
import bookstore_pb2


class Client:
    """Client class encapsulating API"""

    def __init__(self):
        self.port = 50051
        self.ip = "localhost:"
        self.connect()

    def getBook(self, ISBN):
        response = self.stub.GetBook(bookstore_pb2.GetBookRequest(ISBN=ISBN))
        return response

    def connect(self):
        server_address = self.ip + str(self.port)
        channel = grpc.insecure_channel(server_address)
        self.stub = bookstore_pb2_grpc.InventoryServiceStub(channel)
