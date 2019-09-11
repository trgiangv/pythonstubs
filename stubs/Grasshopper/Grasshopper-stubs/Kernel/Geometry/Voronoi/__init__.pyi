from typing import Tuple, Set, Iterable, List


class Cell3Facet:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, pts: Iterable[Point3d]): ...
    @overload
    def __init__(self, other: Cell3Facet): ...
    @property
    def Original(self) -> bool: ...
    @Original.setter
    def Original(self, Value: bool) -> None: ...
    @property
    def MidPoint(self) -> Point3d: ...
    @property
    def Radius(self) -> float: ...
    def DestroyCaches(self) -> None: ...
    def CleanUp(self, tolerance: float, minDistance: float) -> Tuple[float]: ...


class Cell3:
    @overload
    def __init__(self, center: Point3d, box: Box): ...
    @overload
    def __init__(self, other: Cell3): ...
    @property
    def Facets(self) -> List: ...
    @property
    def BoundaryCount(self) -> int: ...
    @property
    def Center(self) -> Point3d: ...
    @property
    def Tolerance(self) -> float: ...
    @Tolerance.setter
    def Tolerance(self, Value: float) -> None: ...
    @property
    def AngleTolerance(self) -> float: ...
    def MidPlane(A: Point3d, B: Point3d) -> Plane: ...
    @overload
    def Slice(self, pt: Point3d) -> None: ...
    @overload
    def Slice(self, pt: Iterable[Point3d]) -> None: ...
    @overload
    def Slice(self, pt: Set(Point3d)) -> None: ...
    @overload
    def Slice(self, section: Plane) -> None: ...
    def ToBrep(self) -> Brep: ...


class Cell2:
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, pt: Node2, Radius: float): ...
    @overload
    def __init__(self, pt: Node2, Contour: Iterable[Node2]): ...
    @overload
    def Slice(self, other: Node2) -> bool: ...
    @overload
    def Slice(self, line: Line2) -> bool: ...
    def SliceConvexNGon(V: List, line: Line2, side: Side2, changed: bool) -> Tuple[List, bool]: ...
    def Radius(self) -> float: ...
    def Edges(self) -> List: ...
    def ToPolyline(self) -> Polyline: ...
    def ToPolyCurve(self, radius: float) -> PolyCurve: ...
    def ToGraphicsPath(self) -> GraphicsPath: ...


class Solver:
    def Solve_BruteForce(nodes: Node2List, outline: Iterable[Node2]) -> List: ...
    def Solve_Connectivity(nodes: Node2List, diagram: Connectivity, outline: Iterable[Node2]) -> List: ...
