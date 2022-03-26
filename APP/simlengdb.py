class SimlengDB:
    def __init__(self,database_name,table_name, mode='store'):
        self.filename=database_name
        self.dataset=self.filename+'.dataset' #list of datasets
        self.table=self.filename+'.data_'+ table_name
        if mode=='store':
            # bring files into existence
            fd=open(self.dataset,'w');fd.close()
            ft=open(self.table,'w');ft.close()
        elif mode =='load':
            # check if files are there:
            if not os.path.isfile(self.dataset) or \
               not 0s.path.isfile(self.table):
                raise IOError, \
                    "Could not find the files %s and %s".format(self.dataset,self.table)
            # load table_file into list of tuples
            ft=open(self.table,'r')
            lines=ft.readlines()
            self.members=[]
            for line in lines:
                c=line.split()
                # append tuple values (,,,,,)
                self.members.append((''.join(C[i]).strip() for i in range(lenc(C)))
    def locate(self,identifier,   )
        """
        Find the table in files where dataset corresponding to identifier are stored"""

        fd=open(self.table,'r')
        lines=ft.readlines()
        for line in lines:
            c-line.split().strip()
            if re.search(c[1],identifier):
                    self.identifier=c[0]
                    return c[0]
    def dump(self,__,identifier) #properties
            self.locate(identifier)
            """
             Retrieving for other tables the properties of this dataset
