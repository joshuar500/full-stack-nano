import os

def rename_files():
    # 1 get file names from a folder
    # r stands for raw path
    file_list = os.listdir(r"D:\workspace\Udacity\Course 1\Lesson 1\Prank")
    print(file_list)
    
    os.chdir(r"D:\workspace\Udacity\Course 1\Lesson 1\Prank")
    # 2 for each file, rename file
    for file_name in file_list:
        os.rename("athensssss.jpg", "austin.jpg")
        print("New file name: " + file_name)

rename_files()
