# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto_files/smartclass.proto
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
    'proto_files/smartclass.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cproto_files/smartclass.proto\x12\nsmartclass\"4\n\x0fJoinRoomRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x13\n\x0bplayer_name\x18\x02 \x01(\t\"?\n\x10JoinRoomResponse\x12\x0e\n\x06joined\x18\x01 \x01(\x08\x12\x0c\n\x04time\x18\x03 \x01(\x05\x12\r\n\x05start\x18\x02 \x01(\x08\"*\n\x13NextQuestionRequest\x12\x13\n\x0bplayer_name\x18\x01 \x01(\t\"=\n\x08Question\x12\x10\n\x08question\x18\x01 \x01(\t\x12\x0f\n\x07options\x18\x02 \x03(\t\x12\x0e\n\x06\x61nswer\x18\x03 \x01(\t\"0\n\x06\x41nswer\x12\x13\n\x0bplayer_name\x18\x01 \x01(\t\x12\x11\n\tisCorrect\x18\x02 \x01(\x08\"*\n\nGameStatus\x12\r\n\x05isEnd\x18\x01 \x01(\x08\x12\r\n\x05score\x18\x02 \x01(\x05\x32\xdb\x01\n\nSmartClass\x12G\n\x08JoinRoom\x12\x1b.smartclass.JoinRoomRequest\x1a\x1c.smartclass.JoinRoomResponse0\x01\x12H\n\x0fgetNextQuestion\x12\x1f.smartclass.NextQuestionRequest\x1a\x14.smartclass.Question\x12:\n\x0csubmitAnswer\x12\x12.smartclass.Answer\x1a\x16.smartclass.GameStatusb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto_files.smartclass_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_JOINROOMREQUEST']._serialized_start=44
  _globals['_JOINROOMREQUEST']._serialized_end=96
  _globals['_JOINROOMRESPONSE']._serialized_start=98
  _globals['_JOINROOMRESPONSE']._serialized_end=161
  _globals['_NEXTQUESTIONREQUEST']._serialized_start=163
  _globals['_NEXTQUESTIONREQUEST']._serialized_end=205
  _globals['_QUESTION']._serialized_start=207
  _globals['_QUESTION']._serialized_end=268
  _globals['_ANSWER']._serialized_start=270
  _globals['_ANSWER']._serialized_end=318
  _globals['_GAMESTATUS']._serialized_start=320
  _globals['_GAMESTATUS']._serialized_end=362
  _globals['_SMARTCLASS']._serialized_start=365
  _globals['_SMARTCLASS']._serialized_end=584
# @@protoc_insertion_point(module_scope)
