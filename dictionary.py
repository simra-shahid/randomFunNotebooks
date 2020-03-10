from bs4 import BeautifulSoup
import requests

   
    
def main(word=None):
    
        if (word==None) : word=input("Enter the word: ")
        
        wiki='https://www.merriam-webster.com/dictionary/{0}'.format(word)
        r = requests.get(wiki)
        soup=BeautifulSoup(r.text,"html.parser")

        try:
            menu(word,soup)
           


        except:
            possibility=soup.find("p",attrs={"class":"definition-inner-item with-sense"}).text
            possibility=possibility.split("\n")
            for i in possibility :
                if i :
                   # print (i,"," ,end="")
                   print("Did you mean %s Y or N ", i)
                   val=input()
                   if  (val.upper()=="Y"):
                        word=i
                        main(word)
                        #print(word)
                        break
                        
                   elif val.upper()=='N': pass
                   else: print("\nWe didnt understand your Input please recheck ")

        return




def get_meaning(word,soup):
     meaning=soup.find('span',attrs={'class': 'dt' }).text
     meaning=meaning.split(":")  # This is done because the text contains " :  meaning : some other words "
     try: print( "Meaning : ",meaning[1] ) # so we pick the 1st element which is the meaning
     except: print("Meaning: ",(meaning[0].split("\n"))[1])  #incase we selected an abbreviation
                                                             # abbreviations are stored like this 




def sentences(word,soup):
    sentences=soup.find("p",attrs={"class":'definition-inner-item'}).text
    print("Sentence with %s : " %(word),end=" ")
    print(sentences)
    

def menu(word,data):

     
     get_meaning(word,data)
     sentences(word,data)
     print("\n")
     ans=input("Do you want to enter another word ? enter Y OR N").upper()
     if (ans=="Y"): main()
     return

main()
