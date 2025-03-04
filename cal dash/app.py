from flask import Flask, render_template
import pandas as pd

app = Flask(__name__, template_folder="coop_site")

#
# http://localhost:8080/gdp/gdp_numbers
# http://127.0.0.1:8080
#

#
#
#   GDP Stuff
#
#

gdp_file_path = r"C:\Users\coope\OneDrive\Documents\created\projects\cal site project\data sets\gross domestic product\cal quarterly gdp.xlsx"

df_gdp = pd.read_excel(gdp_file_path, engine="openpyxl")

df_gdp = df_gdp.dropna().reset_index(drop=True)
df_gdp.columns = df_gdp.iloc[0]
df_gdp = df_gdp.drop(0)
df_gdp = df_gdp.drop(df_gdp.columns[[0, 1, 2]], axis=1)

gdp = []
for i, row in df_gdp.iterrows():
    gdp.append(row[-1])

realGDP = 1000000 * int(gdp[0])
nominalGDP = 1000000 * int(gdp[2])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gdp')
def gdp():
    return render_template('gdp.html')

@app.route('/prices')
def prices():
    return render_template('prices.html')

@app.route('/individual_income')
def individual_income():
    return render_template('individual_income.html')

@app.route("/gdp/gdp_numbers")
def gdp_numbers():
    number = {
        "real": realGDP,
        "nominal": nominalGDP
        }
    return render_template("gdp_numbers.html", number=number)

if __name__ == "__main__":
    app.run(debug=True, port=8080)