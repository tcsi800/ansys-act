import csv
import itertools as it
# from function_module import *

# Helper Functions
def parse_Q(q):
    vars = q.ToString().Split(' ')
    # print(vars[1])
    try:
        out = float(vars[0])
    except ValueError:
        out = vars[0]
    return float(vars[0])

def find_named_child(obj, name):
    '''
    returns the first child of {obj}
    with Name property given by {name}
    '''
    return filter(
        lambda x: x.Name==name,
        obj.Children
        )[0]

def find_named_prop(obj, name):
    return filter(
        lambda x: x.Name==name,
        obj.Properties
        )[0]
        
# function takes float -> quantity in [mm]
def Q_mm(x):
    return Quantity('%f [mm]' % x)
    
def Q_N(x):
    return Quantity('%f [N]' % x)

def Q_u(x, unit=None):
    if unit is None:
        return x
    return Quantity("%f [%s]" % (x, unit))    
    
# path writing data to
path = r'\\unifiles.uoa.auckland.ac.nz\myhome\Documents\ES344\small_test2\small_test.csv'
path1 = r'\\unifiles.uoa.auckland.ac.nz\myhome\Documents\ES344\small_test2\path2'
# name of data being exported
names = ["Spar Size", "Max Tot U", "Max Equiv Stress"]



# clear generated data
mesh = Model.Mesh
mesh.ClearGeneratedData()

Model.Mesh.ElementSize = Q_mm(50)
Model.Mesh.ElementOrder =  ElementOrder.Quadratic
# b_sizes = [Q_mm(x) for x in [6, 8, 10, 12]]
b_sizes = [Q_mm(x) for x in [10, 20, 30, 40, 50]]
# m_sizes = [Q_mm(x) for x in [60, 50, 40]]
# order = [ElementOrder.Linear, ElementOrder.Quadratic]
# params = [s for s in it.product(b_sizes, m_sizes) if s[0] < s[1]]
params = b_sizes


with open(path, 'w') as file:
    writer = csv.DictWriter(file, fieldnames=names)
    writer.writeheader()
    for b in params:
        mesh.ClearGeneratedData()
        
        # modify data
        # Model.Mesh.ElementSize = m
        find_named_child(Model.Mesh, "Body Sizing").ElementSize = b
        # Model.Mesh.ElementOrder = ordr
        
        Model.Solve()
        
        # collect solution data 
        umax = find_named_child(Model.Analyses[0].Solution, 'Total Deformation').Maximum
        smax = find_named_child(Model.Analyses[0].Solution, 'Equivalent Stress').Maximum
            
        # list of output variables
        out = [b, umax, smax]
        
        txt = path1 + '('+ b.ToString() + ').txt'
        find_named_child(Model.Analyses[0].Solution, 'Path Stress').ExportToTextFile(txt)
        
        values = [parse_Q(x) for x in out]
        writer.writerow({
            k:v for (k,v) in zip(names,values)
        })