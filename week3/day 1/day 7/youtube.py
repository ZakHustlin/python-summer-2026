import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    link = re.search(r"https://www.youtube.com/embed/([A-Za-z0-9_-]+)", s)
    if link:
        return "https://youtu.be/" + link.group(1)
    else:
        return None






if __name__ == "__main__":
    main()