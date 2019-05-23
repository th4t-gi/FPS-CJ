import json, os, re, subprocess

#finds training packets
root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
tp = subprocess.check_output("find {} -name Training\ packets  -type d -maxdepth 1".format(root.replace(" ", "\ ")),shell=True,stderr=subprocess.STDOUT)
tp = "".join(tp.rsplit(root)).replace("\n", "")

#Finds individual packets
home_dir = [root, tp]
cwd = "".join(home_dir)
packet_search = re.compile(r"[A-Z][A-Z]\-\d\d\-[JMS][M\d]\d\d\-[P1|P2|Q|S|I]")
packets = filter(packet_search.match, os.listdir(cwd.replace("\\", "")))

#finds data file
data = re.compile(r"data\-\d\d\d?\.json")
packet_data = [[i, j] for i in packets for j in filter(data.match, os.listdir((cwd + "/" + i).replace("\\", "")))]

for i in packet_data:
    print i
    cwfile = cwd.replace("\\", "") + "/" + i[0] + "/" + i[1]
    datafile = open(cwfile).read()

    filepaths = re.findall(r"\".+?\-filepath\": \"\"", datafile)
    for j in filepaths:
        file_dict = {"data": i[1], "future-scene": "fuzzy.txt", "graphics": "graphics.png"}
        for k in file_dict.keys():
            if k in j:
                data_sub = re.compile(r"\"%s\-filepath\": \"\"" % k)
                replaced = j.replace("\"\"", "\"" + "/".join([tp, i[0], file_dict[k]]) + "\"")
                datafile = data_sub.sub(replaced, datafile)

    with open(cwfile, 'w') as file:
        file.write(datafile)
