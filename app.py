try:

    from flask import Flask

    from flask import redirect, url_for, request, render_template, send_file
    from io import BytesIO

    from flask_wtf.file import FileField
    from wtforms import SubmitField
    from flask_wtf import Form
    import sqlite3
    print("All Modules Loaded .... ")
except:
    print (" Some Module are missing ...... ")


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"


@app.route('/', methods=["GET", "POST"])
def index():

    form = UploadForm()
    if request.method == "POST":

        if form.validate_on_submit():
            file_name = form.file.data
            database(name=file_name.filename, data=file_name.read() )
            return render_template("home.html", form=form)

    return render_template("home.html", form=form)


@app.route('/download', methods=["GET", "POST"])
def download():

    form = UploadForm()

    if request.method == "POST":

        conn= sqlite3.connect("__IAMRI__.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        ask=str(request.get_data('ask'))
        c = cursor.execute(""" SELECT * FROM  my_table  where name like '% """+ask+""" %'""") 
        # create a empty  object variable
        output_data_v=None
        for x in c.fetchall():
            name_v=x[0]
            print(type(name_v))
            data_v=x[1]
            output_data_v=data_v
            print(type(data_v))
        
            break

        conn.commit()
        cursor.close()
        conn.close()
        file=request.form['file']
        if file=='pdf':
            return send_file(BytesIO(output_data_v), attachment_filename='Document.pdf', as_attachment=True)
        elif file=='python':
            return send_file(BytesIO(output_data_v), attachment_filename='Main.py', as_attachment=True)
        elif file=='doc':
            return send_file(BytesIO(output_data_v), attachment_filename='Document.doc', as_attachment=True)
        elif file=='docx':
            return send_file(BytesIO(output_data_v), attachment_filename='Document.docx', as_attachment=True)
        elif file=='txt':
            return send_file(BytesIO(output_data_v), attachment_filename='Document.txt', as_attachment=True)
        elif file=='xlsx':
            return send_file(BytesIO(output_data_v), attachment_filename='Document.xlsx', as_attachment=True)
        elif file=='xls':
            return send_file(BytesIO(output_data_v), attachment_filename='Document.xls', as_attachment=True)
        elif file=='csv':
            return send_file(BytesIO(output_data_v), attachment_filename='Document.csv', as_attachment=True)
        elif file=='jpg' or file=='png' or file=='jpeg':
            return send_file(BytesIO(output_data_v), attachment_filename='Document.jpg', as_attachment=True)
        elif file=='gif':
            return send_file(BytesIO(output_data_v), attachment_filename='Document.gif', as_attachment=True)
        elif file=='mp4':
            return send_file(BytesIO(output_data_v), attachment_filename='Document.mp4', as_attachment=True)
        elif file=='mp3':
            return send_file(BytesIO(output_data_v), attachment_filename='Document.mp3', as_attachment=True)
        elif file=='ppt':
            return send_file(BytesIO(output_data_v), attachment_filename='Document.ppt', as_attachment=True)
        else:
            return send_file(BytesIO(output_data_v), attachment_filename='document.pdf', as_attachment=True)


    return render_template("home.html", form=form)




class UploadForm(Form):
    file = FileField()
    submit = SubmitField("submit")
    download = SubmitField("download")

def database(name, data):
    conn= sqlite3.connect("__IAMRI__.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS my_table (name TEXT,data BLOP) """)
    cursor.execute("""INSERT INTO my_table (name, data) VALUES (?,?) """,(name,data))

    conn.commit()
    cursor.close()
    conn.close()



def query():
        conn= sqlite3.connect("__IAMRI__.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  my_table """)

        for x in c.fetchall():
            name_v=x[0]
            data_v=x[1]
            break

        conn.commit()
        cursor.close()
        conn.close()
        return send_file(BytesIO(data_v), attachment_filename='Document.pdf', as_attachment=True)
        



if __name__ == "__main__":
    app.run(debug=True)
