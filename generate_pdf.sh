Folder="/home/nullptr/.latexhelper"
LaTeX_engine="xelatex" # 目前只支持xelatex
begin_text="
\\documentclass[UTF8]{ctexart}\n\\usepackage{amsfonts}\\usepackage{amsmath}\n\\usepackage{figure}\\usepackage{capt-of}\\usepackage{float}\\\begin{document}\n
"

end_text="
\n\\\end{document}
"

if [ ! -d "tmp" ]; then
  mkdir tmp
fi

cp ${Folder}/a.png a.png
cp ${Folder}/a.jpg a.jpg

tex_files=`find ./LaTeX-templates/article -name "*.tex"`

echo ${tex_files}

for tex_file in ${tex_files}
do
    base_file=$(basename -- ${tex_file})
    tmp_file=tmp/${base_file}
    touch ${tmp_file}
    echo ${begin_text} >> ${tmp_file}
    cat ${tex_file} >> ${tmp_file}
    echo ${end_text} >> ${tmp_file}
    echo "generating ${base_file%.*}.pdf ..."
    ${LaTeX_engine} -file-line-error -halt-on-error -interaction=nonstopmode ${tmp_file} 1>/dev/null
done

rm *.log *.aux *.png *.jpg
for file in `find . -maxdepth 1 -name "*.pdf" `
do
    if [ ! -e "${Folder}/pdf/${file}" ]; then
    mv $file ./pdf
    fi
done
rm -rf tmp
echo "preview the pdf files in pdf/"
