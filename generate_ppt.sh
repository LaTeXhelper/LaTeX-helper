Folder="./LaTeX-templates/beamer"
LaTeX_engine="xelatex" # 目前只支持xelatex
Style="Copenhagen" # AnnArbor Antibes Bergen Berkeley Berlin Boadilla cambridgeUS Copenhagen Darmstadt default Dresden Frankfurt Goettingen Hannover Ilmenau JuanLesPins Luebeck Madrid Malmoe Marburg Montpellier PaloAlto Pittsburgh Rochester Singapore Szeged Warsaw

begin_text="
\\documentclass{beamer}\n\\usetheme{${Style}}\n\\usepackage{bm}\n\\usepackage{subcaption}\n\\usepackage{enumitem}\n\\usepackage{wrapfig}\n\\usepackage{ulem}\\usepackage{blindtext}\n\\\begin{document}\n
"

end_text="
\n\\\end{document}
"

if [ ! -d "tmp" ]; then
    mkdir -p tmp
fi

if [ ! -d "pdf/${Style}" ]; then
    mkdir -p pdf/${Style}
fi

for pic_file in `find ${Folder} -name "*.png" -o -name "*.jpg"`
do
    cp ${pic_file} ./
done

tex_files=`find ${Folder} -name "*.tex"`

echo ${tex_files}

for tex_file in ${tex_files}
do
    base_file=$(basename -- ${tex_file})
    if [ ! -f "pdf/${Style}/${base_file%.*}.pdf" ]; then
        tmp_file=tmp/${base_file}
        touch ${tmp_file}
        echo ${begin_text} >> ${tmp_file}
        cat ${tex_file} >> ${tmp_file}
        echo ${end_text} >> ${tmp_file}
        echo "generating ${base_file%.*}.pdf with style ${Style}"
        ${LaTeX_engine} ${tmp_file} 1>/dev/null
    fi
done

rm *.log *.aux *.png *.jpg *.out *.nav *.snm *.toc
for file in `find . -maxdepth 1 -name "*.pdf" `
do
    mv $file ./pdf/${Style}
done
rm -rf tmp
echo "preview the pdf files in pdf//"