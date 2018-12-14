import os
import sys

class ExtractScan:
    def __init__(self, filename):
        self.filename = filename
        self.lines = []
        self.stationarypoints = []
        self.xyzs = []
        self.count = 0

        with open(self.filename, "r") as file:
            self.lines = file.readlines()

        for enumerated in enumerate(self.lines):
            if enumerated[1].__contains__("-- Stationary point found."):
                for line in list(enumerate(self.lines))[enumerated[0]:0:-1]:
                    if line[1].__contains__("                         Standard orientation:"):
                        self.stationarypoints.append([line[0], enumerated[0], self.count])
                        break
                self.count += 1

        for points in self.stationarypoints:
            temp = []
            for line in self.lines[points[0]+5:points[1]]:
                if line.__contains__("-------------------------------------------------------------------"):
                    break
                temp.append(line)
            XYZ(temp, self.filename, points[2])

class XYZ:
    def __init__(self, line_array, filename, count):
        self.filename = filename
        self.line_array = line_array
        #                 atom name      x        y         z
        self.line_template = "{}         {}       {}        {}"


        with open("{}_extract_{}.xyz".format(filename[:-4], count), "w") as file:
            print("writing file: {}_extract_{}.xyz".format(filename[:-4], count))
            file.write(str(len(self.line_array)))
            file.write("\n")
            file.write("\n")
            for line in line_array:
                line_split = line.split()
                atom = line_split[1]
                file.write(self.line_template.format(getAtom(atom), line_split[3], line_split[4], line_split[5]))
                file.write("\n")


def getAtom(number):
    if number == "1":
        return "H"
    elif number == "6":
        return "C"
    elif number == "7":
        return "N"
    elif number == "8":
        return "O"
    elif number == "16":
        return "S"
    else:
        pass

#ExtractScan("/Users/ericboittier/computational_chemistry/QM/CyclobuteneRO/scans/Scans/Scans 1+2/Electro_cyclobutOpt_1CHO_HOpt_OMeOpt_FineIRC_63Opt_Scan34_1Scan45.out")

# os.chdir("/Users/ericboittier/computational_chemistry/QM/CyclobuteneRO/scans/Scans 2")
# for y in os.listdir("/Users/ericboittier/computational_chemistry/QM/CyclobuteneRO/scans/Scans 2"):
#     if y.__contains__(".out"):
#         ExtractScan(y)
#
# print(os.getcwd())
#
# for y in os.listdir("/Users/ericboittier/Desktop/lostscans/"):
#     print(y)
#     ExtractScan(y)

for out in os.listdir("/Users/ericboittier/full_structure_DIH/"):
    if out.__contains__(".out"):
        ExtractScan("/Users/ericboittier/full_structure_DIH/"+out)