if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    file = File(filename)
    print(file.get_pdbqt_files())
