# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/sfida_action_log_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/sfida_action_log_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nFpogoprotos/networking/requests/messages/sfida_action_log_message.proto\x12\'pogoprotos.networking.requests.messages\"\x17\n\x15SfidaActionLogMessageb\x06proto3')
)




_SFIDAACTIONLOGMESSAGE = _descriptor.Descriptor(
  name='SfidaActionLogMessage',
  full_name='pogoprotos.networking.requests.messages.SfidaActionLogMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=138,
)

DESCRIPTOR.message_types_by_name['SfidaActionLogMessage'] = _SFIDAACTIONLOGMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SfidaActionLogMessage = _reflection.GeneratedProtocolMessageType('SfidaActionLogMessage', (_message.Message,), dict(
  DESCRIPTOR = _SFIDAACTIONLOGMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.sfida_action_log_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.SfidaActionLogMessage)
  ))
_sym_db.RegisterMessage(SfidaActionLogMessage)


# @@protoc_insertion_point(module_scope)
