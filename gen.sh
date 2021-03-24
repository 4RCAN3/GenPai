if ![ -d $gen ]
then
  python venv gen || python3 venv gen
fi
gen\Scripts\activate.bat || source gen/Scripts/activate
pip install -r requirements.txt || pip3 install -r requirements.txt