data = [["Sunny","Warm","Normal","Strong","Warm","Same","Yes"],
        ["Sunny","Warm","High","Strong","Warm","Same","Yes"],
        ["Rainy","Cold","High","Strong","Warm","Change","No"],
        ["Sunny","Warm","High","Strong","Cool","Change","Yes"]]

def find_s(data):
    h = None
    
    for row in data:
        if row[-1] == "Yes":
            x = row[:-1]
            
            if h is None:
                h = x
            else:
                for i in range(len(h)):
                    if h[i] == x[i]:
                        pass
                    else:
                        h[i] = "?"
    
    return h

hypothesis = find_s(data)
print("Hypothesis:", hypothesis)                   
