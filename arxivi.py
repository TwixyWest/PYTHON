import zipfile

class Arhive:
    def __init__(self, path, description):
        self.path = path
        self.description = description
        self.password = None
    def getInfo(self):
        print(f"Path: {self.path}\nDesc: {self.description}\nPassword: {self.password}")

class Bruteforce:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def hack(self, archive):
            zip_file = zipfile.ZipFile(archive)
            password = None
            f = open(self.dictionary, "r")
            for line in f.readlines():
                password = line.strip("\n")
                try:
                    zip_file.extractall(pwd=password.encode())
                    print("---------------------")
                    print(f"Result: {password}")
                    f.close()
                    return (True, password)
                except:
                    print(password)
                    f.close()
            f.close()
            return(False, None)

class Library:
    def __init__(self, bruteforce):
        self.bruteforce = bruteforce
        self.archives = []

    def showarhives(self):
            for archive in self.archives:
                archive.getInfo()
                print("")

    def hackall(self):
        for archive in self.archives:
            if archive.password == None:
                res = self.bruteforce.hack(archive.path)
                if res[0] == True:
                    archive.password = res[1]


def main():
    library = Library(Bruteforce("dictionary.txt"))
    library.archives.append(Arhive("test.zip", "IT-Step"))
    library.showarhives()
    library.hackall()
    library.showarhives()

if __name__ == '__main__':
    main()
