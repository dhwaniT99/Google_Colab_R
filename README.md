# Working in R on Google Colab
Here are my views: 
Trying out R in Google colab

So, I have been working on projects in R lately and I got curious if R can be used on Google Colab or not and there are ways where we can use R in Google Colab especially in Python runtime. 

### What is Colab

Google Research's Colaboratory (abbreviated "Colab") is a product. Colab is a web-based Python editor that allows anyone to write and run arbitrary Python code. It's particularly useful for machine learning, data analysis, and education. Colab is a hosted Jupyter notebook service that doesn't require any setup and gives you free access to computational resources, including GPUs. More information can be found here <a href = https://research.google.com/colaboratory/faq.html> More info </a>

Anyway let's dive right in setting up Google Colab in R 

There are two ways to do so: 

<ol>
  <li> Running R in python runtime enviroment using rpy2 package</li>
  <li> Setting up a R runtime enviroment </li>
</ol>

Running R in python runtime enviroment using rpy2 actually helps you to run python and R simultaneously, there are various other runtime enviroments.
All we need to do is just start the colab and then install the rpy2 package, 

Do the following to set up R in colab

<li> Open your browser <\li>
<li> Create a new notebook: https://colab.research.google.com/#create=true.</li?>
<li> Run rmagic by executing this command %load_ext rpy2.ipython. </li>
 <li> After that, every time you want to use R, add %%R in the beginning of each cell. </li>
 
 ## Approach 2
 
<ol>
 <li> Directly copy paste in R this  https://colab.research.google.com/#create=true&language=r, or this short URL https://colab.to/r </li>
 This will setup R as a runtime enviroment and now you will be able to work in R in Colab.
 </ol>
   
Here is the notebook where I tried to reading dataset and performing some operations using some CRAN packages
   
You do not have an option to mount the R files in Google Drive where we have to work on the various files where we can work on using the R file however there are various ways where we can work on. 
   
## The limitations: 
   
   <li> Cant import libraries/packages which do not belong CRAN, </li>
   <li> Mounting Google Drive to the runtime is not readily available, however the package googledrive helps you to connect R runtime with google drive </li> 
   
   There is a way to actually install the packages which do belong to CRAN like installing plotly, for visualinsing the graphs,                 
   devtools::install_github(“DeveloperName/PackageName”)
   
   
