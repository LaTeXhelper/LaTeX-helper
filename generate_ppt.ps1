$corrent_dir=pwd
$Folder="~\\.latexhelper"
$LaTeX_engine="xelatex"
$LaTeX_engine_options="-file-line-error -halt-on-error -synctex=1 -interaction=nonstopmode"
$Style="Copenhagen"
cd $Folder

$begin_text="
\documentclass{beamer}
\usetheme{${Style}}
\usepackage{bm}
\usepackage{subcaption}
\usepackage{enumitem}
\usepackage{wrapfig}
\usepackage{ulem}
\usepackage{blindtext}
"

$end_text="
\end{document}
"

cd "${Folder}\\LaTeX-templates\\beamer"
echo "working in ${Folder}\\LaTeX-templates\\beamer"

$tex_files=Get-ChildItem -Recurse -Force -Name -Include *.tex
echo "all the existing tex files: $tex_files"

foreach($tex_file in $tex_files)
{
    $tex_base_name=[System.IO.Path]::GetFileNameWithoutExtension($tex_file)
    $path_to_pdf="..\\..\\pdf\\$tex_base_name.pdf"
    if (Test-Path $path_to_pdf)
    {
        echo "[Warning] $tex_base_name.pdf exists"
    }
    else
    {
        copy "..\\..\\pictures\\*.png" .
        copy "..\\..\\pictures\\*.jpg" .
        $tmp_file="$tex_base_name.tex"
        if(Test-Path $tmp_file)
        {
            del $tmp_file
        }
        new-item $tmp_file >> $null
        echo $begin_text >> $tmp_file
        type "..\\..\\requirements_ppt.txt" >> $tmp_file
        echo "\begin{document}" >> $tmp_file
        type $tex_file >> $tmp_file
        echo $end_text >> $tmp_file
        echo "generating $tex_base_name.pdf ..."
        xelatex -file-line-error -halt-on-error -interaction=nonstopmode $tmp_file > $null
        if(Test-Path "$tex_base_name.pdf")
        {
            echo "[OK] generated $tex_base_name.pdf successfully!"
            move "$tex_base_name.pdf" "..\\..\\pdf\\$tex_base_name.pdf"
        }
        else
        {
            echo "[Error] failed to generate $tex_base_name.pdf"
        }
        del *.*
    }
}

echo "preview the pdf files in ${Folder}\\pdf\\"
cd $corrent_dir