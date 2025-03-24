# ternary operations using if-else
signal = "Green"
result = "Move" if signal == "Green" else "Stop"
print(result) # output: Move

# ternary operations using tuple
signal = "Green"
result = ("Stop", "Move")[signal=="Green"]
print(result) # output: Move

# ternary operations using list
signal = "Green"
result = ["Stop", "Move"][signal == "Green"]
print(result) #output: Move

# ternary operations using dict
signal = "Green"
result = {"Green":"Move"}
output = result.get(signal, "Stop")
print(output)
