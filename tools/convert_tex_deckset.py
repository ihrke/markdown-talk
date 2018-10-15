"""
this is for Deckset https://www.decksetapp.com/
"""
import re, sys, glob, os

texfname=sys.argv[1]

with open(texfname, "r") as f:
    tex=f.read()

mdtext=tex

pat=re.compile(r"\s*\\begin{document}(.*?)\\end{document}", re.DOTALL)#, re.DOTALL)
mdtext=pat.search(mdtext).groups()[0]



pat=re.compile(r"[ ]*\\begin{frame}(.*?)\\end{frame}", re.DOTALL)#, re.DOTALL)
mdtext=pat.sub(r"---\n\1", mdtext)


mdtext=re.sub(r"[ \t]*\\item", "-", mdtext)


pat=re.compile(r"[ \t]*\\begin{itemize}\s*", re.DOTALL)
mdtext=pat.sub(r"", mdtext)

pat=re.compile(r"[ \t]*\\end{itemize}\s*", re.DOTALL)
mdtext=pat.sub(r"", mdtext)


pat=re.compile(r"[ \t]*\\frametitle{(.*?)}[ \t]*", re.DOTALL)
mdtext=pat.sub(r"# \1", mdtext)

pat=re.compile(r"[ \t]*\\framesubtitle{(.*?)}[ \t]*", re.DOTALL)
mdtext=pat.sub(r"## \1", mdtext)

mdtext=re.sub(r"\\ldots", r"...", mdtext)

mdtext=re.sub(r"%.*", r"", mdtext)


## equation
mdtext=re.sub(r"\$(.*?)\$", r"$$\1$$", mdtext)

pat=re.compile(r"\\\[(.*?)\\\]", re.DOTALL)
mdtext=pat.sub(r"$$\1$$", mdtext)

mdtext=re.sub(r"\\textbf{(.*?)}", r"**\1**", mdtext)
mdtext=re.sub(r"{\\bf\s*(.*?)\s*}", r"**\1**", mdtext)

pat=re.compile(r"[ \t]*\\begin{center}[ \t]*", re.DOTALL)
mdtext=pat.sub(r"", mdtext)

pat=re.compile(r"[ \t]*\\end{center}[ \t]*", re.DOTALL)
mdtext=pat.sub(r"", mdtext)

pat=re.compile(r"[ \t]*\\begin{block}{(.*?)}(.*?)\\end{block}[ \t]*", re.DOTALL)#, re.DOTALL)
mdtext=pat.sub(r"###\1\n\2", mdtext)

pat=re.compile(r"[ \t]*\\centering\s*", re.DOTALL)
mdtext=pat.sub(r"", mdtext)

pat=re.compile(r"[ \t]*\\begin{minipage}{.*?}[ \t]*", re.DOTALL)
mdtext=pat.sub(r"", mdtext)

pat=re.compile(r"[ \t]*\\end{minipage}[ \t]*", re.DOTALL)
mdtext=pat.sub(r"", mdtext)

pat=re.compile(r"[ \t]*\\pause\s*", re.DOTALL)
mdtext=pat.sub(r"", mdtext)

## figures
pat=re.compile(r"[ \t]*\\includegraphics.*?{(.*?)}[ \t]*")#, re.DOTALL)
while(pat.search(mdtext)):
#for m in pat.finditer(mdtext):
    m=pat.search(mdtext)
    #print m.groups()[0], m.span()
    picfname=m.groups()[0]
    fnames=glob.glob(picfname+"*")
    pdf=[os.path.splitext(fname)[1]==".pdf" for fname in fnames]
    if len(fnames)==0:
        fname=picfname
    elif not all(pdf):
        fname=[fname for fname in fnames if os.path.splitext(fname)[1]!=".pdf"][0]
    else:
        pdfname=[fname for fname in fnames if os.path.splitext(fname)[1]==".pdf"][0]
        #cmd="convert -density 300 %s %s"%(pdfname, picfname+".png") ## imagemagick
        cmd="sips -s format png  %s --out %s"%(pdfname,picfname+".png") ## better on Mac OSX
        print >> sys.stderr, cmd
        fname=picfname+".png"
        os.system(cmd)
        #print cmd
    mdtext=mdtext[0:m.start()]+"![inline,fit](%s)\n"%fname+mdtext[m.end():]


## tables
pat=re.compile(r"[ \t]*\\begin{table}(.*?)\end{table}[ \t]*", re.DOTALL)

while(pat.search(mdtext)):
#for m in pat.finditer(mdtext):
    m=pat.search(mdtext)
    tab=m.group()
    ## within each table
    tabpat=re.compile(r"[ \t]*\\begin{tabular}{(.*?)}\s*(.*?)\s*\\end{tabular}[ \t]*", re.DOTALL)
    #print tab
    m2=tabpat.search(tab)
    #print m2
    colpattern=m2.groups()[0]
    tab=m2.groups()[1]
    #print tab
    #tab=re.sub(r"^\s*", "",tab,re.MULTILINE)
    tab=re.sub(r"&", "|", tab)
    tab=re.sub(r"\\hline", "", tab)
    ncol=colpattern.count("c")+colpattern.count("l")+colpattern.count("r")
    tab=re.subn(r"\\\\\s*", "\n"+"---|"*ncol, tab, count=1)[0]
    tab=re.sub(r"\\\\[.*?]", "", tab)
    tab=re.sub(r"\\\\", "", tab)
    #print tab
    mdtext=mdtext[0:m.start()]+tab+mdtext[m.end():]


#mdtext=pat.sub(r"![inline,100%](\1)\n", mdtext)


print mdtext
