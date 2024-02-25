def compute_length(input_data):
    
    if isinstance(input_data, list) or isinstance(input_data, str):
        length = 0
        
        for _ in input_data:
            length += 1
        return length
    else:
        return "Input should be either string or list"
    

print(compute_length([1, 2, 3, 4, 5]))

print(compute_length("hellooooooooooooooooooooooooooooooooooooo"))