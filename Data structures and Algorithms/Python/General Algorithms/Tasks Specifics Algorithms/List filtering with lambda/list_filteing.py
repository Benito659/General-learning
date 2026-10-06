def filters_numbers_1(numbers,function) :
    return [x for x in numbers if function(x)]

def filters_numbers_2(numbers, function) :
    return list(filter(numbers, function))

filters_numbers_1([1,2,3,4,5,6], lambda x: x % 2 == 0)
filters_numbers_2([1,2,3,4,5,6], lambda x: x % 2 == 0)