from typing import Tuple, Set, Iterable, List

class GH_CssProperty:
    def __init__(self, property : str): ...
    def __init__(self, property : str, value : str): ...
    def __init__(self, property : str, values : Iterable[str]): ...
    @property
    def Name (self) -> str: ...
    @property
    def ValueCount (self) -> int: ...
    @property
    def Value (self, index : int) -> str: ...
    @property
    def Values (self) -> ReadOnlyCollection: ...
    def AddValue (self, value : str) -> None: ...
    def AddValues (self, values : Iterable[str]) -> None: ...
    def FormatCss (self, indent : int) -> str: ...
    def CompareTo (self, other : GH_CssProperty) -> int: ...
class GH_CssStyle:
    def __init__(self): ...
    def __init__(self, selector : str): ...
    def __init__(self, selector : str, property : GH_CssProperty): ...
    def __init__(self, selector : str, properties : Iterable[GH_CssProperty]): ...
    @property
    def Selector (self) -> str: ...
    @Selector.setter
    def Selector (self, Value : str) -> None: ...
    @property
    def Properties (self) -> ReadOnlyCollection: ...
    @property
    def Comments (self) -> ReadOnlyCollection: ...
    @property
    def IsPluralSelector (self) -> bool: ...
    @property
    def IsClassSelector (self) -> bool: ...
    @property
    def IsIdSelector (self) -> bool: ...
    def AddProperty (self, property : GH_CssProperty) -> None: ...
    def AddProperty (self, name : str, value : str) -> None: ...
    def AddComment (self, comment : str) -> None: ...
    def FormatCss (self, indent : int) -> str: ...
    def CompareTo (self, other : GH_CssStyle) -> int: ...
class GH_CssStyleSheet:
    def __init__(self): ...
    @property
    def Styles (self) -> ReadOnlyCollection: ...
    @property
    def Links (self) -> ReadOnlyCollection: ...
    def IsStyleDefined (self, style : GH_CssStyle) -> bool: ...
    def AddStyle (self, styles : Set(GH_CssStyle)) -> None: ...
    def FormatCss (self, indent : int) -> str: ...
class GH_CssConstants:
    def __init__(self): ...
    @property
    def ColourBackground (self) -> Color: ...
    @ColourBackground.setter
    def ColourBackground (self, Value : Color) -> None: ...
    @property
    def ColourForeground (self) -> Color: ...
    @ColourForeground.setter
    def ColourForeground (self, Value : Color) -> None: ...
    @property
    def ColourFakeFaint (self) -> Color: ...
    @ColourFakeFaint.setter
    def ColourFakeFaint (self, Value : Color) -> None: ...
    @property
    def ColourChapterBackground (self) -> Color: ...
    @ColourChapterBackground.setter
    def ColourChapterBackground (self, Value : Color) -> None: ...
    @property
    def ColourSectionBackground (self) -> Color: ...
    @ColourSectionBackground.setter
    def ColourSectionBackground (self, Value : Color) -> None: ...
    @property
    def Default (self) -> GH_CssStyle: ...
    @property
    def Text (self) -> GH_CssStyle: ...
    @property
    def TextMonospace (self) -> GH_CssStyle: ...
    @property
    def TextFaint (self) -> GH_CssStyle: ...
    @property
    def TextFaintCheat (self) -> GH_CssStyle: ...
    @property
    def TextChapter (self) -> GH_CssStyle: ...
    @property
    def TextSection (self) -> GH_CssStyle: ...
    @property
    def TextParagraph (self) -> GH_CssStyle: ...
    @property
    def BlockContent (self) -> GH_CssStyle: ...
    @property
    def BlockChapter (self) -> GH_CssStyle: ...
    @property
    def BlockSection (self) -> GH_CssStyle: ...
    @property
    def BlockParagraph (self) -> GH_CssStyle: ...
    @property
    def BlockSeparator (self) -> GH_CssStyle: ...
    @property
    def BlockTight (self) -> GH_CssStyle: ...
    @property
    def BlockListTight (self) -> GH_CssStyle: ...
class GH_HtmlTextProperties:
    None = 0
    Strong = 1
    Emphasis = 2
    SuperScript = 4
    SubScript = 8
    Code = 16
class GH_HtmlListType:
    None = 0
    Unordered = 1
    Ordered = 2
class GH_HtmlWriter:
    def __init__(self): ...
    def __init__(self, cssStyles : Set(GH_CssStyle)): ...
    @property
    def Title (self) -> str: ...
    @Title.setter
    def Title (self, Value : str) -> None: ...
    def ToString (self) -> str: ...
    @property
    def CssStyleSheet (self) -> GH_CssStyleSheet: ...
    def ComposeHTMLDocument (self, cssBodyStyles : Set(GH_CssStyle)) -> str: ...
    def ComposeHTMLDocument (self, cssBodyStyles : Set(str)) -> str: ...
    def WriteComment (self, comment : str) -> None: ...
    def WriteLineBreak (self) -> None: ...
    def WriteHorizontalRule (self) -> None: ...
    def WriteHorizontalRule (self, cssClasses : Set(str)) -> None: ...
    def WriteHorizontalRule (self, cssClasses : Set(GH_CssStyle)) -> None: ...
    def WriteText (self, text : str) -> None: ...
    def WriteText (self, text : str, properties : GH_HtmlTextProperties) -> None: ...
    def WriteText (self, text : str, cssClasses : Set(str)) -> None: ...
    def WriteText (self, text : str, cssClasses : Set(GH_CssStyle)) -> None: ...
    def WriteLink (self, target : str, name : str) -> None: ...
    def WriteLink (self, target : str, name : str, cssClasses : Set(str)) -> None: ...
    def WriteLink (self, target : str, name : str, cssClasses : Set(GH_CssStyle)) -> None: ...
    def WriteDivStart (self) -> None: ...
    def WriteDivStart (self, cssClasses : Set(str)) -> None: ...
    def WriteDivStart (self, cssClasses : Set(GH_CssStyle)) -> None: ...
    def WriteDivEnd (self) -> None: ...
    def WriteHorizontalGradient (self, top : Color, bottom : Color, steps : int, stepHeight : int) -> None: ...
    def WriteBlankSpace (self, height : int) -> None: ...
    def WritePreStart (self) -> None: ...
    def WritePreStart (self, cssClasses : Set(str)) -> None: ...
    def WritePreStart (self, cssClasses : Set(GH_CssStyle)) -> None: ...
    def WritePreEnd (self) -> None: ...
    def WriteSpanStart (self) -> None: ...
    def WriteSpanStart (self, cssClasses : Set(str)) -> None: ...
    def WriteSpanStart (self, cssClasses : Set(GH_CssStyle)) -> None: ...
    def WriteSpanEnd (self) -> None: ...
    def WriteUnorderedListStart (self) -> None: ...
    def WriteUnorderedListStart (self, cssClasses : Set(str)) -> None: ...
    def WriteUnorderedListStart (self, cssClasses : Set(GH_CssStyle)) -> None: ...
    def WriteOrderedListStart (self, start : int) -> None: ...
    def WriteOrderedListStart (self, start : int, cssClasses : Set(str)) -> None: ...
    def WriteOrderedListStart (self, start : int, cssClasses : Set(GH_CssStyle)) -> None: ...
    def WriteListEnd (self) -> None: ...
    def WriteListItemStart (self) -> None: ...
    def WriteListItemStart (self, cssClasses : Set(str)) -> None: ...
    def WriteListItemStart (self, cssClasses : Set(GH_CssStyle)) -> None: ...
    def WriteListItemEnd (self) -> None: ...
    def WriteListItem (self, itemContent : str) -> None: ...
    def WriteListItem (self, itemContent : str, cssClasses : Set(str)) -> None: ...
    def WriteListItem (self, itemContent : str, cssClasses : Set(GH_CssStyle)) -> None: ...
class GH_HtmlFormatterPalette:
    Black = 0
    Gray = 1
    White = 2
    Red = 3
    Green = 4
    Blue = 5
    Yellow = 6
    Cyan = 7
    Magenta = 8
class GH_HtmlRemark:
    def __init__(self): ...
class GH_HtmlTableRow:
    def __init__(self, n_Cells : int): ...
    @property
    def BackColor (self) -> Color: ...
    @BackColor.setter
    def BackColor (self, Value : Color) -> None: ...
    @property
    def ForeColor (self) -> Color: ...
    @ForeColor.setter
    def ForeColor (self, Value : Color) -> None: ...
    @property
    def Header (self) -> bool: ...
    @Header.setter
    def Header (self, Value : bool) -> None: ...
    @property
    def Italic (self) -> bool: ...
    @Italic.setter
    def Italic (self, Value : bool) -> None: ...
    @property
    def Bold (self) -> bool: ...
    @Bold.setter
    def Bold (self, Value : bool) -> None: ...
    @property
    def Size (self) -> int: ...
    @Size.setter
    def Size (self, Value : int) -> None: ...
    @property
    def Content (self, cell_index : int) -> str: ...
    @Content.setter
    def Content (self, cell_index : int, Value : str) -> None: ...
    @property
    def Width (self, index : int) -> int: ...
    @Width.setter
    def Width (self, index : int, Value : int) -> None: ...
    def FormatHtml (self) -> str: ...
class GH_HtmlTable:
    def __init__(self): ...
    def __init__(self, rows : int, columns : int, FirstRowIsHeader : bool): ...
    @property
    def Row (self, index : int) -> GH_HtmlTableRow: ...
    @Row.setter
    def Row (self, index : int, Value : GH_HtmlTableRow) -> None: ...
    @property
    def Content (self, row : int, column : int) -> str: ...
    @Content.setter
    def Content (self, row : int, column : int, Value : str) -> None: ...
    @property
    def ColumnWidth (self, index : int) -> int: ...
    @ColumnWidth.setter
    def ColumnWidth (self, index : int, Value : int) -> None: ...
    def SetAllTextSizes (self, nSize : int) -> None: ...
    @property
    def Border (self) -> int: ...
    @Border.setter
    def Border (self, Value : int) -> None: ...
    @property
    def Padding (self) -> int: ...
    @Padding.setter
    def Padding (self, Value : int) -> None: ...
    @property
    def Width (self) -> int: ...
    @Width.setter
    def Width (self, Value : int) -> None: ...
    def FormatHtml (self) -> str: ...
class GH_HtmlFormatter:
    def __init__(self): ...
    def __init__(self, nSource : IGH_InstanceDescription): ...
    def __init__(self, nSource : IGH_InstanceDescription, nTitle : str): ...
    def __init__(self, nSource : IGH_InstanceDescription, nTitle : str, nDescription : str): ...
    @property
    def Title (self) -> str: ...
    @Title.setter
    def Title (self, Value : str) -> None: ...
    @property
    def Description (self) -> str: ...
    @Description.setter
    def Description (self, Value : str) -> None: ...
    @property
    def Remarks (self) -> List: ...
    @property
    def WebPageURI (self) -> str: ...
    @WebPageURI.setter
    def WebPageURI (self, Value : str) -> None: ...
    @property
    def ContactURI (self) -> str: ...
    @ContactURI.setter
    def ContactURI (self, Value : str) -> None: ...
    def AddRemark (self, text : str, forecolour : GH_HtmlFormatterPalette, backcolour : GH_HtmlFormatterPalette) -> None: ...
    def ReplaceSpecialCharCodes (source : str) -> str: ...
    def ReplaceBoxDrawingCodes (source : str) -> str: ...
    def HtmlFormat (self) -> str: ...
    def HtmlPaletteTag (palette : GH_HtmlFormatterPalette) -> str: ...
class GH_HtmlHelpPopup:
    def __init__(self): ...
    def SetLocation (self, pt : Point) -> None: ...
    @property
    def RegisteredForms () -> List: ...
    def CloseAllPopupDialogs () -> None: ...
    @property
    def BrowserControl (self) -> WebBrowser: ...
    def LoadObject (self, obj : GH_DocumentObject) -> bool: ...
    def LoadHTML (self, syntax : str) -> None: ...
    def LoadHTML (self, syntax : GH_HtmlFormatter) -> None: ...
    def LoadRemoteHTML (self, uri : str) -> None: ...
