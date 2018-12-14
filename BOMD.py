from scipy.spatial import distance
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math


def calculate_distance(a, b):
    """

    :param a: vector a
    :param b: vector b
    :return:
    """
    dif1= a[0] - b[0]
    dif2=a[1] - b[1]
    dif3=a[2] - b[2]

    return math.sqrt(dif1*dif1+dif2*dif2+dif3*dif3)


import os


count = 0


path = "/Volumes/eric/Projects/scripts/BOMD/"



runs = os.listdir(path)

prod1 = 0
prod2 = 0

for run in runs:
    if run.__contains__(".out"):
        bond1 = []
        bond2 = []
        f = open(path+run, "r")
        lines = f.readlines()
        for number, line in enumerate(lines):
            if line.__contains__(" TRJ-TRJ-TRJ-TRJ-TRJ-TRJ-TRJ-TRJ-TRJ-TRJ-TRJ-TRJ-TRJ-TRJ-TRJ-TRJ-TRJ-TRJ") and lines[number+2].__contains__("   Input orientation: "):
                for l in lines[number+7:number+29]:
                    if l.startswith("      3"):
                        atom3 = [float(l.split()[2]), float(l.split()[3]), float(l.split()[4])]

                    if l.startswith("      5"):
                        atom5 = [float(l.split()[2]), float(l.split()[3]), float(l.split()[4])]

                    if l.startswith("      9"):
                        atom9 = [float(l.split()[2]), float(l.split()[3]), float(l.split()[4])]

                    if l.startswith("     18"):
                        atom18 = [float(l.split()[2]), float(l.split()[3]), float(l.split()[4])]

                bond1.append(calculate_distance(atom3, atom9))
                bond2.append(calculate_distance(atom5, atom18))




        plt.ylabel("C2 - C5'")
        plt.xlabel("C4 - C3'")



        if bond1[-1] < 2 and bond2[-1] > 2:
            plt.scatter(bond1[-1], bond2[-1], marker="o", color="b")
            plt.plot(bond1, bond2, color='b', alpha=0.1)
            prod1 +=1
        elif bond2[-1] < 2.5 and bond1[-1] > 2:
            plt.scatter(bond1[-1], bond2[-1], marker="o", color="r")
            plt.plot(bond1, bond2, color='r', alpha=0.1)
            prod2 +=1
        else:
            plt.scatter(bond1[-1], bond2[-1], marker="o", color="tab:gray")
            plt.plot(bond1, bond2, color='tab:gray', alpha=0.1)
        #plt.savefig("{}.pdf".format(run))


print("prod blue {}".format(prod1))
print("prod red {}".format(prod2))

plt.text(2, 2.2, "n={}".format(prod2))
plt.text(1.5, 3.4, "n={}".format(prod1))
plt.savefig("All Trajectories.pdf".format())


    #Axes3D.scatter(bond1, bond2)

    # plt.plot(bond1, label="atom3-atom5")
    # plt.plot(bond2, label="atom9-atom18")
    # plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    # plt.xlabel("Time step")
    # plt.ylabel("Bond distance (Angstrom)")
