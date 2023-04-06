import data_transfer_service_pb2_grpc as dt_service
import data_transfer_service_pb2 as dt_messages
import grpc

if __name__ == '__main__':
    port = 50051
    channel = grpc.insecure_channel(f'localhost:{port}')
    data_transfer_input = dt_messages.DataTransferInput(BatchSize=100)
    stub = dt_service.DataTransferServiceStub(channel=channel)
    result = stub.Transfer(data_transfer_input)
    print(result)
