from tkinter import *
from Calculator import Calculator
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class UserInterface:
    
    def __init__(self, root):
        # Frame 1
        ## frame that is defined 
        frame = Frame(root)
        frame.grid(row = 0, column = 0)
        #### Current Principal
        self.labelPrincipal = Label(frame, text = "Current Principal:")
        self.labelPrincipal.grid(row = 0, column = 0, padx = 10, pady=10, sticky = W)
        self.labelMoneySign = Label(frame, text = "$")
        self.labelMoneySign.grid(row = 0, column = 1, sticky = E)
        self.entryPrincipal = Entry(frame, width = 15)
        self.entryPrincipal.grid(row = 0, column = 2, padx = 15, pady = 10, sticky = W)
        #### Annual Addition
        self.labelAddition = Label(frame, text = "Annual Addition:")
        self.labelAddition.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = W)     
        self.labelMoneySign = Label(frame, text = "$")
        self.labelMoneySign.grid(row = 1, column = 1, sticky = E)   
        self.entryAddition = Entry(frame, width = 15)
        self.entryAddition.grid(row = 1, column = 2, padx = 15, pady = 10, sticky = W )
        #### Years to Grow
        self.labelYears = Label(frame, text = "Years to Grow:")
        self.labelYears.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = W)        
        self.entryYears = Entry(frame, width = 10)
        self.entryYears.grid(row = 2, column = 2, padx = 15, pady = 10, sticky = W )
        #### Interest Rate
        self.labelInterestRate = Label(frame, text = "Interest Rate:")
        self.labelInterestRate.grid(row = 3, column = 0, padx =10, pady = 10, sticky = W)        
        self.entryInterestRate = Entry(frame, width = 10)
        self.entryInterestRate.grid(row = 3, column = 2, padx = 15, pady = 10, sticky = W+E )
        self.labelPercentSign = Label(frame, text = "%")
        self.labelPercentSign.grid(row = 3, column = 3, sticky = W, padx = (0, 15))   
        #### Compounds Once Annually
        self.labelTimesCompounded = Label(frame, text = "Compounds Once Annually")
        self.labelTimesCompounded.grid(row = 4, column = 0, padx = 10, pady = 10, sticky =  W)        
        #### Execute Button
        self.execute = Button(frame, text = " Calculate ", command = self.executeCalculate)
        self.execute.grid(row = 4, column =2, pady = 20, padx = 15, sticky = E + W)
        #### Results
        self.labelResults = Label(frame, text = "Results: ")
        self.labelResults.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = W)       
        self.labelMoneySign = Label(frame, text = "$")
        self.labelMoneySign.grid(row = 5, column = 1, sticky = E)   
        self.entryResults = Entry(frame, width = 15)
        self.entryResults.grid(row = 5, column = 2, padx = 15, pady = 10, sticky = W )

        #Frame 2
        self.frame2 = Frame(root,  height = 500, width = 500)
        self.frame2.grid(row = 0, column = 1)
        # line graph
        self.figure = Figure(figsize=(5,3.5), dpi = 100)
        self.plot1 = self.figure.add_subplot(1,1,1)
        self.canvas = FigureCanvasTkAgg(self.figure, self.frame2)
        self.canvas.get_tk_widget().grid(row = 0, column = 1, padx = 25, pady = 25)

        self.plot1.set_xlabel('Years')
        self.plot1.set_ylabel('Dollar Value')
        self.plot1.set_title('Compounding Interest Over Time')

        self.figure.tight_layout()

    def executeCalculate(self):
        try:
            newCalculator = Calculator(float(self.entryPrincipal.get()), float(self.entryAddition.get()), float(self.entryYears.get()), float(self.entryInterestRate.get()))
            self.entryResults.delete(0, END)
            self.entryResults.insert(END, str(newCalculator.PressButton()))
        except:
            pass
        self._plotData(newCalculator.data)
    
    def _plotData(self, dataSet):
        # creating the figure and subplot
        self.figure = Figure(figsize=(5,3.5), dpi = 100)
        self.plot1 = self.figure.add_subplot(1,1,1)
        # putting the figure onto tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, self.frame2)
        self.canvas.get_tk_widget().grid(row = 0, column = 1, padx = 25, pady = 25)
        
        # setting subplot labels
        self.plot1.set_xlabel('Years')
        self.plot1.set_ylabel('Dollar Value')
        self.plot1.set_title('Compounding Interest Over Time')

        # plotting the subplot's graph and setting x and y tick marks
        self.plot1.plot([i for i in range(len(dataSet))], dataSet)
        self.plot1.axis([0,int(len(dataSet)),int(min(dataSet)),int(max(dataSet)*1.2)])
        
        ## labeling the graph
        if len(dataSet) > 10:
            for x, y in zip([i for i in range(len(dataSet))], dataSet):
                label = "$" + format(y, '.2f')
                if x % 2 == 0:
                    if x == 0:
                        continue
                    else:
                        self.plot1.annotate(label, (x,y), textcoords = "offset points", xytext = (0,10), ha='center')
                                      
                elif x == max(([i for i in range(len(dataSet))])):
                    self.plot1.annotate(label, (x,y), textcoords = "offset points", xytext = (0,10), ha='center')               

        elif len(dataSet) <= 10:    
            for x, y in zip([i for i in range(len(dataSet))], dataSet):
                if x == 0:
                    continue
                else:
                    label = "$" + format(y, '.2f')             
                    self.plot1.annotate(label, (x,y), textcoords = "offset points", xytext = (0,10), ha='center')
        
        # making sure the layout is tight
        self.figure.tight_layout()