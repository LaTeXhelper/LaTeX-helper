Folder="/home/nullptr/.latexhelper"
LaTeX_engine="pdflatex" # 目前只支持pdflatex
Style="Copenhagen" # AnnArbor Antibes Bergen Berkeley Berlin Boadilla cambridgeUS Copenhagen Darmstadt default Dresden Frankfurt Goettingen Hannover Ilmenau JuanLesPins Luebeck Madrid Malmoe Marburg Montpellier PaloAlto Pittsburgh Rochester Singapore Szeged Warsaw
cd ${Folder}

begin_text="
\\documentclass{beamer}\n
\\usetheme{${Style}}\n
\\usepackage{bm}\n
\\usepackage{subcaption}\n
\\usepackage{enumitem}\n
\\usepackage{wrapfig}\n
\\usepackage{ulem}
\\usepackage{blindtext}\n
\\\begin{document}\n
"

end_text="
\n\\\end{document}
"

cd ${Folder}/LaTeX-templates/beamer
echo "working in ${Folder}/LaTeX-templates/beamer"

tex_files=`find . -maxdepth 2 -name "*.tex"`
echo "all the existing tex files: ${tex_files}"

for tex_file in ${tex_files}
do
    tex_base_name=$(basename -- ${tex_file})
    if [ ! -f "../../pdf/${tex_base_name%.*}.pdf" ]; then
        tmp_file=${tex_base_name}
        touch ${tmp_file}
        echo ${begin_text} >> ${tmp_file}
        cat ${tex_file} >> ${tmp_file}
        echo ${end_text} >> ${tmp_file}
        echo "generating ${tex_base_name%.*}.pdf ..."
        ${LaTeX_engine} -file-line-error -halt-on-error -interaction=nonstopmode ${tmp_file} 1>/dev/null
        rm *.toc *.vrb *.aux *.log *.nav *.out *.snm *.synctex.gz *dvi *.tex
    fi
done

for file in `find . -maxdepth 1 -name "*.pdf" `
do
    mv $file ../../pdf
done

echo "preview the pdf files in ${Folder}/pdf/"