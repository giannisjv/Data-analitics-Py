                            # creating folder sorted
def create_folder():                    # initiating the function without parameters
    import os                           # importing os library
    sorted = "sorted"                   # variable string "sorted"
    directory = os.getcwd()             # get current directory
    path = os.path.join(directory, sorted) # joining directory with sorted
    if(os.path.exists(path) == True):      # checking if dir is exists 
        print("directory exists!!")        # id yes print it and continue 
    else:                                  
        os.mkdir(path)                     # else make the dir
    return path                            # return the path

#print(create_folder())

                                #Finding all csv files in the directory
def find_files(file):                   # initiating the function with one parameter (the parameter is a string of file extension for example "csv"  ) 
    import glob                         # importing os and glob
    file_list = list()                  # initiating the list to use
    #path = os.getcwd()               # get the current directory to search in it
    #print(path)
    for files in glob.glob("*" + file):  # in the directory search every file (*) with file extension the second file is function parameter 
        if "sorted" not in files:        # if the word sorted is in the file name drop it and continue
            file_list.append(files)      # append full file name in the list as string
    return file_list                    # return the list

                              # splitting the string to add sorted in the name
def split_str(x):                       # initiating the function with one parameter (the parameter is a string of file)
    xsp = x.split(".")                  # splitting the string in "."
    #print(xsp)                         # printing so we have correct result.  The splitted result is storing in a list with 2 string variables [file_name, extension] 
    return xsp[0] + "sorted." + xsp[1]  # return the file with sorted. in between

                              # OS Version Checker
def os():                                # initiating the function with one parameter (the parameter is a string of the OS)         
    import platform                      # importing platform
    if(platform.system() == "Linux"):    # if platform is Linux return Linux
        return "Linux"
    elif(platform.system() == "Windows"): # else if platform is Windows return Windows
        return "Windows"
    else:
        return "Mac"                       # if platform is Mac return Mac
                                           # Linux and Mac are both Unix base Os's so
                                           # the directory system is the same "/" with 
                                           # forward slash

                                # Sorting function
def csv_sort(file_list_csv):            # initiating the function with one parameter (the parameter is the list of find_files function)
    import pandas as pd                 # importing pandas lib as pd                  #
    utf8 = "utf-8-sig"                  # initializing utf-8-sig. This is because utf-8 doesn't work with utf-8-BOM encoding 
    path = create_folder()


    for x in file_list_csv:             # for every name (file) in the list (of find_file func) 
        csvData = pd.read_csv(x, header=None, encoding=utf8) # read the data of the file, bypass headers, with encoding utf-8-sig

        """
        #unsorted data frame
        print("\nbefore sorting")       # just a informative print
        print(csvData)                  # printing the file untouched
        """
        
        #sorting data using first value
        csvData.sort_values(csvData.columns[0], axis=0, inplace=True) # sorting the list by the first column, sorting by rows, change position enabled
        """
        print("\nAfter sorting")        # just a informative print
        print(csvData)                  # printing the list sorted
        print(split_str(x))             # how the filename will become
        """
        if(os() == "Windows"):
            pathname = path + "\\" + split_str(x)
        else:
            pathname = path + "/" + split_str(x)
        csvData.to_csv(pathname, encoding=utf8, index=False, header=False) # write the data to (filename, encoding= utf-8-sig, bypass indexing, bypass header)

file_list = find_files("csv")   # filling a list with csv files

if not file_list:               # if the list is empty there must be no csv files in the directory
    print("\nΕπελεξε άλλο φάκελο\n")
else:       
    csv_sort(file_list)         # sort the files by first column

