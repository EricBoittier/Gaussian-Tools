from scipy.spatial import distance
import os

class ExtractGaussInfo:
    def __init__(self, filename):
        self.record = False
        self.filename = filename.split(".")[0]
        self.info = []
        self.output = ""
        self.lines = []
        with open(filename, "r") as f:
            lines = self.lines = f.readlines()
            self.lines.reverse()
            for line in lines:
                if line.__contains__("\\\\@"):
                    self.record = True
                if self.record:
                    self.info.append(line)
                if line.__contains__(" GradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGrad") or line.__contains__("Charge unit"):
                    break
            self.info.reverse()
            self.info = self.info[2:]
            for line in self.info:
                self.output += str(line).strip("\n")
            self.output.strip("\n")
            self.info = self.output.split("\\")
        self.atoms = self.getAtoms()

    def getInfo(self):
        return self.info

    def getLines(self):
        return self.lines

    def getNImag(self):
        for line in self.info:
            if line.startswith("NImag="):
                return int(line.split("=")[1])

    def getCalculation(self):
        for line in self.info:
            if line.startswith("#"):
                return str(line.split("#")[1])

    def getEnergy(self):
        for line in self.info:
            if line.startswith("HF"):
                return float(line.split("=")[1].replace(" ", ""))

    def getAtoms(self):
        count = 0
        atoms = {}
        for line in self.getInfo():
            if 6 > len(line.split(",")) > 3:
                count+=1
                atoms[int(count)] = line.split(",")
        return atoms

    def getDistance(self, atom1, atom2):
        a = []
        for point in self.atoms[atom1][1:]:
            a.append(float(point.replace(" ", "")))
        b = []
        for point in self.atoms[atom2][1:]:
            b.append(float(point.replace(" ", "")))
        return distance.euclidean(a,b)

    def getWiberg(self):
        self.lines.reverse()
        catch = False
        row = []
        wiberg = {}
        for line in self.lines:
            if line.__contains__("index matrix in the NAO basis"):
                catch = True
            if line.__contains__(" Wiberg bond index, Totals by atom: "):
                break
            if catch:
                if line.__contains__("Atom"):
                    row = line.split()[1:]
                if len(line.split()) > 1 and line.split()[0].__contains__("."):
                    atom = int(line.split()[0].strip("."))
                    l = line.split()[2:]
                    for enumerated in enumerate(l):
                        wiberg[atom, int(row[enumerated[0]])] = enumerated[1]

        return wiberg

    def makeXYZ(self):
        with open("{}.xyz".format(self.filename), "w") as file:
            file.write("{} \n \n".format(len(self.atoms)))
            for number, atom in self.atoms.items():
                print(atom)
                file.write("{}         {}       {}        {}\n".format(atom[0], atom[2].replace(" ",""), atom[3].replace(" ",""), atom[4].replace(" ","")))
            file.write("\n")



# print(ExtractGaussInfo("xyztest.out").getEnergy())
# for x in ExtractGaussInfo("xyztest.out").getInfo():
#     print(x)
# for x in ExtractGaussInfo("xyztest.out").getAtoms().items():
#     print(x)

for file in os.listdir("."):
    print(file)
    a = ExtractGaussInfo("NBOtest.out")
    a.makeXYZ()