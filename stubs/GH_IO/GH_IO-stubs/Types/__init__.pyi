from typing import Tuple, Set, Iterable, List

class GH_Version:
    def __init__(self, v_major : int, v_minor : int, v_revision : int): ...
    def __init__(self, other : GH_Version): ...
    def op_Equality (A : GH_Version, B : GH_Version) -> bool: ...
    def op_Inequality (A : GH_Version, B : GH_Version) -> bool: ...
    def op_LessThan (A : GH_Version, B : GH_Version) -> bool: ...
    def op_LessThanOrEqual (A : GH_Version, B : GH_Version) -> bool: ...
    def op_GreaterThan (A : GH_Version, B : GH_Version) -> bool: ...
    def op_GreaterThanOrEqual (A : GH_Version, B : GH_Version) -> bool: ...
    def ToString (self) -> str: ...
    def GetHashCode (self) -> int: ...
    def Equals (self, obj : Object) -> bool: ...
class GH_Interval1D:
    def __init__(self, na : float, nb : float): ...
    def ToString (self) -> str: ...
class GH_Interval2D:
    def __init__(self, nu : GH_Interval1D, nv : GH_Interval1D): ...
    def __init__(self, nu0 : float, nu1 : float, nv0 : float, nv1 : float): ...
    def ToString (self) -> str: ...
class GH_Point2D:
    def __init__(self, nx : float, ny : float): ...
    def ToString (self) -> str: ...
class GH_Point3D:
    def __init__(self, nx : float, ny : float, nz : float): ...
    def ToString (self) -> str: ...
class GH_Point4D:
    def __init__(self, nx : float, ny : float, nz : float, nw : float): ...
    def ToString (self) -> str: ...
class GH_Line:
    def __init__(self, nA : GH_Point3D, nB : GH_Point3D): ...
    def __init__(self, Ax : float, Ay : float, Az : float, Bx : float, By : float, Bz : float): ...
    def ToString (self) -> str: ...
class GH_BoundingBox:
    def __init__(self, nMin : GH_Point3D, nMax : GH_Point3D): ...
    def __init__(self, Minx : float, Miny : float, Minz : float, Maxx : float, Maxy : float, Maxz : float): ...
    def ToString (self) -> str: ...
class GH_Plane:
    def __init__(self, nOrigin : GH_Point3D, nXAxis : GH_Point3D, nYAxis : GH_Point3D): ...
    def __init__(self, Ox : float, Oy : float, Oz : float, Xx : float, Xy : float, Xz : float, Yx : float, Yy : float, Yz : float): ...
    def ToString (self) -> str: ...
class GH_Item:
    def __init__(self, item_name : str, item_data : bool): ...
    def __init__(self, item_name : str, item_index : int, item_data : bool): ...
    def __init__(self, item_name : str, item_data : Byte): ...
    def __init__(self, item_name : str, item_index : int, item_data : Byte): ...
    def __init__(self, item_name : str, item_data : int): ...
    def __init__(self, item_name : str, item_index : int, item_data : int): ...
    def __init__(self, item_name : str, item_data : Int64): ...
    def __init__(self, item_name : str, item_index : int, item_data : Int64): ...
    def __init__(self, item_name : str, item_data : Single): ...
    def __init__(self, item_name : str, item_index : int, item_data : Single): ...
    def __init__(self, item_name : str, item_data : float): ...
    def __init__(self, item_name : str, item_index : int, item_data : float): ...
    def __init__(self, item_name : str, item_data : Decimal): ...
    def __init__(self, item_name : str, item_index : int, item_data : Decimal): ...
    def __init__(self, item_name : str, item_data : DateTime): ...
    def __init__(self, item_name : str, item_index : int, item_data : DateTime): ...
    def __init__(self, item_name : str, item_data : Guid): ...
    def __init__(self, item_name : str, item_index : int, item_data : Guid): ...
    def __init__(self, item_name : str, item_data : str): ...
    def __init__(self, item_name : str, item_index : int, item_data : str): ...
    def __init__(self, item_name : str, item_data : Set(Byte)): ...
    def __init__(self, item_name : str, item_index : int, item_data : Set(Byte)): ...
    def __init__(self, item_name : str, item_data : Set(float)): ...
    def __init__(self, item_name : str, item_index : int, item_data : Set(float)): ...
    def __init__(self, item_name : str, item_data : Point): ...
    def __init__(self, item_name : str, item_index : int, item_data : Point): ...
    def __init__(self, item_name : str, item_data : PointF): ...
    def __init__(self, item_name : str, item_index : int, item_data : PointF): ...
    def __init__(self, item_name : str, item_data : Size): ...
    def __init__(self, item_name : str, item_index : int, item_data : Size): ...
    def __init__(self, item_name : str, item_data : SizeF): ...
    def __init__(self, item_name : str, item_index : int, item_data : SizeF): ...
    def __init__(self, item_name : str, item_data : Rectangle): ...
    def __init__(self, item_name : str, item_index : int, item_data : Rectangle): ...
    def __init__(self, item_name : str, item_data : RectangleF): ...
    def __init__(self, item_name : str, item_index : int, item_data : RectangleF): ...
    def __init__(self, item_name : str, item_data : Color): ...
    def __init__(self, item_name : str, item_index : int, item_data : Color): ...
    def __init__(self, item_name : str, item_data : Bitmap): ...
    def __init__(self, item_name : str, item_index : int, item_data : Bitmap): ...
    def __init__(self, item_name : str, item_data : GH_Point2D): ...
    def __init__(self, item_name : str, item_index : int, item_data : GH_Point2D): ...
    def __init__(self, item_name : str, item_data : GH_Point3D): ...
    def __init__(self, item_name : str, item_index : int, item_data : GH_Point3D): ...
    def __init__(self, item_name : str, item_data : GH_Point4D): ...
    def __init__(self, item_name : str, item_index : int, item_data : GH_Point4D): ...
    def __init__(self, item_name : str, item_data : GH_Interval1D): ...
    def __init__(self, item_name : str, item_index : int, item_data : GH_Interval1D): ...
    def __init__(self, item_name : str, item_data : GH_Interval2D): ...
    def __init__(self, item_name : str, item_index : int, item_data : GH_Interval2D): ...
    def __init__(self, item_name : str, item_data : GH_Line): ...
    def __init__(self, item_name : str, item_index : int, item_data : GH_Line): ...
    def __init__(self, item_name : str, item_data : GH_BoundingBox): ...
    def __init__(self, item_name : str, item_index : int, item_data : GH_BoundingBox): ...
    def __init__(self, item_name : str, item_data : GH_Plane): ...
    def __init__(self, item_name : str, item_index : int, item_data : GH_Plane): ...
    def __init__(self, item_name : str, item_data : GH_Version): ...
    def __init__(self, item_name : str, item_index : int, item_data : GH_Version): ...
    @property
    def _double (self) -> float: ...
    @property
    def _decimal (self) -> Decimal: ...
    @property
    def _date (self) -> DateTime: ...
    @property
    def _guid (self) -> Guid: ...
    @property
    def _string (self) -> str: ...
    @property
    def _bytearray (self) -> Set(Byte): ...
    @property
    def _doublearray (self) -> Set(float): ...
    @property
    def _drawing_point (self) -> Point: ...
    @property
    def _drawing_pointf (self) -> PointF: ...
    @property
    def _drawing_size (self) -> Size: ...
    @property
    def _drawing_sizef (self) -> SizeF: ...
    @property
    def _drawing_rectangle (self) -> Rectangle: ...
    @property
    def _drawing_rectanglef (self) -> RectangleF: ...
    @property
    def _drawing_color (self) -> Color: ...
    @property
    def _drawing_bitmap (self) -> Bitmap: ...
    @property
    def _point2d (self) -> GH_Point2D: ...
    @property
    def _point3d (self) -> GH_Point3D: ...
    @property
    def _point4d (self) -> GH_Point4D: ...
    @property
    def _interval1d (self) -> GH_Interval1D: ...
    @property
    def _interval2d (self) -> GH_Interval2D: ...
    @property
    def _line (self) -> GH_Line: ...
    @property
    def _boundingbox (self) -> GH_BoundingBox: ...
    @property
    def _plane (self) -> GH_Plane: ...
    @property
    def _version (self) -> GH_Version: ...
    def CreateFrom (reader : BinaryReader) -> GH_Item: ...
    def CreateFrom (node : XmlNode) -> GH_Item: ...
    def Write (self, writer : BinaryWriter) -> None: ...
    def Read (self, reader : BinaryReader) -> None: ...
    def Write (self, writer : XmlWriter) -> None: ...
    def Read (self, node : XmlNode) -> None: ...
    @property
    def HasType (self) -> bool: ...
    @property
    def HasName (self) -> bool: ...
    @property
    def HasIndex (self) -> bool: ...
    @property
    def Type (self) -> GH_Types: ...
    @property
    def Name (self) -> str: ...
    @Name.setter
    def Name (self, value : str) -> None: ...
    @property
    def Index (self) -> int: ...
    @Index.setter
    def Index (self, value : int) -> None: ...
    def ToString (self) -> str: ...
    @property
    def DebuggerDisplay (self) -> str: ...
    @property
    def InternalData (self) -> Object: ...
    @property
    def _bool (self) -> bool: ...
    @property
    def _byte (self) -> Byte: ...
    @property
    def _int32 (self) -> int: ...
    @property
    def _int64 (self) -> Int64: ...
    @property
    def _single (self) -> Single: ...
class GH_Types:
    unset = 0
    gh_bool = 1
    gh_byte = 2
    gh_int32 = 3
    gh_int64 = 4
    gh_single = 5
    gh_double = 6
    gh_decimal = 7
    gh_date = 8
    gh_guid = 9
    gh_string = 10
    gh_bytearray = 20
    gh_doublearray = 21
    gh_drawing_point = 30
    gh_drawing_pointf = 31
    gh_drawing_size = 32
    gh_drawing_sizef = 33
    gh_drawing_rectangle = 34
    gh_drawing_rectanglef = 35
    gh_drawing_color = 36
    gh_drawing_bitmap = 37
    gh_point2d = 50
    gh_point3d = 51
    gh_point4d = 52
    gh_interval1d = 60
    gh_interval2d = 61
    gh_line = 70
    gh_boundingbox = 71
    gh_plane = 72
    gh_version = 80
