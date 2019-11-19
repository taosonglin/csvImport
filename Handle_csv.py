from tools import *
"""
create by taosonglin on 2019/11/15
to make import easier
"""
class Handler(object):
    _tableName = ''
    _primaryKey = ''
    _configPath = ''
    filePaths=[]
    config = {}
    fields=[]

    def __init__(self, configPath):
        self._configPath = configPath
        self.handle_configPath()
        self.setConfig()
        self.fileOperate()

    def handle_configPath(self):
        """
        Return config by input configPath
        """
        with open(self.configPath, 'r')as f:
            text = f.readlines()
        for line in text:
            line = line.strip('\n')
            ret = line.split('=')
            self.config[ret[0]] = ret[1]

    def setConfig(self):
        self._tableName=self.config['tableName']
        self._primaryKey=self.config['primaryKey']
        self.filePaths=self.config['path']

    def get_csv_fields(self,csvfile):
        """
        input:    csvfile path
        output:   title form of mysql table
        """
        with open(csvfile, 'r')as f:
            reader = csv.reader(f)
            for each in reader:
                if True:
                    self.fields= each
                    break

    def fileOperate(self):
        for path in self.filePaths:
            gen_new_csvFile(path)
