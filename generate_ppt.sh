Folder="/home/nullptr/.latexhelper"
Style="Copenhagen" # AnnArbor Antibes Bergen Berkeley Berlin Boadilla cambridgeUS Copenhagen Darmstadt default Dresden Frankfurt Goettingen Hannover Ilmenau JuanLesPins Luebeck Madrid Malmoe Marburg Montpellier PaloAlto Pittsburgh Rochester Singapore Szeged Warsaw
cd ${Folder}

begin_text="
\\documentclass{beamer}\n
\\usetheme{${Style}}\n
\\usepackage{bm}\n
\\usepackage{subcaption}\n
\\usepackage{enumitem}\n
\\usepackage{wrapfig}\n
\\usepackage{ulem}\n
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
        cp ../../pictures/*.png .
        cp ../../pictures/*.jpg .
        tmp_file=${tex_base_name}
        touch ${tmp_file}
        echo ${begin_text} >> ${tmp_file}
        cat ../../requirements_ppt.txt >> ${tmp_file}
        echo "\\\begin{document}\n" >> ${tmp_file}
        cat ${tex_file} >> ${tmp_file}
        echo ${end_text} >> ${tmp_file}
        echo "\e[34m→ generating ${tex_base_name%.*}.pdf ...\e[0m"
        pdflatex -file-line-error -halt-on-error -interaction=nonstopmode ${tmp_file} 1>/dev/null
        if [ -f "${tex_base_name%.*}.pdf" ]; then
            echo "\e[32m✔ generate ${tex_base_name%.*}.pdf successfully! \e[0m"
            mv ${tex_base_name%.*}.pdf ../../pdf/
        else
            echo "\e[31m✘ can not generate ${tex_base_name%.*}.pdf! \e[0m"
        fi
        rm -f *.*
    else
        echo "\e[33m● ${tex_base_name%.*}.pdf already exists! \e[0m"
    fi
done

echo "preview the pdf files in ${Folder}/pdf/"