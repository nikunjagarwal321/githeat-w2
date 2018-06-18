import os
from plotly.offline import  plot, iplot
import plotly.graph_objs as go
import shutil

output_dictionary = {}
#Get size of a directory
def get_dir_size(curr_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(curr_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

#Get size of all sub-directories and files
def get_all_sub_size(parent_path):
    i = 0
    dir = os.listdir(parent_path)
    size = []
   
    for file in dir:
        curr_path = os.path.join(parent_path, file)
        if os.path.isdir(curr_path):
            temp_size = get_dir_size(curr_path)
            size.append(temp_size)
        else:
            temp_size = os.path.getsize(curr_path)
            size.append(temp_size)
        output_dictionary[i] = file
        i = i + 1
    plot_pie_chart(dir,size)

#Plot the chart
def plot_pie_chart(dir,size):   
    trace = go.Pie(labels=dir, values=size)
    plot([trace], filename='pie_chart.html')
    i = 0
    for file in dir:
        print (str(i) + "." + (output_dictionary[i]) + " - " + str(size[i]) +" bytes")
        i = i + 1


def main():
    choice = 1
    print ("Enter full path and directory name")
    input_path = input()
    if input_path =='.':
        input_path = os.path.realpath('.')
    get_all_sub_size(input_path)
    while choice:
        print("Enter  \n0.To end \n1.To navigate to parent folder \n2.To navigate to child folder \n3.To remove a directory or file from the present directory")
        choice = int(input())
        if choice == 0:
            break
        elif choice == 1:
            input_path = os.path.dirname(input_path)
            get_all_sub_size(input_path)
        elif choice == 2:
            print("Enter index of child directory")
            child_dir_key = int(input())
            child_dir = output_dictionary[child_dir_key]
            input_path = os.path.join(input_path, child_dir)
            get_all_sub_size(input_path)
        elif choice == 3:
            print("Enter index of filename or sub-directory to be deleted")
            file_del_key = int(input())
            file_del = output_dictionary[file_del_key]
            if os.path.isdir(os.path.join(input_path, file_del)):
                shutil.rmtree(os.path.join(input_path, file_del))
            else:
                os.remove(os.path.join(input_path, file_del))
            get_all_sub_size(input_path)
        else:
            print("Wrong choice")

if __name__== "__main__":
    main()


