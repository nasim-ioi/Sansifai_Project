import os
from multiprocessing import Pool

# a list to keep input file path and output file path
work = []

# converting videos's quality using FFMPEG 
def convert_quality(input_path, output_path):
    os.system("ffmpeg -i {input_path} -s 256*144 {output_path}".format(input_path = input_path, output_path = output_path))

# get folder directory
original_folder_directory = input("please enter your complete original folder directory in the correct style(like this : /home/nasim/Videos/clips) : ")

# walk on the all file from an unique directory
for file in os.listdir(original_folder_directory):
    if file.endswith(".mp4"):

        # define file path
        path = os.path.join(original_folder_directory, file)

        # find the parent directory of the original_folder_directory
        indx = 0

        for i in range(0, len(original_folder_directory)):
            if original_folder_directory[i] == '/':
                indx = i
        
        parent_folder_directory = ''

        for i in range(0, indx):
            parent_folder_directory += original_folder_directory[i]

        # define the final path of the converted file
        final_path = os.path.join(parent_folder_directory, 'converted_files')


        # make final folder to keep converted files in the current directory
        try:
            os.mkdir(final_path)
        except FileExistsError:
            pass
        
        # define output path
        output_path = os.path.join(final_path, file)
    
        # appending to the work list
        work.append([path, output_path])


def work_log(work_data):
    print(" Process %s waiting ________________________________________" % work_data[0])
    convert_quality(work_data[0], work_data[1])
    print(" Process %s Finished________________________________________." % work_data[0])


def pool_handler():
    # get number of process from user
    pool_num = int(input("please enter how many process do you want to run concurrently : "))
    p = Pool(pool_num)

    # map work list and work_log together
    p.map(work_log, work)

    # close the pool after it is done
    p.close()

# only run the programme if we are in the main process
if __name__ == '__main__':
    pool_handler()
