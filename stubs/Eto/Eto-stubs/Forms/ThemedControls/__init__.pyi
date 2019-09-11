from typing import Tuple, Set, Iterable, List


class ThemedAboutDialogHandler:
    def __init__(self): ...
    @property
    def Copyright(self) -> str: ...
    @Copyright.setter
    def Copyright(self, value: str) -> None: ...
    @property
    def Designers(self) -> Set(str): ...
    @Designers.setter
    def Designers(self, value: Set(str)) -> None: ...
    @property
    def Developers(self) -> Set(str): ...
    @Developers.setter
    def Developers(self, value: Set(str)) -> None: ...
    @property
    def Documenters(self) -> Set(str): ...
    @Documenters.setter
    def Documenters(self, value: Set(str)) -> None: ...
    @property
    def License(self) -> str: ...
    @License.setter
    def License(self, value: str) -> None: ...
    @property
    def Logo(self) -> Image: ...
    @Logo.setter
    def Logo(self, value: Image) -> None: ...
    @property
    def ProgramDescription(self) -> str: ...
    @ProgramDescription.setter
    def ProgramDescription(self, value: str) -> None: ...
    @property
    def ProgramName(self) -> str: ...
    @ProgramName.setter
    def ProgramName(self, value: str) -> None: ...
    @property
    def Title(self) -> str: ...
    @Title.setter
    def Title(self, value: str) -> None: ...
    @property
    def Version(self) -> str: ...
    @Version.setter
    def Version(self, value: str) -> None: ...
    @property
    def Website(self) -> Uri: ...
    @Website.setter
    def Website(self, value: Uri) -> None: ...
    @property
    def WebsiteLabel(self) -> str: ...
    @WebsiteLabel.setter
    def WebsiteLabel(self, value: str) -> None: ...
    def ShowDialog(self, parent: Window) -> DialogResult: ...


class ThemedCollectionEditorHandler:
    def __init__(self): ...
    @property
    def DataStore(self) -> Iterable[Object]: ...
    @DataStore.setter
    def DataStore(self, value: Iterable[Object]) -> None: ...
    @property
    def ElementType(self) -> Type: ...
    @ElementType.setter
    def ElementType(self, value: Type) -> None: ...


class ThemedCollectionEditor(Panel):
    def __init__(self): ...
    @property
    def DataStore(self) -> Iterable[Object]: ...
    @DataStore.setter
    def DataStore(self, value: Iterable[Object]) -> None: ...
    @property
    def ElementType(self) -> Type: ...
    @ElementType.setter
    def ElementType(self, value: Type) -> None: ...
    @property
    def ExtraContent(self) -> Control: ...
    @ExtraContent.setter
    def ExtraContent(self, value: Control) -> None: ...


class ThemedDocumentControlHandler:
    def __init__(self): ...
    @property
    def TabPadding(self) -> Padding: ...
    @TabPadding.setter
    def TabPadding(self, value: Padding) -> None: ...
    @property
    def Font(self) -> Font: ...
    @Font.setter
    def Font(self, value: Font) -> None: ...
    def OnLoad(self, e: EventArgs) -> None: ...
    @property
    def SelectedIndex(self) -> int: ...
    @SelectedIndex.setter
    def SelectedIndex(self, value: int) -> None: ...
    @property
    def AllowReordering(self) -> bool: ...
    @AllowReordering.setter
    def AllowReordering(self, value: bool) -> None: ...
    def GetPage(self, index: int) -> DocumentPage: ...
    def GetPageCount(self) -> int: ...
    def InsertPage(self, index: int, page: DocumentPage) -> None: ...
    def RemovePage(self, index: int) -> None: ...
    @property
    def Enabled(self) -> bool: ...
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    def AttachEvent(self, id: str) -> None: ...


class ThemedDocumentPageHandler:
    def __init__(self): ...
    @property
    def Closable(self) -> bool: ...
    @Closable.setter
    def Closable(self, value: bool) -> None: ...
    @property
    def Content(self) -> Control: ...
    @Content.setter
    def Content(self, value: Control) -> None: ...
    @property
    def ContextMenu(self) -> ContextMenu: ...
    @ContextMenu.setter
    def ContextMenu(self, value: ContextMenu) -> None: ...
    @property
    def Image(self) -> Image: ...
    @Image.setter
    def Image(self, value: Image) -> None: ...
    @property
    def MinimumSize(self) -> Size: ...
    @MinimumSize.setter
    def MinimumSize(self, value: Size) -> None: ...
    @property
    def Padding(self) -> Padding: ...
    @Padding.setter
    def Padding(self, value: Padding) -> None: ...
    @property
    def Text(self) -> str: ...
    @Text.setter
    def Text(self, value: str) -> None: ...
    @property
    def PropagateLoadEvents(self) -> bool: ...


class ThemedExpanderHandler:
    def __init__(self): ...
    @property
    def ExpandedButtonText(self) -> str: ...
    @ExpandedButtonText.setter
    def ExpandedButtonText(self, value: str) -> None: ...
    @property
    def CollapsedButtonText(self) -> str: ...
    @CollapsedButtonText.setter
    def CollapsedButtonText(self, value: str) -> None: ...
    @property
    def Expanded(self) -> bool: ...
    @Expanded.setter
    def Expanded(self, value: bool) -> None: ...
    @property
    def Header(self) -> Control: ...
    @Header.setter
    def Header(self, value: Control) -> None: ...
    @property
    def Content(self) -> Control: ...
    @Content.setter
    def Content(self, value: Control) -> None: ...
    @property
    def Padding(self) -> Padding: ...
    @Padding.setter
    def Padding(self, value: Padding) -> None: ...
    @property
    def MinimumSize(self) -> Size: ...
    @MinimumSize.setter
    def MinimumSize(self, value: Size) -> None: ...
    @property
    def ContextMenu(self) -> ContextMenu: ...
    @ContextMenu.setter
    def ContextMenu(self, value: ContextMenu) -> None: ...
    def AttachEvent(self, id: str) -> None: ...


class ThemedFilePickerHandler:
    def __init__(self): ...
    @property
    def FileAction(self) -> FileAction: ...
    @FileAction.setter
    def FileAction(self, value: FileAction) -> None: ...
    @property
    def FilePath(self) -> str: ...
    @FilePath.setter
    def FilePath(self, value: str) -> None: ...
    @property
    def CurrentFilterIndex(self) -> int: ...
    @CurrentFilterIndex.setter
    def CurrentFilterIndex(self, value: int) -> None: ...
    @property
    def Title(self) -> str: ...
    @Title.setter
    def Title(self, value: str) -> None: ...
    def ClearFilters(self) -> None: ...
    def InsertFilter(self, index: int, filter: FileFilter) -> None: ...
    def RemoveFilter(self, index: int) -> None: ...
    def AttachEvent(self, id: str) -> None: ...


class ThemedFontPickerHandler:
    def __init__(self): ...
    @property
    def Value(self) -> Font: ...
    @Value.setter
    def Value(self, value: Font) -> None: ...
    def AttachEvent(self, id: str) -> None: ...


class ThemedPropertyGridHandler:
    def __init__(self): ...
    @property
    def SelectedObject(self) -> Object: ...
    @SelectedObject.setter
    def SelectedObject(self, value: Object) -> None: ...
    @property
    def SelectedObjects(self) -> Iterable[Object]: ...
    @SelectedObjects.setter
    def SelectedObjects(self, value: Iterable[Object]) -> None: ...
    @property
    def ShowCategories(self) -> bool: ...
    @ShowCategories.setter
    def ShowCategories(self, value: bool) -> None: ...
    @property
    def ShowDescription(self) -> bool: ...
    @ShowDescription.setter
    def ShowDescription(self, value: bool) -> None: ...
    def Refresh(self) -> None: ...
    def AttachEvent(self, id: str) -> None: ...


class ThemedPropertyGrid(Panel):
    def __init__(self): ...
    def add_PropertyValueChanged(self, value: EventHandler) -> None: ...
    def remove_PropertyValueChanged(self, value: EventHandler) -> None: ...
    def CreateCellValueBinding(self) -> IndirectBinding: ...
    @property
    def PropertyCellTypes(self) -> List[PropertyCellType]: ...
    @property
    def SelectedObjects(self) -> Iterable[Object]: ...
    @SelectedObjects.setter
    def SelectedObjects(self, value: Iterable[Object]) -> None: ...
    @property
    def UseValueTypeDefaults(self) -> bool: ...
    @UseValueTypeDefaults.setter
    def UseValueTypeDefaults(self, value: bool) -> None: ...
    @property
    def SelectedObject(self) -> Object: ...
    @SelectedObject.setter
    def SelectedObject(self, value: Object) -> None: ...
    def add_ShowCategoriesChanged(self, value: EventHandler) -> None: ...
    def remove_ShowCategoriesChanged(self, value: EventHandler) -> None: ...
    @property
    def ShowCategories(self) -> bool: ...
    @ShowCategories.setter
    def ShowCategories(self, value: bool) -> None: ...
    @property
    def ShowDescription(self) -> bool: ...
    @ShowDescription.setter
    def ShowDescription(self, value: bool) -> None: ...
    def Refresh(self) -> None: ...


class ThemedMenuSegmentedItemHandler:
    def __init__(self): ...
    @property
    def MenuDelay(self) -> TimeSpan: ...
    @MenuDelay.setter
    def MenuDelay(self, value: TimeSpan) -> None: ...
    @property
    def MenuIndicator(self) -> str: ...
    @MenuIndicator.setter
    def MenuIndicator(self, value: str) -> None: ...
    @property
    def Menu(self) -> ContextMenu: ...
    @Menu.setter
    def Menu(self, value: ContextMenu) -> None: ...
    @property
    def CanSelect(self) -> bool: ...
    @CanSelect.setter
    def CanSelect(self, value: bool) -> None: ...
    @property
    def Text(self) -> str: ...
    @Text.setter
    def Text(self, value: str) -> None: ...


class ThemedButtonSegmentedItemHandler:
    def __init__(self): ...




class ThemedSegmentedButtonHandler:
    def __init__(self): ...
    @property
    def SelectionMode(self) -> SegmentedSelectionMode: ...
    @SelectionMode.setter
    def SelectionMode(self, value: SegmentedSelectionMode) -> None: ...
    @property
    def Spacing(self) -> int: ...
    @Spacing.setter
    def Spacing(self, value: int) -> None: ...
    @property
    def SelectedIndex(self) -> int: ...
    @SelectedIndex.setter
    def SelectedIndex(self, value: int) -> None: ...
    @property
    def SelectedIndexes(self) -> Iterable[int]: ...
    @SelectedIndexes.setter
    def SelectedIndexes(self, value: Iterable[int]) -> None: ...
    def ClearItems(self) -> None: ...
    def ClearSelection(self) -> None: ...
    def InsertItem(self, index: int, item: SegmentedItem) -> None: ...
    def RemoveItem(self, index: int, item: SegmentedItem) -> None: ...
    def SelectAll(self) -> None: ...
    def SetItem(self, index: int, item: SegmentedItem) -> None: ...
    def AttachEvent(self, id: str) -> None: ...
    def OnPreLoad(self, e: EventArgs) -> None: ...
    def OnLoad(self, e: EventArgs) -> None: ...


class ThemedSpinnerMode:
    Line = 0
    Circle = 1


class ThemedSpinnerDirection:
    Clockwise = 1
    CounterClockwise = -1


class ThemedSpinnerHandler:
    def __init__(self): ...
    @property
    def Increment(self) -> Single: ...
    @Increment.setter
    def Increment(self, value: Single) -> None: ...
    @property
    def Direction(self) -> ThemedSpinnerDirection: ...
    @Direction.setter
    def Direction(self, value: ThemedSpinnerDirection) -> None: ...
    @property
    def DisabledAlpha(self) -> Single: ...
    @DisabledAlpha.setter
    def DisabledAlpha(self, value: Single) -> None: ...
    @property
    def ElementColor(self) -> Color: ...
    @ElementColor.setter
    def ElementColor(self, value: Color) -> None: ...
    @property
    def LineThickness(self) -> Single: ...
    @LineThickness.setter
    def LineThickness(self, value: Single) -> None: ...
    @property
    def LineCap(self) -> PenLineCap: ...
    @LineCap.setter
    def LineCap(self, value: PenLineCap) -> None: ...
    @property
    def ElementSize(self) -> Single: ...
    @ElementSize.setter
    def ElementSize(self, value: Single) -> None: ...
    @property
    def Mode(self) -> ThemedSpinnerMode: ...
    @Mode.setter
    def Mode(self, value: ThemedSpinnerMode) -> None: ...
    @property
    def NumberOfElements(self) -> int: ...
    @NumberOfElements.setter
    def NumberOfElements(self, value: int) -> None: ...
    @property
    def NumberOfVisibleElements(self) -> int: ...
    @NumberOfVisibleElements.setter
    def NumberOfVisibleElements(self, value: int) -> None: ...
    @property
    def Speed(self) -> float: ...
    @Speed.setter
    def Speed(self, value: float) -> None: ...
    def OnLoadComplete(self, e: EventArgs) -> None: ...
    def OnUnLoad(self, e: EventArgs) -> None: ...
    @property
    def Enabled(self) -> bool: ...
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...


class ThemedSplitterHandler:
    def __init__(self): ...
    @property
    def Orientation(self) -> Orientation: ...
    @Orientation.setter
    def Orientation(self, value: Orientation) -> None: ...
    @property
    def FixedPanel(self) -> SplitterFixedPanel: ...
    @FixedPanel.setter
    def FixedPanel(self, value: SplitterFixedPanel) -> None: ...
    @property
    def Position(self) -> int: ...
    @Position.setter
    def Position(self, value: int) -> None: ...
    @property
    def RelativePosition(self) -> float: ...
    @RelativePosition.setter
    def RelativePosition(self, value: float) -> None: ...
    @property
    def SplitterWidth(self) -> int: ...
    @SplitterWidth.setter
    def SplitterWidth(self, value: int) -> None: ...
    @property
    def Panel1(self) -> Control: ...
    @Panel1.setter
    def Panel1(self, value: Control) -> None: ...
    @property
    def Panel2(self) -> Control: ...
    @Panel2.setter
    def Panel2(self, value: Control) -> None: ...
    @property
    def Splitter(self) -> Panel: ...
    @property
    def Panel1MinimumSize(self) -> int: ...
    @Panel1MinimumSize.setter
    def Panel1MinimumSize(self, value: int) -> None: ...
    @property
    def Panel2MinimumSize(self) -> int: ...
    @Panel2MinimumSize.setter
    def Panel2MinimumSize(self, value: int) -> None: ...


class ThemedStepperHandler:
    def __init__(self): ...
    @property
    def UpText(self) -> str: ...
    @UpText.setter
    def UpText(self, value: str) -> None: ...
    @property
    def DownText(self) -> str: ...
    @DownText.setter
    def DownText(self, value: str) -> None: ...
    @property
    def Font(self) -> Font: ...
    @Font.setter
    def Font(self, value: Font) -> None: ...
    @property
    def Orientation(self) -> Orientation: ...
    @Orientation.setter
    def Orientation(self, value: Orientation) -> None: ...
    @property
    def ValidDirection(self) -> StepperValidDirections: ...
    @ValidDirection.setter
    def ValidDirection(self, value: StepperValidDirections) -> None: ...
    @property
    def Enabled(self) -> bool: ...
    @Enabled.setter
    def Enabled(self, value: bool) -> None: ...
    def AttachEvent(self, id: str) -> None: ...


class ThemedTextStepperHandler:
    def __init__(self): ...
    @property
    def CaretIndex(self) -> int: ...
    @CaretIndex.setter
    def CaretIndex(self, value: int) -> None: ...
    @property
    def Font(self) -> Font: ...
    @Font.setter
    def Font(self, value: Font) -> None: ...
    @property
    def MaxLength(self) -> int: ...
    @MaxLength.setter
    def MaxLength(self, value: int) -> None: ...
    @property
    def PlaceholderText(self) -> str: ...
    @PlaceholderText.setter
    def PlaceholderText(self, value: str) -> None: ...
    @property
    def ReadOnly(self) -> bool: ...
    @ReadOnly.setter
    def ReadOnly(self, value: bool) -> None: ...
    @property
    def Selection(self) -> Range: ...
    @Selection.setter
    def Selection(self, value: Range) -> None: ...
    @property
    def ShowBorder(self) -> bool: ...
    @ShowBorder.setter
    def ShowBorder(self, value: bool) -> None: ...
    @property
    def Text(self) -> str: ...
    @Text.setter
    def Text(self, value: str) -> None: ...
    @property
    def TextColor(self) -> Color: ...
    @TextColor.setter
    def TextColor(self, value: Color) -> None: ...
    @property
    def ValidDirection(self) -> StepperValidDirections: ...
    @ValidDirection.setter
    def ValidDirection(self, value: StepperValidDirections) -> None: ...
    def SelectAll(self) -> None: ...
    @property
    def TextAlignment(self) -> TextAlignment: ...
    @TextAlignment.setter
    def TextAlignment(self, value: TextAlignment) -> None: ...
    @property
    def ShowStepper(self) -> bool: ...
    @ShowStepper.setter
    def ShowStepper(self, value: bool) -> None: ...
    @property
    def BackgroundColor(self) -> Color: ...
    @BackgroundColor.setter
    def BackgroundColor(self, value: Color) -> None: ...
    @property
    def AutoSelectMode(self) -> AutoSelectMode: ...
    @AutoSelectMode.setter
    def AutoSelectMode(self, value: AutoSelectMode) -> None: ...
    def AttachEvent(self, id: str) -> None: ...
