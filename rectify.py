
import glob

file_list = glob.glob('img_data/*/*/*.txt')
print(file_list)
# def operation_change(file_name):
#     with open(file_name, 'r') as file :
#         filedata = file.read()
#         file.close()

#     # Replace the target string
#     filedata = filedata.replace('0.6666666666666667 0.6666666666666667 1 1', '0.3 0.3 1 1')

#     with open(file_name, 'w') as file:
#         file.write(filedata)
#         file.close()


# def main_f():
#     for i in file_list:
#         operation_change(i)


# if __name__ == '__main__':
#     main_f()