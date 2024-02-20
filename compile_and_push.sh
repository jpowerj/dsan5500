quarto render
git add -A .
commitMsg="Auto-commit"
if [ $# -eq 1 ]
  then
    commitMsg="$1"
fi
git commit -m "${commitMsg}"
git push
