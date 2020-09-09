import os
import json
import shutil

def main():
    '''
    Main function
    '''

    f = open("config.json")
    d = json.load(f)
    project_name  = d["project_name"]
    project_dir = d["project_path"]

    project_path = os.path.join(project_dir, project_name)

    if (os.path.exists(project_path) == False):
        os.mkdir(project_path)

    print("[INFO] Project Folder created/exists")

    if os.listdir(project_path) != []: 
        print("[INFO] Project folder not empty, Exiting!")
        exit()

    src_path = os.path.join(project_path, "src")
    test_path = os.path.join(project_path, "test")
    thirdparty_path = os.path.join(project_path, "thirdparty")
    os.mkdir(src_path) 
    os.mkdir(test_path)
    os.mkdir(thirdparty_path)

    curr_path = os.getcwd()
    files_path = os.path.join(curr_path, "files")
    shutil.copy(os.path.join(files_path, "main.cpp" ), src_path)

    fin = open(os.path.join(files_path, "CmakeLists.txt"), 'r')
    fout = open(os.path.join(project_path, "CmakeLists.txt"), 'w')

    for line in fin:
	    fout.write(line.replace('###PROJECT_NAME###', project_name))
    fin.close()
    fout.close()
    print("[INFO] Cmake project created")

if __name__ == "__main__":
    main()
