import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

import System 
clr.AddReference("System")
from System.Collections.Generic import List as XS

doc = DocumentManager.Instance.CurrentDBDocument

collector = FilteredElementCollector(doc)
importeddwgs = collector.OfClass(ImportInstance).ToElements()

linked, imported = XS[ElementId](), XS[ElementId]()

for i in importeddwgs:
	if item.IsLinked:
		linked.Add(i.Id)
	else:
		imported.Add(i.Id)

TransactionManager.Instance.EnsureInTransaction(doc)

doc.Delete(linked)

doc.Delete(imported)
	
TransactionManager.Instance.TransactionTaskDone()
doc.Regenerate()
