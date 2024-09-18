try:
    import httpx, re, urllib.parse, json, time, os, sys, random, string
    from rich.console import Console
    from bs4 import BeautifulSoup
    from rich.panel import Panel
    from rich import print as printf
except (ModuleNotFoundError):
    __import__('os').system('pip install rich httpx beautifulsoup4')

SKIP_KEYWORDS = ['/u/', 'login', 'about', 'premium', '/t/']
TAUTAN = []
PERTANYAAN_DEFAULT = ('justpaste site:justpaste.it')

class FEATURE:

    def __init__(self) -> None:
        pass

    def MAIN(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        printf(Panel("""[bold red]  _______                ______                        \n (_______)           _  (_____ \             _         \n      _ _   _  ___ _| |_ _____) )____  ___ _| |_ _____ \n  _  | | | | |/___|_   _)  ____(____ |/___|_   _) ___ |\n | |_| | |_| |___ | | |_| |    / ___ |___ | | |_| ____|\n[bold white]  \___/|____/(___/   \__)_|    \_____(___/   \__)_____)\n        [bold green]Justpaste.it Link Scraper - by Rozhak""", width=60, style="bold bright_black"))

        printf(Panel(f"[bold white]Please fill in the question you will use for the search. For example:[bold green] September 2024 site:justpaste.it[bold white]\n*you can press `[bold red]Enter[bold white]` if you don't have a question!", width=60, style="bold bright_black", title="> [Pertanyaan] <", subtitle="╭───────", subtitle_align="left"))
        self.PERTANYAAN = Console().input("[bold bright_black]   ╰─> ")
        if len(self.PERTANYAAN) == 0:
            self.PERTANYAAN = PERTANYAAN_DEFAULT
        else:
            self.PERTANYAAN = self.PERTANYAAN

        printf(Panel(f"[bold white]Do you want to visit justpaste.it link directly and find all the links there. Type[bold red] Y[bold white] if you want to display type[bold green] N[bold white] if you don't want to display!", width=60, style="bold bright_black", title="> [Visit Link] <", subtitle="╭───────", subtitle_align="left"))
        self.VISIT = Console().input("[bold bright_black]   ╰─> ")
        printf(Panel(f"[bold white]You must use `[bold green]AIRPLANE MODE[bold white]` to avoid spam. if you want to stop press[bold yellow] CTRL + C[bold white]\n*[bold red]remember not to use CTRL + Z to save the results[bold white]!", width=60, style="bold bright_black", title="> [Catatan] <"))
        self.FILENAME = (f"Temporary/{''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))}.json")

        CLASS = SCRAPING()
        CLASS.GOOGLE(PERTANYAAN=self.PERTANYAAN)

        if len(TAUTAN) != 0:
            if os.path.exists(self.FILENAME) == True:
                os.remove(self.FILENAME)
            with open(f'{self.FILENAME}', 'w') as JSON_FILE:
                json.dump(TAUTAN, JSON_FILE, indent=4)
            JSON_FILE.close()

            if self.VISIT.lower() != 'y':
                for IDX, LINK in enumerate(TAUTAN, start=1):
                    self.NUMBER = str(IDX).zfill(2)
                    printf(Panel(f"[bold green]{self.NUMBER}[bold white]. Link:[bold green] {LINK}", width=60, style="bold bright_black"))
            else:
                for URL in TAUTAN:
                    self.COMBINED_OUTPUT = VISIT().JUSTPASTE(URL=URL)
                    printf(Panel(f"{self.COMBINED_OUTPUT}", width=60, style="bold bright_black"))
            printf(Panel(f"[bold white]You have successfully obtained[bold green] {len(TAUTAN)}[bold white] justpaste.it links and saved them in[bold red] {self.FILENAME}", width=60, style="bold bright_black", title="> [Selesai] <"))
            sys.exit()
        else:
            printf(Panel(f"[bold red]Sorry, we didn't find any justpaste.it links, you can change the Query in this Tools!", width=60, style="bold bright_black", title="> [Tautan Kosong] <"))
            sys.exit()

class SCRAPING:

    def __init__(self) -> None:
        pass

    def GOOGLE(self, PERTANYAAN):
        try:
            with httpx.Client() as CLIENT:
                CLIENT.headers.update({
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'Accept-Encoding': 'gzip, deflate, br, zstd',
                    'sec-ch-ua-full-version': '"128.0.6613.86"',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Connection': 'keep-alive',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
                    'sec-ch-ua-arch': '"x86"',
                    'sec-ch-ua-bitness': '"64"',
                    'Host': 'www.google.com',
                    'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.86", "Not;A=Brand";v="24.0.0.0", "Google Chrome";v="128.0.6613.86"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-form-factors': '"Desktop"',
                    'sec-ch-ua-wow64': '?0',
                    'Sec-Fetch-Dest': 'document',
                    'sec-ch-ua-platform': '"Windows"',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'none',
                    'Sec-Fetch-User': '?1',
                    'sec-ch-ua-platform-version': '"15.0.0"',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                })
                PARAMS = {
                    'oq': '{}'.format(PERTANYAAN),
                    'q': '{}'.format(PERTANYAAN),
                    'ie': 'UTF-8',
                    'gs_lcrp': '',
                    'sourceid': 'chrome',
                }
                RESPONSE = CLIENT.get('https://www.google.com/search?', params=PARAMS)
                self.COOKIES = "; ".join([f"{name}={value}" for name, value in RESPONSE.cookies.items()])

                self.SOUP = BeautifulSoup(RESPONSE.text, 'html.parser')
                self.NEXT_PAGE = self.SOUP.find('a', {'aria-label': 'Halaman berikutnya'})

                self.JUSTPASTE = re.findall(r'/url\?q=(https://justpaste\.it/[^\&]+)', str(self.SOUP))
                for URL in self.JUSTPASTE:
                    if any(KEYWORD in URL for KEYWORD in SKIP_KEYWORDS):
                        continue
                    else:
                        if str(URL) not in TAUTAN:
                            TAUTAN.append(URL)
                            printf(f"[bold bright_black]   ──>[bold white] DUMP[bold green] {str(URL).upper()}[bold white]/[bold green]{len(TAUTAN)}[bold white] LINK!     ", end='\r')
                            time.sleep(0.07)
                        else:
                            continue
                if self.NEXT_PAGE != None:
                    printf(f"[bold bright_black]   ──>[bold green] SUCCESSFULLY FOUND THE NEXT PAGE!        ", end='\r')
                    time.sleep(2.5)
                    self.NEXT_URL = (f"https://www.google.com{self.NEXT_PAGE['href']}")
                    self.NEXT_GOOGLE(CLIENT=CLIENT, NEXT_URL=self.NEXT_URL, COOKIES=self.COOKIES)
                else:
                    printf(f"[bold bright_black]   ──>[bold red] CAN'T FIND NEXT PAGE!                      ", end='\r')
                    time.sleep(5.0)
                    self.NEXT_URL = ('null')
                    return (False)
        except (httpx.RequestError):
            printf(f"[bold bright_black]   ──>[bold red] YOUR CONNECTION IS BAD!              ", end='\r')
            time.sleep(9.5)
            self.GOOGLE()
        except (KeyboardInterrupt):
            printf(f"                                        ", end='\r')
            time.sleep(2.0)
            return (True)

    def NEXT_GOOGLE(self, CLIENT, NEXT_URL, COOKIES):
        try:
            CLIENT.headers.update({
                'Referer': '{}'.format(NEXT_URL),
                'Cookie': '{}'.format(COOKIES),
            })
            RESPONSE = CLIENT.get('{}'.format(NEXT_URL))

            self.SOUP = BeautifulSoup(RESPONSE.text, 'html.parser')
            self.NEXT_PAGE = self.SOUP.find('a', {'aria-label': 'Halaman berikutnya'})

            self.JUSTPASTE = re.findall(r'/url\?q=(https://justpaste\.it/[^\&]+)', str(self.SOUP))
            for URL in self.JUSTPASTE:
                if any(KEYWORD in URL for KEYWORD in SKIP_KEYWORDS):
                    continue
                else:
                    if str(URL) not in TAUTAN:
                        TAUTAN.append(URL)
                        printf(f"[bold bright_black]   ──>[bold white] DUMP[bold green] {str(URL).upper()}[bold white]/[bold green]{len(TAUTAN)}[bold white] LINK!     ", end='\r')
                        time.sleep(0.07)
                    else:
                        continue
            if self.NEXT_PAGE != None:
                printf(f"[bold bright_black]   ──>[bold green] SUCCESSFULLY FOUND THE NEXT PAGE!        ", end='\r')
                time.sleep(2.5)
                self.NEXT_URL = (f"https://www.google.com{self.NEXT_PAGE['href']}")
                self.NEXT_GOOGLE(CLIENT=CLIENT, NEXT_URL=self.NEXT_URL, COOKIES=self.COOKIES)
            else:
                printf(f"[bold bright_black]   ──>[bold red] CAN'T FIND NEXT PAGE!                      ", end='\r')
                time.sleep(5.0)
                self.NEXT_URL = ('null')
                return (False)
        except (httpx.RequestError):
            printf(f"[bold bright_black]   ──>[bold red] YOUR CONNECTION IS BAD!              ", end='\r')
            time.sleep(9.5)
            self.NEXT_GOOGLE(CLIENT=CLIENT, NEXT_URL=NEXT_URL, COOKIES=COOKIES)

class VISIT:

    def __init__(self) -> None:
        pass

    def JUSTPASTE(self, URL):
        try:
            with httpx.Client() as CLIENT:
                CLIENT.headers.update({
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'Accept-Encoding': 'gzip, deflate, br, zstd',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Connection': 'keep-alive',
                    'Host': 'justpaste.it',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'none',
                    'Sec-Fetch-User': '?1',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
                })
                RESPONSE = CLIENT.get('{}'.format(URL))

                self.SOUP = BeautifulSoup(RESPONSE.text, 'html.parser')
                try:
                    self.ARTICLE_TITLE = self.SOUP.find('h1', class_='articleFirstTitle').string
                except (AttributeError):
                    self.ARTICLE_TITLE = ('Tidak ada')

                self.ARTICLE_CONTENT = self.SOUP.find('div', id='articleContent')
                self.LINKS = self.ARTICLE_CONTENT.find_all('a', href=True)

                self.COMBINED_OUTPUT = (f"[bold white]Judul Konten:[bold green] {self.ARTICLE_TITLE}\n\n[bold white]Link dan Deskripsi:[bold green]\n")
                for LINK in self.LINKS:
                    self.HREF = LINK['href']
                    self.REDIRECT = re.compile(r'/redirect/[^/]+/(.+)').search(self.HREF)
                    if self.REDIRECT != None:
                        self.EXTRACTED_LINK = self.REDIRECT.group(1)
                        self.DECODED_LINK = urllib.parse.unquote(self.EXTRACTED_LINK)
                        self.CAPTION = LINK.find_previous_sibling(string=True)
                        
                        self.CAPTION = self.CAPTION.strip() if self.CAPTION else ""
                        self.COMBINED_OUTPUT += f"[bold white]{self.CAPTION}[bold green] {self.DECODED_LINK}\n"
                    else:
                        self.COMBINED_OUTPUT += f"[bold green] {self.HREF}\n"
                return (self.COMBINED_OUTPUT.strip())
        except (httpx.RequestError):
            printf(f"[bold bright_black]   ──>[bold red] YOUR CONNECTION IS BAD!              ", end='\r')
            time.sleep(9.5)
            self.JUSTPASTE(URL=URL)

if __name__=='__main__':
    try:
        os.makedirs('Temporary', exist_ok=True)
        os.system('git pull')
        FEATURE().MAIN()
    except (Exception) as e:
        printf(Panel(f"[bold red]{str(e).capitalize()}", width=60, style="bold bright_black", title="> [Error] <"))
        sys.exit()
    except (KeyboardInterrupt):
        sys.exit()