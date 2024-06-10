class ChartModel:
    def __init__(self):
        self.nameChart2Value = ["Bar Chart", "Line Chart",  "Scatter Plot",
                                "Heatmap", "Violin Plot", "Pair Plot", "Joint Plot", "Swarm Plot", "Boxen Plot"]
        self.nameChart1Value = ["Pie Chart",
                                "Histogram", "Box Plot",  "Rug Plot"]

    def get_1_value(self):
        return self.nameChart1Value

    def get_2_value(self):
        return self.nameChart2Value
