from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about-us')
def about_us():
    return render_template('about-us.html')



@app.route('/dash')
def dash():
    return render_template('dash.html')

@app.route('/farmer')
def farmer():
    return render_template('login-farmer.html')

@app.route('/farmer_promoter')
def farmer_promoter():
    return render_template('login-promoter.html')

@app.route('/agrodealer')
def agrodealer():
    return render_template('login-dealer.html')

@app.route('/customer')
def customer():
    return render_template('logincustomer.html')

@app.route('/research')
def research():
    return render_template('login-research.html')

@app.route('/policy_maker')
def policy_maker():
    return render_template('login-policy maker.html')        

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/market')
def market():
    return render_template('market.html')

@app.route('/account_farmer')
def account_farmer():
    return render_template('account-farmer.html')

@app.route('/create-account promoter')
def promoter():
    return render_template('account-promoter.html')  

@app.route('/create-account agrodealer')
def account_agrodealer():
    return render_template('account-agrodealer.html') 

@app.route('/create-account customer')
def account_customer():
    return render_template('account-customer.html')  

@app.route('/create-account research')
def account_research():
    return render_template('account-research.html')  

@app.route('/create-account policy_maker')
def account_policy_maker():
    return render_template('account-policy maker.html')             

@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/irrigation')
def irrigation():
    return render_template('irrigation.html')

@app.route('/service')
def service():
    youtube_id = "29KDeFQIIpI"
    return render_template('service.html', youtube_id=youtube_id)

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/appreciate-agrodealer')
def appreciateagrodealer():
    return render_template('appreciate-agrodealer.html')

@app.route('/login-agrodealer')
def loginagrodealer():
    return render_template('login-agrodealer.html')

@app.route('/login-customer')
def logincustomer():
    return render_template('login-customer.html')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
