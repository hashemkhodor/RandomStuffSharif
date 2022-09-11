def split(s):
    L = s.split('\n')
    if L[-1]!='':
        L  = [l+'\n' for l in L[:-1]]+[L[-1]]
    else:
        L = [l+'\n' for l in L[:-1]]
    return L
class fakeFile(list):
    # a list of strings 
    def __init__(self, s):
        list.__init__ (self,split(s))
        self.__mode__ = 'closed' 
        self.__cursor__=-1 #For readline function
        self.__position__=1 #For tell function(current file position)
        self.__name__=''
        self.__open__=False
        
    def read(self):
        """Reads File Content"""
        assert self.__open__ , "Value Error: I/O operation on closed file"
        assert self.__mode__ == 'r', 'UnsupportedOperation - not readable'
        
        return ''.join(self)
    def close(self):
        """Closes File"""
        self.__open__=False
        self.__mode__='closed'
    def __contains__(self,s):
        assert self.__open__,"Value Error: I/O operation on closed file"
        assert self.__mode__ == 'r' and type(s)==str, 'UnsupportedOperation - not readable' 
        return s in self.read()
    def write(self,s):
        assert self.__open__ , "Value Error: I/O operation on closed file"
        assert (self.__mode__ =='w' or self.__mode__=='a') and type(s)==str, 'UnsupportedOperation - not writtable'
        self.extend(split(s))
    def writable(self):
        return self.__mode__=="a" or self.__mode__=="w"
    def readable(self):
        return self.__mode__=="r"
    
    def readline(self,n=-1):
        #n takes default value -1
        assert self.__open__ , "Value Error: I/O operation on closed file"
        assert type(n)==int and n<len(self) and n>=-1, "Error"
        if n==-1:
            if self.cursor>=len(self)-1:
                #Stop reading after finishing the content of the file
                return ''
            else:
                self.__cursor__+=1
                self.__position__+=len(self[self.cursor])
                return ''.join(self[self.cursor])
            
        return ''.join(self[n])
    def tell(self):
        #Returns the current file position
        assert self.__open__ , "Value Error: I/O operation on closed file"
        return self.__position__
    
    def __str__(self):
        return "<_io.TextIOWrapper name='"+self.__name__+"' mode='" + self.__mode__+"' encoding='cp1252'>"
    
    def __getitem__(self,i):
        assert self.__open__, "Value Error: I/O operation on closed file"
        return list.__getitem__(self,i)
    def __iter__(self):
        ##Handling for item in list when the file is closed
        assert self.__open__, "Value Error: I/O operation on closed file"
        return list.__iter__(self)