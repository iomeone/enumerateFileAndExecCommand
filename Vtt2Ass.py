import os, subprocess, sys

# if len(sys.argv) != 3:
#     print('Must have 2 arguments!')
#     print('Correct usage is "python answer.py input_dir output_dir" ')
#     exit()

input_dir = "C:/Users/user/Desktop/pythontest/vtt"
output_dir ="C:/Users/user/Desktop/pythontest/ass" 

input_file_extension = ".vtt"

# cmd = 'currentframe'

# iterate over the contents of the directory
for f in os.listdir(input_dir):
    # index of last period in string
    fi = f.rfind('.')
    # separate filename from extension
    file_name = f[:fi]
    file_ext = f[fi:]
    # create args
    input_str = '%s' % (os.path.join(input_dir, f))  #'%s.ifd' % (os.path.join(input_dir, file_name))
    output_str =  '%s.ass' % (os.path.join(output_dir ,  file_name))
    cli_args = ['ffmpeg.exe', '-i', input_str, output_str]
    #call function
    if subprocess.call(cli_args, shell=True):
        print('An error has occurred with command "%s"' % ' '.join(cli_args))
