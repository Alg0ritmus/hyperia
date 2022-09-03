import sys
import webScraper as ws
ORIGIN = "https://www.hyperia.sk"
my_parser = ws.HyperiaCarierParser(ORIGIN)
my_parser.scrape_jobs_urls()


def bad_args():
    print("Wrong use of arguments. Available args:")
    print("""
    '-s' [job_position]    ->  scrape particular job position
    '-sa'                  ->  scrape all job position
    '-j'                   ->  print JSON file w jobs positions
    '-jo' [filename.json]  ->  create and fill in JSON file w jobs positions
    """)

def case(idx):
    

    switcher = {
        "-s":my_parser.scrape_position,
        "-sa":my_parser.scrape_position_all,
        "-j":my_parser.getJson,
        "-jo":my_parser.getJsonToFile,
    }
    

    try:
        if (sys.argv[idx] == '-s') or (sys.argv[idx] == '-jo'): 
            switcher[sys.argv[idx]](str(sys.argv[idx+1]))
        elif (sys.argv[idx] == '-j'):
            print(switcher[sys.argv[idx]]())
        else:
            switcher[sys.argv[idx]]()
    except Exception as e:
        print("your arg:",sys.argv[idx] )
        print(e)
        bad_args()
        


if __name__ == "__main__":
    for idx in range(len(sys.argv)):
        if sys.argv[idx][0] == "-":
            case(idx)


