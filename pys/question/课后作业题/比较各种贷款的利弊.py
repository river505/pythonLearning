def findPayment(loan, r, m):
    return loan * ((r * (1 + r) ** m) / ((1 + r) ** m - 1))

class Mortgage(object):
     def __init__(self, loan, annRate, months):
         self.loan = loan
         self.rate = annRate / 1200.0
         self.months = months
         self.paid = [0.0]
         self.owed = [loan]
         self.payment = findPayment(loan, self.rate, self.months)
         self.legend = None

     def makePayment(self):
         self.paid.append(self.payment)
         reduction = self.payment - self.owed[-1] * self.rate
         self.owed.append(self.owed[-1] - reduction)

     def getTotalPaid(self):
         return sum(self.paid)

     def __str__(self):
         return str(self.legend)


class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(r) + '%, for ' + str(months) + ' months'


class FixedWithPoints(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan * (pts / 100.0)]
        self.legend = 'Fixed, ' + str(r) + '%, ' + str(pts) + ' points, for ' + str(months) + ' months'


class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate/1200
        self.nextRate = r / 1200.0
        self.legend = str(teaserRate)\
                      + '% for ' + str(self.teaserMonths)\
                      + ' months, \n then ' + str(r) + '%, for ' + str(months) + ' months'

    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.owed[-1], self.rate, self.months - self.teaserMonths)
        Mortgage.makePayment(self)


def compareMortgages(amt, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths):
    # 请在此添加代码，补全函数compareMortgages
        #********** Begin *********#
    
    m1=Fixed(amt,fixedRate,years*12)
    m2=FixedWithPoints(amt,ptsRate,years*12,pts)
    m3=TwoRate(amt, varRate2, years*12, varRate1, varMonths)
    morts=[m1,m2,m3]

    totMonths=years*12
        #********** End *********#
    for m in range(totMonths):
        # 请在此添加代码，补全函数compareMortgages
        #********** Begin *********#
        m1.makePayment()
        m2.makePayment()
        m3.makePayment()
        #********** End *********#
    for m in morts:
        print(m)
        print('Loan ' + str(amt) + ' Total payments = ' + str(int(m.getTotalPaid())))

if __name__=="__main__":
    compareMortgages(200000, 30, 7, 3.25, 5, 4.5, 9.5, 48)
    print('*'*40)
    compareMortgages(1000000, 30, 7, 20, 5, 4.5, 9.5, 48)
    print('*' * 40)
    compareMortgages(500000, 10, 7, 20, 5, 4.5, 9.5, 48)