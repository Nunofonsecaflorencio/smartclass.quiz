# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from proto_files import smartclass_pb2 as proto__files_dot_smartclass__pb2

GRPC_GENERATED_VERSION = '1.66.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in proto_files/smartclass_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class SmartClassStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.JoinRoom = channel.unary_unary(
                '/smartclass.SmartClass/JoinRoom',
                request_serializer=proto__files_dot_smartclass__pb2.JoinRoomRequest.SerializeToString,
                response_deserializer=proto__files_dot_smartclass__pb2.JoinRoomResponse.FromString,
                _registered_method=True)
        self.GetNextQuestion = channel.unary_unary(
                '/smartclass.SmartClass/GetNextQuestion',
                request_serializer=proto__files_dot_smartclass__pb2.Player.SerializeToString,
                response_deserializer=proto__files_dot_smartclass__pb2.Question.FromString,
                _registered_method=True)
        self.SubmitAnswer = channel.unary_unary(
                '/smartclass.SmartClass/SubmitAnswer',
                request_serializer=proto__files_dot_smartclass__pb2.Answer.SerializeToString,
                response_deserializer=proto__files_dot_smartclass__pb2.GameStatus.FromString,
                _registered_method=True)
        self.ExitRoom = channel.unary_unary(
                '/smartclass.SmartClass/ExitRoom',
                request_serializer=proto__files_dot_smartclass__pb2.Player.SerializeToString,
                response_deserializer=proto__files_dot_smartclass__pb2.GameStatus.FromString,
                _registered_method=True)


class SmartClassServicer(object):
    """Missing associated documentation comment in .proto file."""

    def JoinRoom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNextQuestion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitAnswer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExitRoom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SmartClassServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'JoinRoom': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinRoom,
                    request_deserializer=proto__files_dot_smartclass__pb2.JoinRoomRequest.FromString,
                    response_serializer=proto__files_dot_smartclass__pb2.JoinRoomResponse.SerializeToString,
            ),
            'GetNextQuestion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNextQuestion,
                    request_deserializer=proto__files_dot_smartclass__pb2.Player.FromString,
                    response_serializer=proto__files_dot_smartclass__pb2.Question.SerializeToString,
            ),
            'SubmitAnswer': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitAnswer,
                    request_deserializer=proto__files_dot_smartclass__pb2.Answer.FromString,
                    response_serializer=proto__files_dot_smartclass__pb2.GameStatus.SerializeToString,
            ),
            'ExitRoom': grpc.unary_unary_rpc_method_handler(
                    servicer.ExitRoom,
                    request_deserializer=proto__files_dot_smartclass__pb2.Player.FromString,
                    response_serializer=proto__files_dot_smartclass__pb2.GameStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'smartclass.SmartClass', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('smartclass.SmartClass', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SmartClass(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def JoinRoom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/smartclass.SmartClass/JoinRoom',
            proto__files_dot_smartclass__pb2.JoinRoomRequest.SerializeToString,
            proto__files_dot_smartclass__pb2.JoinRoomResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetNextQuestion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/smartclass.SmartClass/GetNextQuestion',
            proto__files_dot_smartclass__pb2.Player.SerializeToString,
            proto__files_dot_smartclass__pb2.Question.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SubmitAnswer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/smartclass.SmartClass/SubmitAnswer',
            proto__files_dot_smartclass__pb2.Answer.SerializeToString,
            proto__files_dot_smartclass__pb2.GameStatus.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ExitRoom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/smartclass.SmartClass/ExitRoom',
            proto__files_dot_smartclass__pb2.Player.SerializeToString,
            proto__files_dot_smartclass__pb2.GameStatus.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
