class Solution():
    def solve(self, file_1, file_2, file_3):
        '''
        :type file_1, file_2, file_3: str
        :rtype : None
        '''

        with open(file_1,'r+') as f1,open(file_2,'r+') as f2, open(file_3,'r+') as f3:
            asd = f1.readlines()
            asd += f2.readlines()
            sorted(asd, key=lambda x:int(x))
            f3.writelines(asd)


c=Solution()
c.solve(r'.\data\123.txt',r'.\data\456.txt',r'.\data\asd.txt')