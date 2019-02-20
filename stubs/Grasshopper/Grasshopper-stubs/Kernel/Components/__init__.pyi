from typing import Tuple, Set, Iterable, List

class GH_DocExampleComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_MetaBallComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
    def SolveMetaBall (component : GH_Component, DA : IGH_DataAccess, context : GH_Context, plane : Plane, threshold : float) -> None: ...
class GH_MetaBallComponentThreshold(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_MetaBallComponentThresholdEx(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_GrasshopperLibraryInfo(GH_AssemblyInfo):
    def __init__(self): ...
    @property
    def Name (self) -> str: ...
    @property
    def Description (self) -> str: ...
    @property
    def Version (self) -> str: ...
    @property
    def License (self) -> GH_LibraryLicense: ...
    @property
    def Icon (self) -> Bitmap: ...
    @property
    def Id (self) -> Guid: ...
    @property
    def AuthorName (self) -> str: ...
    @property
    def AuthorContact (self) -> str: ...
class GH_CleanTreeComponent_OBSOLETE(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_CleanTreeComponent_OSBOLETE_AS_WELL(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_CleanComponentUpgrader:
    def __init__(self): ...
    @property
    def UpgradeFrom (self) -> Guid: ...
    @property
    def UpgradeTo (self) -> Guid: ...
    @property
    def Version (self) -> DateTime: ...
    def Upgrade (self, target : IGH_DocumentObject, document : GH_Document) -> IGH_DocumentObject: ...
class GH_CleanTreeComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
    def CanInsertParameter (self, side : GH_ParameterSide, index : int) -> bool: ...
    def CanRemoveParameter (self, side : GH_ParameterSide, index : int) -> bool: ...
    def CreateParameter (self, side : GH_ParameterSide, index : int) -> IGH_Param: ...
    def DestroyParameter (self, side : GH_ParameterSide, index : int) -> bool: ...
    def VariableParameterMaintenance (self) -> None: ...
class GH_IsNullDataComponent_OBSOLETE(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_PruneTreeComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_GraftTreeComponent_OBSOLETE(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_GraftTreeComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_SimplifyTreeComponent_OBSOLETE(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_SimplifyTreeComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
    def AddedToDocument (self, document : GH_Document) -> None: ...
    def RemovedFromDocument (self, document : GH_Document) -> None: ...
    def MovedBetweenDocuments (self, oldDocument : GH_Document, newDocument : GH_Document) -> None: ...
class GH_SimplifyComponentUpgrader:
    def __init__(self): ...
    @property
    def UpgradeFrom (self) -> Guid: ...
    @property
    def UpgradeTo (self) -> Guid: ...
    @property
    def Version (self) -> DateTime: ...
    def Upgrade (self, target : IGH_DocumentObject, document : GH_Document) -> IGH_DocumentObject: ...
class GH_FlattenTreeComponent_OBSOLETE(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_FlattenTreeComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_FlattenComponentUpgrader:
    def __init__(self): ...
    @property
    def UpgradeFrom (self) -> Guid: ...
    @property
    def UpgradeTo (self) -> Guid: ...
    @property
    def Version (self) -> DateTime: ...
    def Upgrade (self, target : IGH_DocumentObject, document : GH_Document) -> IGH_DocumentObject: ...
class GH_UnflattenTreeComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_TrimTreeComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_MatchTreeComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_ReplacePathComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_ExplodeTreeComponent_OBSOLETE(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
    @property
    def IsInputVariable (self) -> bool: ...
    @property
    def IsOutputVariable (self) -> bool: ...
    def IsVariableParam (self, e : GH_VarParamEventArgs) -> bool: ...
    def ConstructVariable (self, e : GH_VarParamEventArgs) -> IGH_Param: ...
    def ManagerConstructed (self, side : GH_VarParamSide, manager : GH_VariableParameterManager) -> None: ...
    def ParametersModified (self, side : GH_VarParamSide) -> None: ...
class GH_ExplodeTreeComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
    def CanInsertParameter (self, side : GH_ParameterSide, index : int) -> bool: ...
    def CanRemoveParameter (self, side : GH_ParameterSide, index : int) -> bool: ...
    def CreateParameter (self, side : GH_ParameterSide, index : int) -> IGH_Param: ...
    def DestroyParameter (self, side : GH_ParameterSide, index : int) -> bool: ...
    def VariableParameterMaintenance (self) -> None: ...
class GH_UpgradeExplodeComponent:
    def __init__(self): ...
    @property
    def UpgradeFrom (self) -> Guid: ...
    @property
    def UpgradeTo (self) -> Guid: ...
    @property
    def Version (self) -> DateTime: ...
    def Upgrade (self, target : IGH_DocumentObject, document : GH_Document) -> IGH_DocumentObject: ...
class GH_FlipDataMatrixComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_ShiftDataPathComponent(GH_Component):
    def __init__(self): ...
    @property
    def ComponentGuid (self) -> Guid: ...
    @property
    def Exposure (self) -> GH_Exposure: ...
class GH_GroupGeometryComponent(GH_Component):
    def __init__(self): ...
    @property
    def ComponentGuid (self) -> Guid: ...
    @property
    def Exposure (self) -> GH_Exposure: ...
class GH_UngroupGeometryComponent(GH_Component):
    def __init__(self): ...
    @property
    def ComponentGuid (self) -> Guid: ...
    @property
    def Exposure (self) -> GH_Exposure: ...
class GH_MergeGroupComponent(GH_Component):
    def __init__(self): ...
    @property
    def ComponentGuid (self) -> Guid: ...
    @property
    def Exposure (self) -> GH_Exposure: ...
class GH_SplitGroupComponent(GH_Component):
    def __init__(self): ...
    @property
    def ComponentGuid (self) -> Guid: ...
    @property
    def Exposure (self) -> GH_Exposure: ...
class GH_DataDamAttributes(GH_ComponentAttributes):
    def __init__(self, owner : GH_DataDamComponent): ...
    def RespondToMouseMove (self, sender : GH_Canvas, e : GH_CanvasMouseEvent) -> GH_ObjectResponse: ...
    def RespondToMouseUp (self, sender : GH_Canvas, e : GH_CanvasMouseEvent) -> GH_ObjectResponse: ...
    def SetupTooltip (self, canvasPoint : PointF, e : GH_TooltipDisplayEventArgs) -> None: ...
class GH_DataDamComponent(GH_Component):
    def __init__(self): ...
    def CreateAttributes (self) -> None: ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
    def AppendMenuItems (self, menu : ToolStripDropDown) -> bool: ...
    @property
    def Mode (self) -> BufferMode: ...
    @Mode.setter
    def Mode (self, Value : BufferMode) -> None: ...
    @property
    def Delay (self) -> TimeSpan: ...
    @Delay.setter
    def Delay (self, Value : TimeSpan) -> None: ...
    @property
    def TransferPossible (self) -> bool: ...
    def ExpireSolution (self, recompute : bool) -> None: ...
    def RemovedFromDocument (self, document : GH_Document) -> None: ...
    def DocumentContextChanged (self, document : GH_Document, context : GH_DocumentContext) -> None: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
    def CanInsertParameter (self, side : GH_ParameterSide, index : int) -> bool: ...
    def CanRemoveParameter (self, side : GH_ParameterSide, index : int) -> bool: ...
    def CreateParameter (self, side : GH_ParameterSide, index : int) -> IGH_Param: ...
    def DestroyParameter (self, side : GH_ParameterSide, index : int) -> bool: ...
    def VariableParameterMaintenance (self) -> None: ...
class GH_SmoothNumbersComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_ReadFileComponentAttributes(GH_ComponentAttributes):
    def __init__(self, owner : GH_ReadFileComponent): ...
    def RespondToMouseDoubleClick (self, sender : GH_Canvas, e : GH_CanvasMouseEvent) -> GH_ObjectResponse: ...
class GH_ReadFileComponent(GH_Component):
    def __init__(self): ...
    def __init__(self, file : str): ...
    def CreateAttributes (self) -> None: ...
    def IsAcceptableFileFormat (filename : str) -> bool: ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
    def Menu_PerLineClicked (self, sender : Object, e : EventArgs) -> None: ...
    def Menu_ParserClicked (self, sender : Object, e : EventArgs) -> None: ...
    @property
    def PerLineParse (self) -> bool: ...
    @PerLineParse.setter
    def PerLineParse (self, Value : bool) -> None: ...
    @property
    def Parser (self) -> GH_LineParser: ...
    @Parser.setter
    def Parser (self, AutoPropertyValue : GH_LineParser) -> None: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_PathCompareComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_TreeSplitComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_StreamFilterComponent_OBSOLETE(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
    @property
    def IsInputVariable (self) -> bool: ...
    @property
    def IsOutputVariable (self) -> bool: ...
    def IsVariableParam (self, e : GH_VarParamEventArgs) -> bool: ...
    def ConstructVariable (self, e : GH_VarParamEventArgs) -> IGH_Param: ...
    def ParametersModified (self, side : GH_VarParamSide) -> None: ...
    def ManagerConstructed (self, side : GH_VarParamSide, manager : GH_VariableParameterManager) -> None: ...
class GH_StreamFilterComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
    def CanInsertParameter (self, side : GH_ParameterSide, index : int) -> bool: ...
    def CanRemoveParameter (self, side : GH_ParameterSide, index : int) -> bool: ...
    def CreateParameter (self, side : GH_ParameterSide, index : int) -> IGH_Param: ...
    def DestroyParameter (self, side : GH_ParameterSide, index : int) -> bool: ...
    def VariableParameterMaintenance (self) -> None: ...
class GH_StreamGateComponent_OBSOLETE(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
    @property
    def IsInputVariable (self) -> bool: ...
    @property
    def IsOutputVariable (self) -> bool: ...
    def IsVariableParam (self, e : GH_VarParamEventArgs) -> bool: ...
    def ConstructVariable (self, e : GH_VarParamEventArgs) -> IGH_Param: ...
    def ParametersModified (self, side : GH_VarParamSide) -> None: ...
    def ManagerConstructed (self, side : GH_VarParamSide, manager : GH_VariableParameterManager) -> None: ...
class GH_StreamGateComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
    def CanInsertParameter (self, side : GH_ParameterSide, index : int) -> bool: ...
    def CanRemoveParameter (self, side : GH_ParameterSide, index : int) -> bool: ...
    def CreateParameter (self, side : GH_ParameterSide, index : int) -> IGH_Param: ...
    def DestroyParameter (self, side : GH_ParameterSide, index : int) -> bool: ...
    def VariableParameterMaintenance (self) -> None: ...
class Upgrade_StreamGateComponent:
    def __init__(self): ...
    @property
    def UpgradeFrom (self) -> Guid: ...
    @property
    def UpgradeTo (self) -> Guid: ...
    @property
    def Version (self) -> DateTime: ...
    def Upgrade (self, target : IGH_DocumentObject, document : GH_Document) -> IGH_DocumentObject: ...
class GH_CustomPreviewComponent(GH_Component):
    def __init__(self): ...
    @property
    def ComponentGuid (self) -> Guid: ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def DisplayItems (self) -> Iterable[GH_CustomPreviewItem]: ...
    @property
    def IncludeInRender (self) -> bool: ...
    @IncludeInRender.setter
    def IncludeInRender (self, AutoPropertyValue : bool) -> None: ...
    def ClearData (self) -> None: ...
    @property
    def ClippingBox (self) -> BoundingBox: ...
    def DrawViewportWires (self, args : IGH_PreviewArgs) -> None: ...
    def DrawViewportMeshes (self, args : IGH_PreviewArgs) -> None: ...
    @property
    def ViewportFilter (self) -> str: ...
    @ViewportFilter.setter
    def ViewportFilter (self, AutoPropertyValue : str) -> None: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
    def AppendRenderGeometry (self, args : GH_RenderArgs) -> None: ...
    @property
    def IsBakeCapable (self) -> bool: ...
    def BakeGeometry (self, doc : RhinoDoc, att : ObjectAttributes, objectIds : List) -> None: ...
class GH_CustomPreviewItem:
    def PushToRenderPipeline (self, args : GH_RenderArgs) -> None: ...
    def PushToRhinoDocument (self, doc : RhinoDoc, att : ObjectAttributes) -> Guid: ...
class GH_CurvatureGraphComponent(GH_Component):
    def __init__(self): ...
    def ClearData (self) -> None: ...
    def DrawViewportWires (self, args : IGH_PreviewArgs) -> None: ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_PointListComponent(GH_Component):
    def __init__(self): ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
    @property
    def IsPreviewCapable (self) -> bool: ...
    @property
    def ClippingBox (self) -> BoundingBox: ...
    def DrawViewportWires (self, args : IGH_PreviewArgs) -> None: ...
    def BakeGeometry (self, doc : RhinoDoc, att : ObjectAttributes, obj_ids : List) -> None: ...
class GH_TextTag3DComponent_OBSOLETE(GH_Component):
    def __init__(self): ...
    def ClearData (self) -> None: ...
    def BakeGeometry (self, doc : RhinoDoc, obj_ids : List) -> None: ...
    @property
    def IsPreviewCapable (self) -> bool: ...
    @property
    def ClippingBox (self) -> BoundingBox: ...
    def DrawViewportWires (self, args : IGH_PreviewArgs) -> None: ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_TextTag3DComponent_OBSOLETE_AS_WELL(GH_Component):
    def __init__(self): ...
    def ClearData (self) -> None: ...
    def BakeGeometry (self, doc : RhinoDoc, obj_ids : List) -> None: ...
    def BakeGeometry (self, doc : RhinoDoc, att : ObjectAttributes, obj_ids : List) -> None: ...
    @property
    def IsPreviewCapable (self) -> bool: ...
    @property
    def ClippingBox (self) -> BoundingBox: ...
    def DrawViewportWires (self, args : IGH_PreviewArgs) -> None: ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_TextTag3DComponent(GH_Component):
    def __init__(self): ...
    def ClearData (self) -> None: ...
    def BakeGeometry (self, doc : RhinoDoc, obj_ids : List) -> None: ...
    def BakeGeometry (self, doc : RhinoDoc, att : ObjectAttributes, obj_ids : List) -> None: ...
    @property
    def IsPreviewCapable (self) -> bool: ...
    @property
    def ClippingBox (self) -> BoundingBox: ...
    def DrawViewportWires (self, args : IGH_PreviewArgs) -> None: ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
class GH_TextTag3DUpgrader:
    def __init__(self): ...
    @property
    def UpgradeFrom (self) -> Guid: ...
    @property
    def UpgradeTo (self) -> Guid: ...
    @property
    def Version (self) -> DateTime: ...
    def Upgrade (self, target : IGH_DocumentObject, document : GH_Document) -> IGH_DocumentObject: ...
class GH_TextTagComponent_OBSOLETE(GH_Component):
    def __init__(self): ...
    def ClearData (self) -> None: ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
    def BakeGeometry (self, doc : RhinoDoc, obj_ids : List) -> None: ...
    @property
    def IsPreviewCapable (self) -> bool: ...
    @property
    def ClippingBox (self) -> BoundingBox: ...
    def DrawViewportWires (self, args : IGH_PreviewArgs) -> None: ...
    @property
    def TagHeight (self) -> int: ...
    @TagHeight.setter
    def TagHeight (self, Value : int) -> None: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class GH_TextTagComponent(GH_Component):
    def __init__(self): ...
    def ClearData (self) -> None: ...
    @property
    def Exposure (self) -> GH_Exposure: ...
    @property
    def ComponentGuid (self) -> Guid: ...
    def BakeGeometry (self, doc : RhinoDoc, obj_ids : List) -> None: ...
    def BakeGeometry (self, doc : RhinoDoc, att : ObjectAttributes, obj_ids : List) -> None: ...
    @property
    def IsPreviewCapable (self) -> bool: ...
    @property
    def ClippingBox (self) -> BoundingBox: ...
    def DrawViewportWires (self, args : IGH_PreviewArgs) -> None: ...
    @property
    def TagHeight (self) -> int: ...
    @TagHeight.setter
    def TagHeight (self, Value : int) -> None: ...
    def Write (self, writer : GH_IWriter) -> bool: ...
    def Read (self, reader : GH_IReader) -> bool: ...
class BufferMode:
    Never = 0
    Always = 1
    Delay = 2
