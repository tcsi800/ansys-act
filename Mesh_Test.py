import csv
from function_module import *

# name of data being exported
names = ["Elem Size", "Max Tot U", "Max Equiv Stress"]



# clear generated data
mesh = Model.Mesh
mesh.ClearGeneratedData()



Model.Mesh.ElementOrder = ElementOrder.Quadratic
Model.Mesh.ElementSize = Quantity('50 [mm]')

sizes = [Q_mm(x) for x in [60, 50, 40, 30]]



with open(r'\\unifiles.uoa.auckland.ac.nz\myhome\Documents\ES344\singular_sol.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=names)
    writer.writeheader()
    for s in sizes:
        mesh.ClearGeneratedData()
        Model.Mesh.Children[0].ElementSize = s
        Model.Solve()
        umax = find_named_child(Model.Analyses[0].Solution, 'Total Deformation').Maximum
        smax = find_named_child(Model.Analyses[0].Solution, 'Equivalent Stress').Maximum
        umax = filter(lambda x: x.Name=='Total Deformation',Model.Analyses[0].Solution.Children)[0].Maximum
        smax = filter(lambda x: x.Name=='Equivalent Stress',Model.Analyses[0].Solution.Children)[0].Maximum
        values = [parse_Q(x) for x in[s, umax, smax]]
        writer.writerow({
            k:v for (k,v) in zip(names,values)
        })
        
        
        
        

    