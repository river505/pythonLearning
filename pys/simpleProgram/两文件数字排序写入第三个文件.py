class Solution():
    def solve(self, file_1, file_2, file_3):
        '''
        :type file_1, file_2, file_3: str
        :rtype : None
        '''
        ls1=[]
        with open(str(file_1).strip(), "r") as f1, open(str(file_2).strip(), "r") as f2, open(str(file_3), "w") as f3:
            ls1.extend(list(map(lambda x: int(x), f1.readlines())))
            ls1.extend(list(map(lambda x: int(x), f2.readlines())))
            ls1.sort()
            for x in ls1:
                f3.writelines(str(x))
                f3.writelines('\n')


c=Solution()
c.solve(r'..\data\123.txt',r'..\data\456.txt',r'..\data\asd.txt')