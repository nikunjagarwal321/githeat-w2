import os
from plotly.offline import  plot, iplot
import plotly.graph_objs as go
import shutil


#Get size of a directory
def dir_size(curr_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(curr_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

#Get size of all sub-directories and files
def all_sub_size(parent_path):
    dir = os.listdir(parent_path)
    size = []
    i = 0
    for file in dir:
        curr_path = parent_path + "\\" + dir[i]
        if os.path.isdir(curr_path):
            size.append(dir_size(curr_path))
        else:
            size.append(os.path.getsize(curr_path))
        i +=1 
    trace = go.Pie(labels=dir, values=size)
    plot([trace], filename='pie_chart.html')
    print (dir)
    print (size)  


choice = 1
print ("Enter full path and directory name")
input_path = input()
all_sub_size(input_path)
while choice:
    print("Enter  \n0.To end \n1.To navigate to parent folder \n2.To navigate to child folder \n3.To remove a directory or file from the present directory")
    choice = int(input())
    if choice == 0:
        break
    elif choice == 1:
        input_path = os.path.dirname(input_path)
        all_sub_size(input_path)
    elif choice == 2:
        print("Enter name of child directory")
        child_dir = input()
        input_path = input_path + "\\" + child_dir
        all_sub_size(input_path)
    elif choice == 3:
        print("Enter filename with extension or sub-directory to be deleted")
        file_del = input()
        if os.path.isdir(input_path + "\\" + file_del):
            shutil.rmtree((input_path + "\\" + file_del))
        else:
            os.remove(input_path + "\\" + file_del) 
        all_sub_size(input_path)
    else:
        print("Wrong choice")



