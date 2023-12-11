import shutil, os


def main():
    # copy a file
    shutil.copy('data.txt', 'data_copy.txt')

    # copy a file and rename it
    # you will have to have data.txt in the same directory as this file
    shutil.copy('data.txt', 'data_copy2.txt')

    # copy a directory
    shutil.copytree('data', 'data_copy')

    # move a file
    shutil.move('data.txt', 'data_copy/data.txt')

    # move a directory
    shutil.move('data', 'data_copy/data')

    # delete a file
    shutil.rmtree('data_copy')
    os.remove('data_copy.txt')

    # delete a directory
    os.rmdir('data_copy')

if  __name__ == '__main__':
    main()