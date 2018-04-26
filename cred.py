'''
Jen Yu
Softdev pd7
2018-04-26
K#15: Do You Even List?
'''

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
	u = uc_count(p)
	n = n_count(p)
	a = a_count(p)
	score = 10
	r = " \n"
	if len(p) < 6: 
		score -= 5
		r += "Less than 6 characters: too short!\n"
		if n < 2 or a < 2: 
			score -= 3
			r += "Not enough numbers or alphanumerical characters!\n"
			if u > 2:
				return "Score: " + str(score) + r
			else:
				return "Score: " + str(score) + r + "Not enough capitalization!\n"
		else: 
			if u < 2:
				return "Score: " + str(score) + r + "Not enough capitalization!\n"
			return "Score: " + str(score) + r 
	else:
		if u < len(p)/2 - n - a:
			score -= 3
			r += "Need a healthy mixture of capitalization.\n"
			if n < 2 or a < 2: 
				score -= 2
				return "Score: " + str(score) + r + "Not enough numbers or alphanumerical characters!\n"
			else: 
				return "Score: " + str(score) + r
		else:
			if n < 2 or a < 2: 
				score -= 2
				return "Score: " + str(score) + r + "Not enough numbers or alphanumerical characters!\n"
			else: 
				return "Score: " + str(score) + r

print pass_check("hello") 
print pass_check("1Wwerwer!")
print pass_check("!1WeRe")
