from src.Bugs import Bug
from src.KubernetesBugs import KubernetesBug

if __name__ == "__main__":
    bug1 = KubernetesBug("./bugs/bug-1", False)
    bug1.bugDefine()