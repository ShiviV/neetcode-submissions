class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices)==1):
            return 0
        max=prices[1]-prices[0]
        for i in range(len(prices)-1):#0-4
            #max=prices[i+1]-prices[i]#-6,4,-2
            print ('out', max)
            for j in range(i+1,len(prices)):
                if prices[i]>prices[j]:
                    continue

                else:
                    profit=prices[j]-prices[i]
                    if profit>max:
                            max=profit#5
                    print ('in',profit, max)

        if max<0:
            return 0
        else:
            return max
                    





    # def find (self, profits: List[int]) -> int:
    #    max=prices[0]
    #    for i in range(len(profits)):
    #     profit = profits[i]
    #     if profit>max:
    #         max=profit
    #     else:
    #         continue:

    #     return max




                