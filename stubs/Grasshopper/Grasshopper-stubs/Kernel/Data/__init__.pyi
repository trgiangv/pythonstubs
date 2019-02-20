from typing import Tuple, Set, Iterable, List

class GH_IndexRange:
    def __init__(self, index : int): ...
    def __init__(self, index0 : int, index1 : int): ...
    @property
    def MaxValue () -> GH_IndexRange: ...
    def Union (range0 : GH_IndexRange, range1 : GH_IndexRange) -> GH_IndexRange: ...
    def Intersection (range0 : GH_IndexRange, range1 : GH_IndexRange) -> GH_IndexRange: ...
    def Split (range : GH_IndexRange, splitter : GH_IndexRange) -> Tuple[int, GH_IndexRange, GH_IndexRange]: ...
    @property
    def InvalidRange () -> GH_IndexRange: ...
    @property
    def Index0 (self) -> int: ...
    @property
    def Index1 (self) -> int: ...
    @property
    def Length (self) -> int: ...
    @property
    def IsSingular (self) -> bool: ...
    @property
    def IsValid (self) -> bool: ...
    def IntersectsWith (self, range : GH_IndexRange) -> bool: ...
    def AdjacentTo (self, range : GH_IndexRange) -> bool: ...
    def Contains (self, range : GH_IndexRange) -> bool: ...
    def Contains (self, index : int) -> bool: ...
    def ToString (self) -> str: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_IndexRanges:
    def __init__(self): ...
    @property
    def Count (self) -> int: ...
    @property
    def Range (self, index : int) -> GH_IndexRange: ...
    def InsertRange (self, range : GH_IndexRange) -> bool: ...
    def RemoveRange (self, range : GH_IndexRange) -> bool: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
    def ToString (self) -> str: ...
class GH_TreeIndex:
    def __init__(self, path : GH_Path, item : int): ...
    @property
    def Path (self) -> GH_Path: ...
    @Path.setter
    def Path (self, AutoPropertyValue : GH_Path) -> None: ...
    @property
    def Item (self) -> int: ...
    @Item.setter
    def Item (self, AutoPropertyValue : int) -> None: ...
class GH_RuleResult:
    NoOpinion = 0
    Include = 1
    Exclude = -1
class IGH_IndexRule:
    def Evaluate (self, index : int) -> GH_RuleResult: ...
class GH_IndexRuleSet:
    def __init__(self): ...
    @property
    def Count (self) -> int: ...
    @property
    def Rule (self, index : int) -> IGH_IndexRule: ...
    def AddDigitRule (self, digit : int, invert : bool) -> None: ...
    def AddRangeRule (self, range : GH_IndexRange, invert : bool) -> None: ...
    def AddAnyDigitRule (self) -> None: ...
    def AddAnyDigitsRule (self) -> None: ...
    def AddDigitPatternRule (self, firstDigit : int, nextDigit : int) -> None: ...
    def AddDigitPatternRule (self, firstDigit : int, nextDigit : int, lastDigit : int) -> None: ...
    def AddDigitPatternRule (self, pattern : Set(int)) -> None: ...
    def AddRangePatternRule (self, pattern : Set(GH_IndexRange)) -> None: ...
    def Evaluate (self, index : int) -> GH_RuleResult: ...
class GH_TreeFilter:
    def __init__(self): ...
    def ParsePattern (filter : str) -> GH_TreeFilter: ...
    def FindPathBrackets (text : str) -> Tuple[bool, int, int]: ...
    def FindItemBrackets (text : str) -> Tuple[bool, int, int]: ...
    def FindNextLevelChar (text : str, index : int, char : Char) -> int: ...
    def FindPrevLevelChar (text : str, index : int, char : Char) -> int: ...
    def SplitStringWithExpressions (text : str, separator : Char) -> List: ...
class GH_BracketMismatchException:
    def __init__(self): ...
    def __init__(self, message : str): ...
    def __init__(self, message : str, location : int): ...
    @property
    def Index (self) -> int: ...
class GH_StringMismatchException:
    def __init__(self): ...
    def __init__(self, message : str): ...
class GH_RuleKind:
    None = 0
    AnyNumber = 1
    AnyNumbers = 2
    Number = 3
    Group = 4
    Range = 5
    Sequence = 6
    Complex = 7
class GH_RuleOperator:
    Conjunction = 0
    Disjunction = 1
class IGH_Rule:
    @property
    def Kind (self) -> GH_RuleKind: ...
    @property
    def Notation (self) -> str: ...
    def Apply (self, number : int) -> bool: ...
class GH_RuleAnyNumbers:
    def __init__(self): ...
    def Apply (self, number : int) -> bool: ...
    @property
    def Notation (self) -> str: ...
    @property
    def Kind (self) -> GH_RuleKind: ...
class GH_RuleAnyNumber:
    def __init__(self): ...
    def Apply (self, number : int) -> bool: ...
    @property
    def Notation (self) -> str: ...
    @property
    def Kind (self) -> GH_RuleKind: ...
class GH_RuleNumber:
    def __init__(self, number : int, negate : bool): ...
    def Apply (self, number : int) -> bool: ...
    @property
    def Notation (self) -> str: ...
    @property
    def Kind (self) -> GH_RuleKind: ...
class GH_RuleGroup:
    def __init__(self, numbers : Iterable[int], negate : bool): ...
    def Apply (self, number : int) -> bool: ...
    @property
    def Notation (self) -> str: ...
    @property
    def Kind (self) -> GH_RuleKind: ...
class GH_RuleRange:
    def __init__(self, min : int, max : int, negate : bool): ...
    def Apply (self, number : int) -> bool: ...
    @property
    def Notation (self) -> str: ...
    @property
    def Kind (self) -> GH_RuleKind: ...
class GH_RuleSequence:
    def __init__(self, sequence : Iterable[int], limit : int, negate : bool): ...
    def Apply (self, number : int) -> bool: ...
    @property
    def Notation (self) -> str: ...
    @property
    def Kind (self) -> GH_RuleKind: ...
class GH_RuleComplex:
    def __init__(self, fragments : Iterable[IGH_Rule], operators : Iterable[GH_RuleOperator]): ...
    def Apply (self, number : int) -> bool: ...
    @property
    def Notation (self) -> str: ...
    @property
    def Kind (self) -> GH_RuleKind: ...
class GH_TreeRules:
    def __init__(self, pathRules : Iterable[IGH_Rule], indexRule : IGH_Rule): ...
    def ToString (self) -> str: ...
    def FromString (text : str, message : str) -> Tuple[GH_TreeRules, str]: ...
    @property
    def PathRuleCount (self) -> int: ...
    @property
    def HasPathRules (self) -> bool: ...
    @property
    def HasItemRule (self) -> bool: ...
    def Apply (self, path : GH_Path, index : int) -> bool: ...
    def Apply (self, path : GH_Path) -> bool: ...
class IGH_DataTree:
    def MergeWithParameter (self, param : IGH_Param) -> bool: ...
class GH_DirtyCaster:
    def CastToList (in : Object) -> List: ...
    def CastToTree (in : Object) -> DataTree: ...
class GH_Path:
    def __init__(self): ...
    def __init__(self, index : int): ...
    def __init__(self, args : Set(int)): ...
    def __init__(self, Other : GH_Path): ...
    def op_Equality (A : GH_Path, B : GH_Path) -> bool: ...
    def op_Inequality (A : GH_Path, B : GH_Path) -> bool: ...
    def op_LessThan (A : GH_Path, B : GH_Path) -> bool: ...
    def op_GreaterThan (A : GH_Path, B : GH_Path) -> bool: ...
    def GetHashCode (self) -> int: ...
    def CompareTo (self, other : GH_Path) -> int: ...
    def Compare (self, x : GH_Path, y : GH_Path) -> int: ...
    @property
    def Dimension (self, index : int) -> int: ...
    @Dimension.setter
    def Dimension (self, index : int, Value : int) -> None: ...
    @property
    def DebuggerDisplay (self) -> str: ...
    @property
    def Indices (self) -> Set(int): ...
    @Indices.setter
    def Indices (self, Value : Set(int)) -> None: ...
    @property
    def InternalPath (self) -> Set(int): ...
    @InternalPath.setter
    def InternalPath (self, Value : Set(int)) -> None: ...
    @property
    def Length (self) -> int: ...
    @property
    def Valid (self) -> bool: ...
    def ToString (self) -> str: ...
    def ToString (self, includeBrackets : bool) -> str: ...
    def Format (self, format_provider : str, separator : str) -> str: ...
    def SplitPathLikeString (s : str) -> Tuple[bool, Set(str), str]: ...
    def FromString (self, s : str) -> bool: ...
    def IsCoincident (self, other : GH_Path) -> bool: ...
    def IsCoincident (self, index_list : Set(int)) -> bool: ...
    def IsAncestor (self, potential_ancestor : GH_Path, additional_generations : int) -> Tuple[bool, int]: ...
    def AppendElement (self, index : int) -> GH_Path: ...
    def PrependElement (self, index : int) -> GH_Path: ...
    def CullElement (self) -> GH_Path: ...
    def CullFirstElement (self) -> GH_Path: ...
    def Increment (self, index : int) -> GH_Path: ...
    def Increment (self, index : int, offset : int) -> GH_Path: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_Lexer:
    def __init__(self): ...
    def __init__(self, M : str): ...
    @property
    def Mask (self) -> str: ...
    @property
    def Item (self) -> str: ...
    @property
    def Path (self) -> List: ...
    @property
    def IsItem (self) -> bool: ...
    @property
    def IsPath (self) -> bool: ...
    def EvaluatePath (self, evaluator : GH_ExpressionParser, path : GH_Path, index : int) -> Tuple[bool, GH_Path, int]: ...
    def PerformLexicalReplace (source : GH_Lexer, target : GH_Lexer, structure_in : IGH_Structure, structure_out : GH_Structure) -> None: ...
    def PerformLexicalReplace (source : GH_Lexer, target : GH_Lexer, tree_in : DataTree, tree_out : DataTree) -> None: ...
class GH_LexerCombo:
    def __init__(self): ...
    def __init__(self, n_source : GH_Lexer, n_target : GH_Lexer): ...
    def __init__(self, n_source : str, n_target : str): ...
    @property
    def Source (self) -> GH_Lexer: ...
    @Source.setter
    def Source (self, Value : GH_Lexer) -> None: ...
    @property
    def Target (self) -> GH_Lexer: ...
    @Target.setter
    def Target (self, Value : GH_Lexer) -> None: ...
class GH_PathOffset:
    def __init__(self): ...
    def __init__(self, pathShift : Iterable[int]): ...
    def __init__(self, pathShift : Iterable[int], itemShift : int): ...
    def __init__(self, pathShift : Iterable[int], itemShift : int, pathWrap : bool, itemWrap : bool): ...
    def ParseString (mask : str) -> GH_PathOffset: ...
    @property
    def ItemOffset (self) -> int: ...
    @ItemOffset.setter
    def ItemOffset (self, Value : int) -> None: ...
    @property
    def PathOffset (self) -> List: ...
    @property
    def PathWrap (self) -> bool: ...
    @PathWrap.setter
    def PathWrap (self, Value : bool) -> None: ...
    @property
    def ItemWrap (self) -> bool: ...
    @ItemWrap.setter
    def ItemWrap (self, Value : bool) -> None: ...
    def ToString (self) -> str: ...
    def OffsetPath (self, path : GH_Path, index : int, rel_path : GH_Path, rel_index : int) -> Tuple[bool, GH_Path, int]: ...
    def OffsetPath (self, path : GH_Path, index : int, tree : IGH_Structure) -> Tuple[bool, GH_Path, int]: ...
class GH_GraphicBranch:
    def __init__(self): ...
    @property
    def Path (self) -> GH_Path: ...
    @Path.setter
    def Path (self, Value : GH_Path) -> None: ...
    @property
    def Data (self) -> IList: ...
    @Data.setter
    def Data (self, Value : IList) -> None: ...
    @property
    def IsEmpty (self) -> bool: ...
    @property
    def DataCount (self) -> int: ...
    @property
    def Offset (self) -> Single: ...
    @Offset.setter
    def Offset (self, Value : Single) -> None: ...
    @property
    def Length (self) -> Single: ...
    @Length.setter
    def Length (self, Value : Single) -> None: ...
    @property
    def Angle (self) -> Single: ...
    @Angle.setter
    def Angle (self, Value : Single) -> None: ...
    @property
    def Selected (self) -> bool: ...
    @Selected.setter
    def Selected (self, Value : bool) -> None: ...
    def SelectAll (self, bSelect : bool) -> None: ...
    def SelectAll (self, b_path : GH_Path) -> None: ...
    @property
    def Parent (self) -> GH_GraphicBranch: ...
    @Parent.setter
    def Parent (self, Value : GH_GraphicBranch) -> None: ...
    @property
    def Twigs (self) -> List: ...
    @Twigs.setter
    def Twigs (self, Value : List) -> None: ...
    @property
    def IsRoot (self) -> bool: ...
    @property
    def IsTrunk (self) -> bool: ...
    @property
    def IsLeaf (self) -> bool: ...
    @property
    def LongestPathLength (self) -> int: ...
    def GrowTree (self, paths : List) -> None: ...
    def SolveLeafAngles (self, angle : Single, spread : Single, angle_per_item : Single, args : GH_GraphicTreeDisplayArgs) -> None: ...
    def Distribute_Phylogenetic (self, max_path_length_inverse : float) -> None: ...
    def RenderWires_Schematic (self, G : Graphics, e : GH_GraphicTreeDisplayArgs) -> None: ...
    def RenderWires_Organic (self, G : Graphics, e : GH_GraphicTreeDisplayArgs) -> None: ...
    def RenderNodes (self, G : Graphics, e : GH_GraphicTreeDisplayArgs) -> None: ...
    def RenderTags (self, G : Graphics, e : GH_GraphicTreeDisplayArgs) -> None: ...
class GH_GraphicTreeDisplayArgs:
    def __init__(self): ...
    def SetupViewport (self, vport : GH_Viewport) -> None: ...
    def AdjustMaxPathLength (self, potential_new_length : int) -> None: ...
    def RadialX (self, angle : Single, offset : Single) -> Single: ...
    def RadialY (self, angle : Single, offset : Single) -> Single: ...
    def RadialCrd (self, angle : Single, offset : Single) -> PointF: ...
    def RadialBox (self, box_edge : Single) -> RectangleF: ...
    def Visible (self, pt : PointF) -> bool: ...
    def Visible (self, pt : PointF, radius : Single) -> bool: ...
    def Visible (self, rec : RectangleF) -> bool: ...
    def Visible (self, rec : RectangleF, margin : Single) -> bool: ...
    def Visible (self, ptA : PointF, ptB : PointF, fuzz : Single) -> bool: ...
    def Visible (self, P0 : PointF, P1 : PointF, P2 : PointF, P3 : PointF, fuzz : Single) -> bool: ...
    def RemapDegrees (a : Single) -> Single: ...
    def RadToDeg (a : Single) -> Single: ...
    def DistanceSquared (A : PointF, B : PointF) -> Single: ...
    def Distance (A : PointF, B : PointF) -> Single: ...
    def Distance (A : PointF, B : PointF, P : PointF) -> Single: ...
class GH_TreeBuilder:
    def __init__(self): ...
    def AddPath (self, p : GH_Path) -> None: ...
    def AddPathRecursive (self, p : GH_Path) -> None: ...
    @property
    def AllPaths (self) -> List: ...
class IGH_StructureEnumerator:
class GH_SimplificationMode:
    None = 0
    CollapseLeadingOverlaps = 1
    CollapseAllOverlaps = 2
class GH_ExpandMode:
    None = 0
    SimpleReplace = 1
    SimpleAppend = 2
    Recursive = 3
class GH_GraftMode:
    None = 0
    GraftNullItems = 1
    GraftEmptyLists = 2
    GraftAll = 3
class IGH_Structure:
    @property
    def IsEmpty (self) -> bool: ...
    @property
    def PathCount (self) -> int: ...
    @property
    def DataCount (self) -> int: ...
    @property
    def Paths (self) -> List[GH_Path]: ...
    @property
    def StructureProxy (self) -> List[IList]: ...
    @property
    def TopologyDescription (self) -> str: ...
    def PathExists (self, path : GH_Path) -> bool: ...
    def PathIndex (self, path : GH_Path, idx0 : int, idx1 : int) -> Tuple[int, int]: ...
    def LongestPathIndex (self) -> int: ...
    def ShortestPathIndex (self) -> int: ...
    def RemovePath (self, path : GH_Path) -> None: ...
    def ReplacePath (self, find : GH_Path, replace : GH_Path) -> None: ...
    def ExpandPath (self, path : GH_Path, element : int, mode : GH_ExpandMode) -> None: ...
    @property
    def Path (self, index : int) -> GH_Path: ...
    @property
    def Branch (self, path : GH_Path) -> IList: ...
    @property
    def Branch (self, index : int) -> IList: ...
    def AllData (self, skipNulls : bool) -> IGH_StructureEnumerator: ...
    def Clear (self) -> None: ...
    def ClearData (self) -> None: ...
    def TrimExcess (self) -> None: ...
    def EnsureCapacity (self, capacity : int) -> None: ...
    def Graft (self, clearSingleNulls : bool) -> None: ...
    def Graft (self, path : GH_Path, clearSingleNulls : bool) -> None: ...
    def Graft (self, mode : GH_GraftMode) -> None: ...
    def Graft (self, mode : GH_GraftMode, path : GH_Path) -> None: ...
    def Flatten (self, path : GH_Path) -> None: ...
    def Simplify (self, mode : GH_SimplificationMode) -> None: ...
    def DataDescription (self, includeIndices : bool, includePaths : bool) -> str: ...
class PathLengthComparer:
    def __init__(self): ...
    def Compare (self, x : GH_Path, y : GH_Path) -> int: ...
