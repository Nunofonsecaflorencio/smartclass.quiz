# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: core/proto_files/smartclass.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'core/proto_files/smartclass.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!core/proto_files/smartclass.proto\x12\nsmartclass\"&\n\x0fJoinRoomRequest\x12\x13\n\x0bplayer_name\x18\x01 \x01(\t\"V\n\x10JoinRoomResponse\x12\x0e\n\x06joined\x18\x01 \x01(\x08\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x12\n\ngame_timer\x18\x03 \x01(\x05\x12\x0f\n\x07message\x18\x04 \x01(\t\"\x1d\n\x06Player\x12\x13\n\x0bplayer_name\x18\x01 \x01(\t\"9\n\x04Quiz\x12\x10\n\x08question\x18\x01 \x01(\t\x12\x0f\n\x07options\x18\x02 \x03(\t\x12\x0e\n\x06\x61nswer\x18\x03 \x01(\t\"0\n\x06\x41nswer\x12\x13\n\x0bplayer_name\x18\x01 \x01(\t\x12\x11\n\tisCorrect\x18\x02 \x01(\x08\"+\n\nGameStatus\x12\x0e\n\x06isOver\x18\x01 \x01(\x08\x12\r\n\x05score\x18\x02 \x01(\x05\x32\xf8\x01\n\nSmartClass\x12\x45\n\x08JoinRoom\x12\x1b.smartclass.JoinRoomRequest\x1a\x1c.smartclass.JoinRoomResponse\x12/\n\x07GetQuiz\x12\x12.smartclass.Player\x1a\x10.smartclass.Quiz\x12:\n\x0cSubmitAnswer\x12\x12.smartclass.Answer\x1a\x16.smartclass.GameStatus\x12\x36\n\x08\x45xitRoom\x12\x12.smartclass.Player\x1a\x16.smartclass.GameStatusb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'core.proto_files.smartclass_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_JOINROOMREQUEST']._serialized_start=49
  _globals['_JOINROOMREQUEST']._serialized_end=87
  _globals['_JOINROOMRESPONSE']._serialized_start=89
  _globals['_JOINROOMRESPONSE']._serialized_end=175
  _globals['_PLAYER']._serialized_start=177
  _globals['_PLAYER']._serialized_end=206
  _globals['_QUIZ']._serialized_start=208
  _globals['_QUIZ']._serialized_end=265
  _globals['_ANSWER']._serialized_start=267
  _globals['_ANSWER']._serialized_end=315
  _globals['_GAMESTATUS']._serialized_start=317
  _globals['_GAMESTATUS']._serialized_end=360
  _globals['_SMARTCLASS']._serialized_start=363
  _globals['_SMARTCLASS']._serialized_end=611
# @@protoc_insertion_point(module_scope)
