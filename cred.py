UC = "QWERTYUIOPASDFGHJKLZXCVBNM"
N = "1234567890"
A = ".?!&#,;:-_*"

def uc_count(p):
    vals = [1 for x in p if x in UC]
    return len(vals)

def n_count(p):
    vals = [1 for x in p if x in N]
    return len(vals)

def a_count(p):
    vals = [1 for x in p if x in A]
    return len(vals)

def pass_check(p):
    if (uc_count(p) >= 1) and (n_count(p) > 0) and (a_count(p) > 0):
        return "good password"
    #print uc_count(p)
    #print n_count(p)
    return "bad password"

print pass_check("hello")
print pass_check("1Wwerwer!")
print pass_check("!1WeRe")
