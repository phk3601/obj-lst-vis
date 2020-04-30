# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from object_list/ObjectsList.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import object_list.msg
import std_msgs.msg

class ObjectsList(genpy.Message):
  _md5sum = "ad78ad5b64d1034693ee039c59e27240"
  _type = "object_list/ObjectsList"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
ObjectList[] obj_list

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: object_list/ObjectList
int32 obj_id
Geometric geometric
float64[36] covariance
Dimension dimension
float32 prop_existence
float32 prop_mov 
Classification classification
Features features

================================================================================
MSG: object_list/Geometric
float64 x
float64 y
float64 vx
float64 vy
float64 ax
float64 ay
float64 yaw
float64 yawrate

================================================================================
MSG: object_list/Dimension
float64 length
float64 width
float64 height

================================================================================
MSG: object_list/Classification
float32 car
float32 truck
float32 motorcycle
float32 bicycle
float32 pedestrian
float32 stacionary
float32 other

================================================================================
MSG: object_list/Features
bool FL
bool FM
bool FR
bool MR
bool RR
bool RM
bool RL
bool ML
"""
  __slots__ = ['header','obj_list']
  _slot_types = ['std_msgs/Header','object_list/ObjectList[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,obj_list

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ObjectsList, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.obj_list is None:
        self.obj_list = []
    else:
      self.header = std_msgs.msg.Header()
      self.obj_list = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.obj_list)
      buff.write(_struct_I.pack(length))
      for val1 in self.obj_list:
        buff.write(_get_struct_i().pack(val1.obj_id))
        _v1 = val1.geometric
        _x = _v1
        buff.write(_get_struct_8d().pack(_x.x, _x.y, _x.vx, _x.vy, _x.ax, _x.ay, _x.yaw, _x.yawrate))
        buff.write(_get_struct_36d().pack(*val1.covariance))
        _v2 = val1.dimension
        _x = _v2
        buff.write(_get_struct_3d().pack(_x.length, _x.width, _x.height))
        _x = val1
        buff.write(_get_struct_2f().pack(_x.prop_existence, _x.prop_mov))
        _v3 = val1.classification
        _x = _v3
        buff.write(_get_struct_7f().pack(_x.car, _x.truck, _x.motorcycle, _x.bicycle, _x.pedestrian, _x.stacionary, _x.other))
        _v4 = val1.features
        _x = _v4
        buff.write(_get_struct_8B().pack(_x.FL, _x.FM, _x.FR, _x.MR, _x.RR, _x.RM, _x.RL, _x.ML))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.obj_list is None:
        self.obj_list = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.obj_list = []
      for i in range(0, length):
        val1 = object_list.msg.ObjectList()
        start = end
        end += 4
        (val1.obj_id,) = _get_struct_i().unpack(str[start:end])
        _v5 = val1.geometric
        _x = _v5
        start = end
        end += 64
        (_x.x, _x.y, _x.vx, _x.vy, _x.ax, _x.ay, _x.yaw, _x.yawrate,) = _get_struct_8d().unpack(str[start:end])
        start = end
        end += 288
        val1.covariance = _get_struct_36d().unpack(str[start:end])
        _v6 = val1.dimension
        _x = _v6
        start = end
        end += 24
        (_x.length, _x.width, _x.height,) = _get_struct_3d().unpack(str[start:end])
        _x = val1
        start = end
        end += 8
        (_x.prop_existence, _x.prop_mov,) = _get_struct_2f().unpack(str[start:end])
        _v7 = val1.classification
        _x = _v7
        start = end
        end += 28
        (_x.car, _x.truck, _x.motorcycle, _x.bicycle, _x.pedestrian, _x.stacionary, _x.other,) = _get_struct_7f().unpack(str[start:end])
        _v8 = val1.features
        _x = _v8
        start = end
        end += 8
        (_x.FL, _x.FM, _x.FR, _x.MR, _x.RR, _x.RM, _x.RL, _x.ML,) = _get_struct_8B().unpack(str[start:end])
        _v8.FL = bool(_v8.FL)
        _v8.FM = bool(_v8.FM)
        _v8.FR = bool(_v8.FR)
        _v8.MR = bool(_v8.MR)
        _v8.RR = bool(_v8.RR)
        _v8.RM = bool(_v8.RM)
        _v8.RL = bool(_v8.RL)
        _v8.ML = bool(_v8.ML)
        self.obj_list.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.obj_list)
      buff.write(_struct_I.pack(length))
      for val1 in self.obj_list:
        buff.write(_get_struct_i().pack(val1.obj_id))
        _v9 = val1.geometric
        _x = _v9
        buff.write(_get_struct_8d().pack(_x.x, _x.y, _x.vx, _x.vy, _x.ax, _x.ay, _x.yaw, _x.yawrate))
        buff.write(val1.covariance.tostring())
        _v10 = val1.dimension
        _x = _v10
        buff.write(_get_struct_3d().pack(_x.length, _x.width, _x.height))
        _x = val1
        buff.write(_get_struct_2f().pack(_x.prop_existence, _x.prop_mov))
        _v11 = val1.classification
        _x = _v11
        buff.write(_get_struct_7f().pack(_x.car, _x.truck, _x.motorcycle, _x.bicycle, _x.pedestrian, _x.stacionary, _x.other))
        _v12 = val1.features
        _x = _v12
        buff.write(_get_struct_8B().pack(_x.FL, _x.FM, _x.FR, _x.MR, _x.RR, _x.RM, _x.RL, _x.ML))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.obj_list is None:
        self.obj_list = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.obj_list = []
      for i in range(0, length):
        val1 = object_list.msg.ObjectList()
        start = end
        end += 4
        (val1.obj_id,) = _get_struct_i().unpack(str[start:end])
        _v13 = val1.geometric
        _x = _v13
        start = end
        end += 64
        (_x.x, _x.y, _x.vx, _x.vy, _x.ax, _x.ay, _x.yaw, _x.yawrate,) = _get_struct_8d().unpack(str[start:end])
        start = end
        end += 288
        val1.covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=36)
        _v14 = val1.dimension
        _x = _v14
        start = end
        end += 24
        (_x.length, _x.width, _x.height,) = _get_struct_3d().unpack(str[start:end])
        _x = val1
        start = end
        end += 8
        (_x.prop_existence, _x.prop_mov,) = _get_struct_2f().unpack(str[start:end])
        _v15 = val1.classification
        _x = _v15
        start = end
        end += 28
        (_x.car, _x.truck, _x.motorcycle, _x.bicycle, _x.pedestrian, _x.stacionary, _x.other,) = _get_struct_7f().unpack(str[start:end])
        _v16 = val1.features
        _x = _v16
        start = end
        end += 8
        (_x.FL, _x.FM, _x.FR, _x.MR, _x.RR, _x.RM, _x.RL, _x.ML,) = _get_struct_8B().unpack(str[start:end])
        _v16.FL = bool(_v16.FL)
        _v16.FM = bool(_v16.FM)
        _v16.FR = bool(_v16.FR)
        _v16.MR = bool(_v16.MR)
        _v16.RR = bool(_v16.RR)
        _v16.RM = bool(_v16.RM)
        _v16.RL = bool(_v16.RL)
        _v16.ML = bool(_v16.ML)
        self.obj_list.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_7f = None
def _get_struct_7f():
    global _struct_7f
    if _struct_7f is None:
        _struct_7f = struct.Struct("<7f")
    return _struct_7f
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
_struct_36d = None
def _get_struct_36d():
    global _struct_36d
    if _struct_36d is None:
        _struct_36d = struct.Struct("<36d")
    return _struct_36d
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_8d = None
def _get_struct_8d():
    global _struct_8d
    if _struct_8d is None:
        _struct_8d = struct.Struct("<8d")
    return _struct_8d
_struct_8B = None
def _get_struct_8B():
    global _struct_8B
    if _struct_8B is None:
        _struct_8B = struct.Struct("<8B")
    return _struct_8B
_struct_2f = None
def _get_struct_2f():
    global _struct_2f
    if _struct_2f is None:
        _struct_2f = struct.Struct("<2f")
    return _struct_2f
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
