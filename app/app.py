from flask import Flask, render_template, request
from hdxapi import get_datasets_with_active_datastores, get_recently_updated_datasets


app = Flask(__name__, static_folder="../static", static_url_path="/static")
#url = "https://data.hdx.rwlabs.org/api/3/action/package_search?q=ebola"
url = "https://data.hdx.rwlabs.org/api/3/action/package_search?q="
temp = [{"package_title": "Really cool data","package_name": "really-cool-data","resource_name": "cool.csv"}]
temp2 = [{"package_title": "More data","package_name": "really-cool-data","resource_name": "cool.csv"}]
endpoint = "https://data.hdx.rwlabs.org/api/3/action/"
action_package_search = "package_search"

@app.route('/', methods=["GET","POST"])
def index():
    # TODO improve the default list to be the latest 10 datasets or something relevant
    #items = get_datasets_with_active_datastores(url + "?" + "rows=" + str(row_limit))
    if request.method == "GET":
        return render_template('index.jinja2.html', 
            rows=get_recently_updated_datasets(url=endpoint+action_package_search))
    else:
        return render_template('index.jinja2.html', 
                           rows=temp)

@app.route('/search', methods=["POST"])
def search():
    query = request.form['q']
    rows = request.form['rows']
    print url + query + rows
    return render_template('index.jinja2.html', rows=get_datasets_with_active_datastores(url + query + "&rows=" + rows), query=query, url=url + query + "&rows=" + rows)
    #return render_template('index.jinja2.html', rows=[{"package_title": url + query + "&rows=" + rows}])

@app.route('/submit/', methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        return do_submit()
    else:
        return render_template('submit.jinja2.html')

def do_submit():
    # article = Article(title=title, link=link)
    # insert_article(article)
    article = insert_article()
    return render_template("inserted.jinja2.html", article=article)

def run_devserver():
    app.run(debug=True)

if __name__ == "__main__":
    run_devserver()
