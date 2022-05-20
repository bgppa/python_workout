'''
Practicing a bit with csv files.
'''
import csv

def passwd_to_csv(i_filename, o_filename):
    '''
    Open i_filename assuming a /etc/passwd format.
    Reading username and id, writing them in a csv formal into o_filename,
    using tab as separating value.
    '''
    try:
        with open(i_filename, 'r') as i_file:
            # using a csv reader with : as delimiter
            print(f"Opening {i_filename}", end = '')
            i_reader = csv.reader(i_file, delimiter = ':')

            with open(o_filename, 'w') as o_file:
                # using a csv writer using TAB as delimiter
                print(f"...writing to {o_filename}")
                o_writer = csv.writer(o_file, delimiter = '\t')

                for line_splitted in i_reader:
#                    print(line_splitted, flush = True)
                    # simple check to avoid empty lines and comment
                    if line_splitted and line_splitted[0][0] not in "#":
                        o_writer.writerow([line_splitted[0],line_splitted[2]])

    except FileNotFoundError:
        print(f"ERROR: unable to open {i_filename}")

    else:
        print(f"Success: {i_filename} -> {o_filename}")

    return 1
#---


if __name__ == '__main__':
    passwd_to_csv('passwd.txt', 'csv1.txt')
    passwd_to_csv('not_existing.txt', 'csv2.txt')
