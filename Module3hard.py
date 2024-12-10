###data_structure=[
    #[1,2,3],
    #{'a':4,'b':5},
    #(6,{'cube':7,'drum':8}),
    #"Hello",
    #((),[{(2,'Urban',('Urban2',35))}])
#]

def calculate_data_structure(data):
    total_sum=0
    if isinstance(data, int):
    total_sum += data
    elif isinstance(data, str):
    total_sum += len(data)
    #тут же теперь нужно по словарям и спискам пройтись, верно? но я ничего не нашла в лекциях этого и прошлого модуля про рекусивный вызов функции
    return total_sum

result=calculate_structure_sum(data_structure)
print(result)