# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: uno.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='uno.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\tuno.proto\"O\n\x04\x43\x61rd\x12\x1b\n\x06\x63olour\x18\x01 \x01(\x0e\x32\x0b.CardColour\x12\x1b\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\x0b.CardAction\x12\r\n\x05value\x18\x03 \x01(\x11\"P\n\x06Player\x12\x13\n\x04hand\x18\x04 \x03(\x0b\x32\x05.Card\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x14\n\x0cuno_declared\x18\x06 \x01(\x08\x12\r\n\x05score\x18\x07 \x01(\r\"=\n\x07WinInfo\x12\x11\n\tgame_over\x18\x08 \x01(\x08\x12\x1f\n\x0eranked_players\x18\t \x03(\x0b\x32\x07.Player\"\xa1\x01\n\x0bStateOfPlay\x12\x11\n\tround_num\x18\n \x01(\r\x12\x18\n\x07players\x18\x0b \x03(\x0b\x32\x07.Player\x12\x1b\n\x0c\x64iscard_pile\x18\x0c \x03(\x0b\x32\x05.Card\x12\x18\n\tdraw_pile\x18\r \x03(\x0b\x32\x05.Card\x12\x12\n\nround_over\x18\x0e \x01(\x08\x12\x1a\n\x08win_info\x18\x0f \x01(\x0b\x32\x08.WinInfo*L\n\nCardColour\x12\t\n\x05WHITE\x10\x00\x12\x07\n\x03RED\x10\x01\x12\x08\n\x04\x42LUE\x10\x02\x12\t\n\x05GREEN\x10\x03\x12\n\n\x06YELLOW\x10\x04\x12\t\n\x05\x42LACK\x10\x05*^\n\nCardAction\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06NUMBER\x10\x01\x12\x0b\n\x07REVERSE\x10\x02\x12\t\n\x05\x44RAW2\x10\x03\x12\x08\n\x04SKIP\x10\x04\x12\x08\n\x04WILD\x10\x05\x12\x0e\n\nWILD_DRAW4\x10\x06\x32\xba\x01\n\x03Uno\x12-\n\x12RequestStateOfPlay\x12\x07.Player\x1a\x0c.StateOfPlay\"\x00\x12!\n\x08PlayCard\x12\x05.Card\x1a\x0c.StateOfPlay\"\x00\x12\x1c\n\x08\x44rawCard\x12\x07.Player\x1a\x05.Card\"\x00\x12\x1f\n\tAddPlayer\x12\x07.Player\x1a\x07.Player\"\x00\x12\"\n\x0cRemovePlayer\x12\x07.Player\x1a\x07.Player\"\x00\x62\x06proto3'
)

_CARDCOLOUR = _descriptor.EnumDescriptor(
  name='CardColour',
  full_name='CardColour',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WHITE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLUE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREEN', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YELLOW', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLACK', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=403,
  serialized_end=479,
)
_sym_db.RegisterEnumDescriptor(_CARDCOLOUR)

CardColour = enum_type_wrapper.EnumTypeWrapper(_CARDCOLOUR)
_CARDACTION = _descriptor.EnumDescriptor(
  name='CardAction',
  full_name='CardAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUMBER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REVERSE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DRAW2', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SKIP', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WILD', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WILD_DRAW4', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=481,
  serialized_end=575,
)
_sym_db.RegisterEnumDescriptor(_CARDACTION)

CardAction = enum_type_wrapper.EnumTypeWrapper(_CARDACTION)
WHITE = 0
RED = 1
BLUE = 2
GREEN = 3
YELLOW = 4
BLACK = 5
NONE = 0
NUMBER = 1
REVERSE = 2
DRAW2 = 3
SKIP = 4
WILD = 5
WILD_DRAW4 = 6



_CARD = _descriptor.Descriptor(
  name='Card',
  full_name='Card',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='colour', full_name='Card.colour', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='Card.action', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Card.value', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13,
  serialized_end=92,
)


_PLAYER = _descriptor.Descriptor(
  name='Player',
  full_name='Player',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hand', full_name='Player.hand', index=0,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Player.name', index=1,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uno_declared', full_name='Player.uno_declared', index=2,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='Player.score', index=3,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=174,
)


_WININFO = _descriptor.Descriptor(
  name='WinInfo',
  full_name='WinInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_over', full_name='WinInfo.game_over', index=0,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ranked_players', full_name='WinInfo.ranked_players', index=1,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=176,
  serialized_end=237,
)


_STATEOFPLAY = _descriptor.Descriptor(
  name='StateOfPlay',
  full_name='StateOfPlay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='round_num', full_name='StateOfPlay.round_num', index=0,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='players', full_name='StateOfPlay.players', index=1,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='discard_pile', full_name='StateOfPlay.discard_pile', index=2,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='draw_pile', full_name='StateOfPlay.draw_pile', index=3,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='round_over', full_name='StateOfPlay.round_over', index=4,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='win_info', full_name='StateOfPlay.win_info', index=5,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=401,
)

_CARD.fields_by_name['colour'].enum_type = _CARDCOLOUR
_CARD.fields_by_name['action'].enum_type = _CARDACTION
_PLAYER.fields_by_name['hand'].message_type = _CARD
_WININFO.fields_by_name['ranked_players'].message_type = _PLAYER
_STATEOFPLAY.fields_by_name['players'].message_type = _PLAYER
_STATEOFPLAY.fields_by_name['discard_pile'].message_type = _CARD
_STATEOFPLAY.fields_by_name['draw_pile'].message_type = _CARD
_STATEOFPLAY.fields_by_name['win_info'].message_type = _WININFO
DESCRIPTOR.message_types_by_name['Card'] = _CARD
DESCRIPTOR.message_types_by_name['Player'] = _PLAYER
DESCRIPTOR.message_types_by_name['WinInfo'] = _WININFO
DESCRIPTOR.message_types_by_name['StateOfPlay'] = _STATEOFPLAY
DESCRIPTOR.enum_types_by_name['CardColour'] = _CARDCOLOUR
DESCRIPTOR.enum_types_by_name['CardAction'] = _CARDACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Card = _reflection.GeneratedProtocolMessageType('Card', (_message.Message,), {
  'DESCRIPTOR' : _CARD,
  '__module__' : 'uno_pb2'
  # @@protoc_insertion_point(class_scope:Card)
  })
_sym_db.RegisterMessage(Card)

Player = _reflection.GeneratedProtocolMessageType('Player', (_message.Message,), {
  'DESCRIPTOR' : _PLAYER,
  '__module__' : 'uno_pb2'
  # @@protoc_insertion_point(class_scope:Player)
  })
_sym_db.RegisterMessage(Player)

WinInfo = _reflection.GeneratedProtocolMessageType('WinInfo', (_message.Message,), {
  'DESCRIPTOR' : _WININFO,
  '__module__' : 'uno_pb2'
  # @@protoc_insertion_point(class_scope:WinInfo)
  })
_sym_db.RegisterMessage(WinInfo)

StateOfPlay = _reflection.GeneratedProtocolMessageType('StateOfPlay', (_message.Message,), {
  'DESCRIPTOR' : _STATEOFPLAY,
  '__module__' : 'uno_pb2'
  # @@protoc_insertion_point(class_scope:StateOfPlay)
  })
_sym_db.RegisterMessage(StateOfPlay)



_UNO = _descriptor.ServiceDescriptor(
  name='Uno',
  full_name='Uno',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=578,
  serialized_end=764,
  methods=[
  _descriptor.MethodDescriptor(
    name='RequestStateOfPlay',
    full_name='Uno.RequestStateOfPlay',
    index=0,
    containing_service=None,
    input_type=_PLAYER,
    output_type=_STATEOFPLAY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PlayCard',
    full_name='Uno.PlayCard',
    index=1,
    containing_service=None,
    input_type=_CARD,
    output_type=_STATEOFPLAY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DrawCard',
    full_name='Uno.DrawCard',
    index=2,
    containing_service=None,
    input_type=_PLAYER,
    output_type=_CARD,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddPlayer',
    full_name='Uno.AddPlayer',
    index=3,
    containing_service=None,
    input_type=_PLAYER,
    output_type=_PLAYER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemovePlayer',
    full_name='Uno.RemovePlayer',
    index=4,
    containing_service=None,
    input_type=_PLAYER,
    output_type=_PLAYER,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_UNO)

DESCRIPTOR.services_by_name['Uno'] = _UNO

# @@protoc_insertion_point(module_scope)
