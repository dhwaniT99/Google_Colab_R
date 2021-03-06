# -*- coding: utf-8 -*-
"""R in colab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dco-0duSYSXNOfZ1PcYnyQVlMFWlMj6v
"""

R.version.string

install.packages(plotly)

library(tidyr)
library(dplyr)
library(base)
library(plotly)

data <- read.csv("activities.csv",na.strings=c("","NA"))
head(data, 5)

#First thing we can do is to work on plotting the time elapsed during the whole time. 
#There are various plots, using plotly in this case.

"""**Plotting the distance covered during the whole time**

---


"""

data_act$Date <- strsplit(data_act$Activity.Date, ",", "")

data_act <- cSplit(data_act$Date,"Date",",")