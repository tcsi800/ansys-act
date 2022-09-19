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
    