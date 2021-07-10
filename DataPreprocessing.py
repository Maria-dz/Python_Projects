import csv
add_col = ["our_data", "cid", "t", "idf", "idt", "idc", "idth", "idh"]
print("Path to input file:")
input_file = input()
print("Path to output file:")
output_file = input()
with open(input_file, encoding='utf-8') as file:
    reader = csv.reader(file)
    with open(output_file, 'w',  encoding='utf-8') as wr:
        csv.register_dialect('my_dialect', delimiter=',', quotechar='"')
        writer = csv.writer(wr, delimiter=",", lineterminator="\r")
        rows = []
        flag = 0
        fl = 0
        ans = ["False", "", "", "", "", "", "", ""]
        for row in reader:
            rows.append(row)
        writer.writerow(rows[0]+add_col)

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
                ans[1] = label[3+fl:24+fl]
                label = label[25+fl:]
                params = label.split('_')
                for word in params:
                    if word in add_col:
                        flag = add_col.index(word)
                    else:
                        ans[flag] = word
            writer.writerow(elem + ans)
            ans = ["False",  "", "", "", "", "", "", ""]

