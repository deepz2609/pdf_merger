import PyPDF2
import pyfiglet
from colorama import init, Fore

banner = pyfiglet.figlet_format("PDF MERGER", font="slant")
colored_banner = Fore.BLUE + banner + Fore.RESET
print(colored_banner)
pdf=[]

try:
    n = int(input(Fore.GREEN+"[+]Enter the number of pdf: "+ Fore.RESET))
    for i in range(1,n+1):
        file=input(Fore.GREEN+f"[+]Enter the {i} pdf file path/name:"+ Fore.RESET)
        pdf.append(file)
    merged_pdf=input(Fore.GREEN+"[+]Enter the final pdf name(with .pdf extension): "+ Fore.RESET)

    merger=PyPDF2.PdfMerger()
    for filename in pdf:
        pdfFile= open(filename,'rb')
        pdfreader = PyPDF2.PdfReader(pdfFile)
        merger.append(pdfreader)
    merger.write(merged_pdf)
    pdfFile.close()
    print(Fore.GREEN+f"\n{merged_pdf} has been created successfully!"+ Fore.RESET)
except Exception as e:
    print(Fore.RED+"Please enter correct details"+Fore.RESET)

