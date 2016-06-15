from sys import argv
script, user_name=argv
prompt='/'
print"hi %s, I'm the %s script." %(user_name, script)
print" question"
print"do u like me %s" %user_name
like=raw_input(prompt)
print"where do you stay %s" %user_name
stay=raw_input(prompt)
print" which computer you use"
computer=raw_input(prompt)
print""""
alright, so you said %r about liking me 
you stay in %r and you use %r computer""" %(like,stay,computer)
