class Calculator:

  def __init__(self, currentprincipal, annualAddition, yrsGrow, intRate):
    #self.values = []
    self.currentprincipal = currentprincipal
    self.annualAddition = annualAddition
    self.yrsGrow = yrsGrow
    self.intRate = intRate
    self.results = float()
    self.data = []

  def PressButton(self):
    P = self.currentprincipal
    annualAddition = self.annualAddition
    r = self.intRate * 0.01
    t = self.yrsGrow    
    n = 1
    self.data.clear()
    self.data.append(P)

    for i in range(int(t)):
      P = P + annualAddition
      interest = P * (r/n)
      A = P + interest
      P = A
      val = format(P, '.2f')
      self.data.append(float(val))
      
    self.results = format(A, '.2f')
    return self.results