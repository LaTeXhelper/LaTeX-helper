Folder="${HOME}/.latexhelper" # 模板仓库的工作目录
LaTeX_engine="pdflatex" # 目前只支持pdflatex
dvi_engine="dvipdfm"
begin_text="
\\documentclass{article}\n
\\usepackage{amsfonts}\n
\\usepackage{amsmath}\n
\\usepackage{float}\n
\\usepackage{capt-of}\n
\\usepackage{graphicx}\n
\\usepackage{subfigure}\n
\\\begin{document}\n
" 

end_text="
\\\end{document}
"

cd ${Folder}/LaTeX-templates/article
echo "working in ${Folder}/LaTeX-templates/article"

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
