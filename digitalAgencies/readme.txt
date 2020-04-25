#          ////////////    Scraper for www.digitalagencynetwork.com     //////////////////

TO run the scraper you need to do the following:
1- Install Pyhton3.x in your system
2- Intsall python-pip in your system
3- In terminal/cmd, head to the parent directory "digitalAgencies" and run command "pip install -r requirements.txt"
4- Go to digitalAgencies/spiders and open "agencies_spider.py"
5- At line 11, in start_urls, type the url of the country you want to scrape
    For example, for usa, it is , start_urls = "https://digitalagencynetwork.com/agencies/usa/"

6- You must have firefox installed, otherwise it wont work, because it scrapes through Mozilla Firefox
    In case you must want to use some other browser, contact the developer, But preferablly just install Firefox.

7- At line 63, in "country" write the name of Country you are scraping, this was kept manual due to some technical
    issues. For example, for usa , it would be ["country": "USA"]

8- Now in cmd/terminal, head to the parent/root directory "digitalAgencies" and type command
    "scrapy crawl agencies_spider -o Output_file.csv"
        here, Output_file.csv is the name of file you want to store the data to.

9- And that's it.



#      ///////////////////////  Happy Scraping    ////////////////////