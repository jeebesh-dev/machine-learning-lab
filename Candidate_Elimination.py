data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

def candidate_elimination(data):
    s = data[0][:-1]   
    G = [['?' for _ in range(len(s))]]   

    for row in data:
        attributes = row[:-1]
        target = row[-1]

        if target == "Yes":  
            
            # Remove inconsistent hypotheses from G
            G = [h for h in G if all(h[j] == '?' or h[j] == attributes[j] for j in range(len(s)))]
            
            # Generalize S
            for i in range(len(s)):
                if attributes[i] != s[i]:
                    s[i] = '?'

        else:  # Negative example
            new_G = []
            for g in G:
                if all(g[j] == '?' or g[j] == attributes[j] for j in range(len(attributes))):
                    for j in range(len(attributes)):
                        if s[j] != attributes[j] and s[j] != '?':
                            new_hypothesis = g.copy()
                            new_hypothesis[j] = s[j]
                            new_G.append(new_hypothesis)
                else:
                    new_G.append(g)
            G = new_G

    return s, G

s_final, g_final = candidate_elimination(data)
print("Specific Boundary(S):", s_final)
print("General Boundary(G):", g_final)