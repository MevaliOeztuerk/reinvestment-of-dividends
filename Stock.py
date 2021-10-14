class stock():
    def __init__(self,name,wkn):
        self.name = name
        self.wkn = wkn

    def set_div_values(self,div_yield,div_growth,share_growth_pa,price):
        self.price = price
        self.div_yield = div_yield / 100
        self.div_growth = div_growth / 100
        self.share_growth_pa = share_growth_pa / 100
        self.div = price * div_yield / 100
        self.div_sum = 0

    # calc compounded dividends p.a grown over time
    def calc_div(self,time, reinvest = True):

        dividends = dict()
        dividends[0] = [self.div]

        if reinvest is True:
            for t in range(1,time+1):
                temp = []
                for i in range(t):
                    temp.append(dividends[t-1][i]*(1+self.div_growth))

                div_sum_reinvest = sum(dividends[t - 1])
                temp.append(div_sum_reinvest*self.div_yield)
                dividends[t] = temp

            n = len(dividends.keys())-1
            div_pa = sum(dividends[n])

        else:
            div_pa = self.div
            for t in range(1,time+1):
                div_pa = div_pa * (1+self.div_growth)
                #print(f"{t}:  Div: {div} ")

        return div_pa

    # calc compount interest
    def calc_endcap(self,time):
        return self.price * pow(1+self.share_growth_pa,time)


coke = stock("Coca Cola","850663")
coke.set_div_values(3.1,5,5,100)

coke_dividends_re = coke.calc_div(20)
coke_dividends = coke.calc_div(20,False)
coke_endcap = coke.calc_endcap(20)
print(f"dividends reinveste:\t{coke_dividends_re}\ndividends not reinveste:\t{coke_dividends}\nendcap: \t{coke_endcap}")