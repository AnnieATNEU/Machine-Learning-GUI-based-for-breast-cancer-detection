
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure

import pandas as pd 


##Class/ Modification made for selecting only folders but also will show what it contains
class DirProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, fsModel):
        super().__init__()
        self.fsModel = fsModel
        self.setSourceModel(fsModel)

    def lessThan(self, left, right):
        # QFileSystemModel populates its entries with some delay, which results 
        # in the proxy model not able to do the proper sorting (usually showing 
        # directories first) since the proxy does not always "catch up" with the 
        # source sorting; so, this has to be manually overridden by 
        # force-checking the entry type of the index.
        leftIsDir = self.fsModel.fileInfo(left).isDir()
        if leftIsDir != self.fsModel.fileInfo(right).isDir():
            return leftIsDir
        return super().lessThan(left, right)

    def flags(self, index):
        flags = super().flags(index)
        # map the index to the source and check if it's a directory or not
        if not self.fsModel.fileInfo(self.mapToSource(index)).isDir():
            # if it is a directory, remove the enabled flag
            flags &= ~QtCore.Qt.ItemIsEnabled
        return flags

#model for the tableView
class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self,parent=None, dpi = 120):
        fig = Figure(dpi = dpi)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas,self).__init__(fig)
        fig.tight_layout()

class PandasModel(QtCore.QAbstractTableModel): 
    def __init__(self, df = pd.DataFrame(), parent=None): 
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df.copy()

    def toDataFrame(self):
        return self._df.copy()

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()
        elif orientation == QtCore.Qt.Vertical:
            try:
                # return self.df.index.tolist()
                return self._df.index.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if not index.isValid():
            return QtCore.QVariant()

        return QtCore.QVariant(str(self._df.iloc[index.row(), index.column()]))

    def setData(self, index, value, role):
        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            # PyQt5 gets a QVariant
            value = value.toPyObject()
        else:
            # PySide gets an unicode
            dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.index)

    def columnCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.columns)

    def sort(self, column, order):
        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(colname, ascending= order == QtCore.Qt.AscendingOrder, inplace=True)
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()

#=============================================================================


