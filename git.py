#git push https://username:password@myrepository.biz/file.git --all
import os
with open("TEST.md", "a") as myfile:
    myfile.write("update text")


cmd = "git add README.md"
cmd1 = "git commit -s -m {}".format("update")
cmd2 = "git push https://harshita-sharma-mayadata:mygithubpass%40123321@github.com/harshita-sharma-mayadata/test_badges.git HEAD:master"
os.system(cmd)
os.system(cmd1)
os.system(cmd2)
