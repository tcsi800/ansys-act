# Helper Functions
def parse_Q(q):
    vars = q.ToString().Split(' ')
    print(vars[1])
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
    
def Q_u(x, unit):
    if unit is None:
        return x
    return Quantity("%f [%s]" % (x, unit))

Pressure = Model.Analyses[0].AddPressure()
Pressure.Name = "Lift/Drag"

Fx = Q_N(30 * 5)
Fy = Q_N(1300 * 5)

wing_underside = find_named_child(Model.NamedSelections, "Wing_Underside")
A = find_named_prop(wing_underside, "AreaOfFaces").InternalValue

Px = Fx / Q_u(A, "mm^2")
Py = Fy / Q_u(A, "mm^2")

Pressure.DefineBy =  LoadDefineBy.Components
Pressure.CoordinateSystem = find_named_child(
    Model.CoordinateSystems, "AOA=5"
    )
Pressure.Location = wing_underside    
Pressure.XComponent.Output.DiscreteValues = [Px]
Pressure.YComponent.Output.DiscreteValues = [Py]



# Pressure.