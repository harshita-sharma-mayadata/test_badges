#git push https://username:password@myrepository.biz/file.git --all
import os
import re



num_tests = str(sum(1 for line in open('TESTS.md')))
num_tests = '-'+num_tests+'-'


myfile =  open("README.md", "r") 
line = myfile.readlines()

match = re.sub(r'\-(.*)\-',num_tests,line[1])

line[1] = match 

myfile = open("README.md", "w")

myfile.writelines(line)
	
myfile.close()			 


cmd = "git add README.md"
cmd1 = "git commit -s -m {}".format("update")
cmd2 = "git push https://harshita-sharma-mayadata:mygithubpass%40123321@github.com/harshita-sharma-mayadata/test_badges.git HEAD:master"
os.system(cmd)
os.system(cmd1)
os.system(cmd2)
