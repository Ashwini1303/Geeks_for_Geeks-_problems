def gfg(S):
    S_lower = S.lower()
    if S_lower.startswith("gfg") and S_lower.endswith("gfg"):
        print("Yes")
    else:
        print("No")

S1 = "gFgabcdEGfG"
gfg(S1) 
S2 = "GgfhTnagfg"
gfg(S2)  
