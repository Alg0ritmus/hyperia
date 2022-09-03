import json
import os.path
import requests
from bs4 import BeautifulSoup 
import uuid
class HyperiaCarierParser():
    def __init__(self,origin):
        self.origin=origin # origin shpuld be like this: https://www.hyperia.sk
        self.url=origin+"/kariera/" # URL of main page
        self.jobs_available_urls_list=[] # store all available urls of cariers
        self.jobs_positions=[] # specific jobs positions

        self.data_dicts=[] # parsed data
        
    
    def scrape_jobs_urls(self):
        # get request from url
        request_main_page = requests.get(self.url)

        # create BeautifulSoup parser
        soup = BeautifulSoup(request_main_page.text,"html.parser")
        
        hrefs = soup.find_all("a", {"class": "arrow-link"})

        # add links to specific jobs,
        #  but only those links, that has attr data-v-4496620d
        for link in hrefs:
            if "data-v-4496620d" in str(link):
                # add links to jobs_available_urls_list list
                self.jobs_available_urls_list.append(self.origin+link.get("href"))

                # add job positions to jobs_position array
                # should look like this:
                #['leadgen-php-developer', 'python-developer', 'senior-ppc-specialista', 'product-owner', 'lead-frontend-developer', 'frontend-developer', 'kimbino-senior-php-developer']
                self.jobs_positions.append(link.get("href").replace("/",""))

        

    def scrape_position(self,position_name):
        if position_name not in self.jobs_positions:
            return print(position_name,"is not valid job position.Try one of theese:",self.jobs_positions)
        
        #request jobs page
        request_jobs_page = requests.get(self.origin+"/"+position_name)
        # change encoding from ISO-8859-1 to utf-8 (diakritika)
        request_jobs_page.encoding='utf-8'
        

        # create BeautifulSoup parser
        soup = BeautifulSoup(request_jobs_page.text,"html.parser")
  

        ####
        # GET Title
        ####

        # get hero-text div
        hero_div = soup.find("div", {"class": "hero-text"})

        # get Title from hero_div
        title = hero_div.h1.string

        
        ####
        # GET place, salary and contract_type
        ####
        
        # get hero-icons div
        hero_body = soup.find("div", {"class": "hero-icons"})
       
        # get list of all p tags in hero-icons
        p_tags = hero_body.find_all("p")

        


    
        # p_tags is list of p tags, contents[-1] extract specific item from p[i],
        # in this case we get place, salary and contract_type
        place = str(p_tags[0].contents[-1].text)
        salary = str(p_tags[1].contents[-1]).replace(",- €","€")
        contract_type = str(p_tags[2].contents[-1].string)  


        ####
        # GET contact_email
        ####

        position_a_mailto = soup.find("a", {"class": "position-button"})
        # extracted mail, syntax: mailto:hr@hyperia.sk
        mailto = str(position_a_mailto.get("href"))
        # get just email
        contact_email = mailto[mailto.find(":")+1::] #mailto.find(":") -> find index where ":" is located and create string slice [idx+1::]
        
       
       
        # fill in data_dicts
        self.data_dicts.append({
		"title": title,
		"place": place,
		"salary": salary,
		"contract_type": contract_type,
		"contact_email": contact_email
        })

        
    def scrape_position_all(self):
        # check if list of jobs positions is empty
        if not self.jobs_positions:
            self.scrape_jobs_urls()

        for position in self.jobs_positions:
            self.scrape_position(position)


    def getJson(self):
        # check if dict is empty
        if not self.data_dicts:
            print("No data to stringify")
            return None
        
        # Serializing json w ensure_ascii=False, bcs. sometimes it gets messy with non-ascii symbols
        json_object = json.dumps(self.data_dicts, indent = 4, ensure_ascii=False).encode('utf8')
        return json_object.decode('utf8')
    
    def getJsonToFile(self,filename):
        json_data_from_data_dicts = self.getJson()
        # in case user parse bad format of json file like: "test.johsn"
        # we can extract name of the file : "test" and add extension explicitly
        # when we create a file

        filename = filename[0:(filename.find("."))]


        # if file with parsed name already exists, create new one with uuid

        if os.path.isfile(filename+".json"):
            filename += str(uuid.uuid1())
            print("File already exists, new file will be generated w name:",filename+".json")

        # write file w UTF-8 (diakritika)
        with open(filename+".json", "w", encoding="utf-8") as f:
            f.write(json_data_from_data_dicts)



"""
myParser = HyperiaCarierParser("https://www.hyperia.sk")
myParser.scrape_jobs_urls()
print(myParser.jobs_positions)



myParser.scrape_position("leadgen-php-developer")
print(myParser.data_dicts)



myParser = HyperiaCarierParser("https://www.hyperia.sk")
myParser.scrape_position_all()
#print(myParser.data_dicts)


myParser.getJsonToFile("skuska1.json")
"""


