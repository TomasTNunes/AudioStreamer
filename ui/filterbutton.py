from PySide6.QtWidgets import QPushButton

class BaseFilterButton(QPushButton):
     # Class Variables (Global)
    selectedButtons = {}  # Class variable to track the currently selected button

    def __init__(self, parent=None):
        super().__init__(parent)
        # Connect button click signal to method
        self.clicked.connect(self._buttonClick)
    
    def _buttonClick(self):
        if self.isChecked():
            groupKey = self._groupKey
            if BaseFilterButton.selectedButtons.get(groupKey) and BaseFilterButton.selectedButtons[groupKey] != self:
                BaseFilterButton.selectedButtons[groupKey].setChecked(False)  # Deselect the currently selected widget
            # Check this widget
            BaseFilterButton.selectedButtons[groupKey] = self
    

# Subclass for Search Filter Buttons
class SearchFilterButton(BaseFilterButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._groupKey = "search"
        # Initialize "all" as initial selected Search Filter Button
        if self.text() == 'all':
            BaseFilterButton.selectedButtons[self._groupKey] = self
        # Connect button click signal to method
        self.clicked.connect(self._buttonClick2)
    
    def _buttonClick2(self):
        if not self.isChecked():
            self.setChecked(True)


# Subclass for Library Filter Buttons
class LibraryFilterButton(BaseFilterButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._groupKey = "library"