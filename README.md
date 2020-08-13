#Senimental-Analysis project' README.md

Please Follow these instructions before cloning this project:-

  1. You should have pip installed in your system which gets installed automatically when you install python
  
  2. As i have created this project in spyder ide so i did not require to install matplotlib seperately, in your case-> you can firstly install matplotlib by: "pip install matplotlib"
  
  3. Now Write command in cmd => "pip install GetOldTweets3" => this will download the twitter library which will provide us old twitts on any topic within a given period.
  
  4. In this point if you want to just see general working of project then clone this project and run only "Main_Without_nltk.py" only but that would not provide most accurate 
     result but work good enough for just testing.
     
     Otherwise for having more accurate results just follow this:
     ->Now you have to first download nltk (Natural language toolkit), for that write command: "pip install nltk" then after cloning my project run that "nltk_settings.py" file.
       that will open a nltk downloader wizard in which you have to download all packages that would take some time(around 400mb).
     
     ->Now you have to run Main_With_nltk.py only and that's enough for getting output in which you would be able to select 3 options and proceed further.

Note: If you get errors in commands when you write them in windows command prompt then set your path otherwise you can also run them in anaconda prompt if you have 
      Anaconda installed in your system and then run them in spyder without any problems.
      
Note: For Mac-Os kindly follow these links:
      1). For installing GetOldTweets3: https://pypi.org/project/GetOldTweets3/
      2). For installing nltk: https://www.nltk.org/data.html
