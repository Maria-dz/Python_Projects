import csv
import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inp', required=True)
    parser.add_argument('-o', '--out', required=True)
    return parser


add_col = ["our_data", "cid", "t", "idf", "idt", "idc", "idth", "idh"]

parser = create_parser()
namespace = parser.parse_args(sys.argv[1:])
input_file = namespace.inp
output_file = namespace.out
try:
    file = open(input_file, 'r', encoding='utf-8')
    wr = open(output_file, 'w',  encoding='utf-8')
    reader = csv.reader(file)
    csv.register_dialect('my_dialect', delimiter=',', quotechar='"')
    writer = csv.writer(wr, delimiter=",", lineterminator="\r")
    rows = []
    flag = 0
    fl = 0
    ans = ["False", "", "", "", "", "", "", ""]
    for row in reader:
        rows.append(row)
        writer.writerow(rows[0] + add_col)

    for elem in rows[1:]:
        for param in elem:
            index = elem.index(param)
            if ',' in param:
                elem[index] = '"{}"'.format(param)
        label = elem[19]
        if label.startswith("cid"):
            if label[3] == "=":
                fl = 1
            ans[0] = "True"
            ans[1] = label[3 + fl:24 + fl]
            label = label[25 + fl:]
            params = label.split('_')
            for word in params:
                if word in add_col:
                    flag = add_col.index(word)
                else:
                    ans[flag] = word
        writer.writerow(elem + ans)
        ans = ["False", "", "", "", "", "", "", ""]
    file.close()
    wr.close()
except IOError:
    print("Error in file names found!")
