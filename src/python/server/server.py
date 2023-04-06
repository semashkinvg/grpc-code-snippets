from concurrent import futures
import time

import grpc

from data_transfer_service import DataTransferService

import data_transfer_service_pb2_grpc as dt_service
_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def start_server(port: int):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dt_service.add_DataTransferServiceServicer_to_server(
        DataTransferService(), server)
    server.add_insecure_port(f'0.0.0.0:{port}')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    start_server(port=50051)
