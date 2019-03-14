#git push https://username:password@myrepository.biz/file.git --all
import os
with open("README.md", "a") as myfile:
    myfile.write("update text")


cmd = "git add README.md"
cmd1 = "git commit -s -m {}".format("update")
cmd2 = "git push origin"
os.system(cmd)
os.system(cmd1)
os.system(cmd2)
