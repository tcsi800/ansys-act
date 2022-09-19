if r"\\unifiles.uoa.auckland.ac.nz\myhome\Documents\ES344\project_files" not in sys.path:
  sys.path.append(r"\\unifiles.uoa.auckland.ac.nz\myhome\Documents\ES344\project_files")
    
import csv
from function_module import *

# Creates a 
with Model.CoordinateSystems.AddCoordinateSystem as c:
    c.Name = "AOA=5"
    c.AddTransformation(TransformationType.Rotation, CoordinateSystemAxisType.PositiveZAxis)
    c.SetTransformationValue(1, 5)
    
    
Model.Mesh.AddSizing
    