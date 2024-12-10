def calculate_structure_sum(data_structure):
    if isinstance(data_structure, (int,float)):
       return data_structure
    if isinstance(data_structure, (str)):
       return len(data_structure)
    if len(data_structure)==0:
       return 0
    if isinstance(data_structure,(list,tuple,set)):
        a=calculate_structure_sum(list(data_structure)[0])
        b=calculate_structure_sum(list(data_structure)[1:])
        return a+b
    elif isinstance(data_structure,dict):
        a=calculate_structure_sum(list(data_structure.keys()))
        b=calculate_structure_sum(list(data_structure.values()))
        return a+b
    return 0

data_structure=[
    [1,2,3],
    {'a':4,'b':5},
    (6,{'cube':7,'drum':8}),
    "Hello",
    ((),[{(2,'Urban',('Urban2',35))}])
]
result=calculate_structure_sum(data_structure)
print(result)