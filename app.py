from flask import Flask, render_template


app = Flask(__name__)

contacts = [{"name":"aviad", "age": 36 ,"phone": "0528693299" , "email": "aviad@gmail.com"}, 
            {"name":"Ran","age": 44, "phone": "0505213654" , "email": "raner@gmail.com"}]


@app.route('/')
def contact_list():
    return render_template('contact_list.html', contacts=contacts)


@app.route("/list_page")
def list_p():
    final_str =""
    for c in contacts:
        final_str+= f'<li style= "color: blue">{c["name"]} - {c["phone"]}</li>'
    return f'{final_str}'


@app.route("/one_contact/<int:index>")
def contact(index):
    return f'user name is: {contacts[index-1]["name"]}. age:{contacts[index-1]["age"]}. phone: {contacts[index-1]["phone"]}. mail: {contacts[index-1]["email"]}'


@app.route("/add_contact")
def add_c():
    return "<button>add</button>"


if __name__ == "__main__":
    app.run(debug=True)
