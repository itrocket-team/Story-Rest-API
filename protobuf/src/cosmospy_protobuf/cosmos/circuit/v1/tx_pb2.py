"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from ....cosmos.circuit.v1 import types_pb2 as cosmos_dot_circuit_dot_v1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1acosmos/circuit/v1/tx.proto\x12\x11cosmos.circuit.v1\x1a\x17cosmos/msg/v1/msg.proto\x1a\x1dcosmos/circuit/v1/types.proto"\x81\x01\n\x1aMsgAuthorizeCircuitBreaker\x12\x0f\n\x07granter\x18\x01 \x01(\t\x12\x0f\n\x07grantee\x18\x02 \x01(\t\x123\n\x0bpermissions\x18\x03 \x01(\x0b2\x1e.cosmos.circuit.v1.Permissions:\x0c\x82\xe7\xb0*\x07granter"5\n"MsgAuthorizeCircuitBreakerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08"Q\n\x15MsgTripCircuitBreaker\x12\x11\n\tauthority\x18\x01 \x01(\t\x12\x15\n\rmsg_type_urls\x18\x02 \x03(\t:\x0e\x82\xe7\xb0*\tauthority"0\n\x1dMsgTripCircuitBreakerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08"R\n\x16MsgResetCircuitBreaker\x12\x11\n\tauthority\x18\x01 \x01(\t\x12\x15\n\rmsg_type_urls\x18\x03 \x03(\t:\x0e\x82\xe7\xb0*\tauthority"1\n\x1eMsgResetCircuitBreakerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x082\xf4\x02\n\x03Msg\x12\x7f\n\x17AuthorizeCircuitBreaker\x12-.cosmos.circuit.v1.MsgAuthorizeCircuitBreaker\x1a5.cosmos.circuit.v1.MsgAuthorizeCircuitBreakerResponse\x12p\n\x12TripCircuitBreaker\x12(.cosmos.circuit.v1.MsgTripCircuitBreaker\x1a0.cosmos.circuit.v1.MsgTripCircuitBreakerResponse\x12s\n\x13ResetCircuitBreaker\x12).cosmos.circuit.v1.MsgResetCircuitBreaker\x1a1.cosmos.circuit.v1.MsgResetCircuitBreakerResponse\x1a\x05\x80\xe7\xb0*\x01B\x1eZ\x1ccosmossdk.io/x/circuit/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.circuit.v1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1ccosmossdk.io/x/circuit/types'
    _globals['_MSGAUTHORIZECIRCUITBREAKER']._options = None
    _globals['_MSGAUTHORIZECIRCUITBREAKER']._serialized_options = b'\x82\xe7\xb0*\x07granter'
    _globals['_MSGTRIPCIRCUITBREAKER']._options = None
    _globals['_MSGTRIPCIRCUITBREAKER']._serialized_options = b'\x82\xe7\xb0*\tauthority'
    _globals['_MSGRESETCIRCUITBREAKER']._options = None
    _globals['_MSGRESETCIRCUITBREAKER']._serialized_options = b'\x82\xe7\xb0*\tauthority'
    _globals['_MSG']._options = None
    _globals['_MSG']._serialized_options = b'\x80\xe7\xb0*\x01'
    _globals['_MSGAUTHORIZECIRCUITBREAKER']._serialized_start = 106
    _globals['_MSGAUTHORIZECIRCUITBREAKER']._serialized_end = 235
    _globals['_MSGAUTHORIZECIRCUITBREAKERRESPONSE']._serialized_start = 237
    _globals['_MSGAUTHORIZECIRCUITBREAKERRESPONSE']._serialized_end = 290
    _globals['_MSGTRIPCIRCUITBREAKER']._serialized_start = 292
    _globals['_MSGTRIPCIRCUITBREAKER']._serialized_end = 373
    _globals['_MSGTRIPCIRCUITBREAKERRESPONSE']._serialized_start = 375
    _globals['_MSGTRIPCIRCUITBREAKERRESPONSE']._serialized_end = 423
    _globals['_MSGRESETCIRCUITBREAKER']._serialized_start = 425
    _globals['_MSGRESETCIRCUITBREAKER']._serialized_end = 507
    _globals['_MSGRESETCIRCUITBREAKERRESPONSE']._serialized_start = 509
    _globals['_MSGRESETCIRCUITBREAKERRESPONSE']._serialized_end = 558
    _globals['_MSG']._serialized_start = 561
    _globals['_MSG']._serialized_end = 933