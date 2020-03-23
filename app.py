from flask import Flask,render_template,request
from notifications import send_email

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route('/blog',methods=['GET','POST'])
def blog():
    return render_template('blog.html')

@app.route('/single_blog',methods=['GET','POST'])
def single_blog():
    return render_template('single_blog.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
    return render_template('contact.html')

@app.route('/elements',methods=['GET','POST'])
def elements():
    return render_template('elements.html')

@app.route('/main',methods=['GET','POST'])
def main():
    return render_template('main.html')

@app.route('/portfolio_details',methods=['GET','POST'])
def portfolio_details():
    return render_template('portfolio_details.html')

@app.route('/portfolio',methods=['GET','POST'])
def portfolio():
    return render_template('portfolio.html')

@app.route('/service',methods=['GET','POST'])
def service():
    return render_template('service.html')


@app.route('/single',methods=['GET','POST'])
def single():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        message = request.form['message']

        data = [name,email,phone_number,message]

        subject = "Enquiry"
        fileToSend = None
        msgg = " Name : "+name+" \n  Email : "+email+" \n Phone Number : "+phone_number+" \n message : "+message+"  "

        toaddr = "teamstockity@gmail.com"
        send_email(msgg,subject,toaddr,fileToSend)

        return render_template('index.html')

    else:
        return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)
