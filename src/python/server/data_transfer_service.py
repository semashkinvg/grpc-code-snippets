
import data_transfer_service_pb2_grpc as dt_service
import data_transfer_service_pb2 as dt_messages


class DataTransferService(dt_service.DataTransferService):

    def Transfer(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        # do some data transfer
        process_result = dt_messages.DataTransferResult(ProcessCount=1)
        return process_result
