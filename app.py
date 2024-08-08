import joblib
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import pandas as pd
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

diabetesmodel = pickle.load(open('diabetes-prediction-rfc-model.pkl', 'rb'))
breastcancermodel = joblib.load('model.pkl')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'


# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(15), unique=True)
#     email = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(80))
# with app.app_context():
#     db.create_all()

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])


@app.route('/')
def index():
    return render_template("/index.html")


@app.route('/about')
def about():
    return render_template("/about.html")


@app.route('/appointment')
def appointment():
    return render_template("appointment.html")


@app.route('/blog_sidebar')
def blog_sidebar():
    return render_template("/blog-sidebar.html")


@app.route('/blog_single')
def blog_single():
    return render_template("/blog_single.html")


@app.route('/bp')
def bp():
    return render_template("/bp.html")


@app.route('/bpconsultancy')
def bpconsultancy():
    return render_template("/bpconsultancy")


@app.route('/bptips')
def bptips():
    return render_template("/bptips.html")


@app.route('/breast')
def breast():
    return render_template("/breast.html")


@app.route('/breastconsultancy')
def breastconsultancy():
    return render_template("/breastconsultancy.html")


@app.route('/breasttips')
def breasttips():
    return render_template("/breasttips.html")


@app.route('/contact')
def contact():
    return render_template("/contact.html")


@app.route('/Cystitis')
def Cystitis():
    return render_template("/Cystitis.html")


@app.route('/Cystitisconsultancy')
def Cystitisconsultancy():
    return render_template("/Cystitisconsultancy.html")


@app.route('/Cystitistips')
def Cystitistips():
    return render_template("/Cystitistips.html")


@app.route('/demo')
def demo():
    return render_template("/demo.html")


@app.route('/department_single')
def department_single():
    return render_template("/department_single.html")


@app.route('/department')
def department():
    return render_template("/department.html")


@app.route('/diabetes')
def diabetes():
    return render_template("/diabetes.html")


@app.route('/diabetesconsultancy')
def diabetesconsultancy():
    return render_template("/diabetesconsultancy.html")


@app.route('/diabetestips')
def diabetestips():
    return render_template("/diabetestips.html")


@app.route('/diabetes_questions')
def diabetes_questions():
    return render_template("/diabetes_questions.html")


@app.route('/heart')
def heart():
    return render_template("/heart.html")


@app.route('/heartconsultancy')
def heartconsultancy():
    return render_template("/heartconsultancy.html")


@app.route('/hearttips')
def hearttips():
    return render_template("/hearttips.html")

@app.route('/heart_questions')
def heart_questions():
    return render_template('heart_questions.html')


@app.route('/HPV')
def HPV():
    return render_template("/HPV.html")


@app.route('/hpvconsultancy')
def hpvconsultancy():
    return render_template("/hpvconsultancy.html")


@app.route('/hpvtips')
def hpvtips():
    return render_template("/hpvtips.html")


@app.route('/index')
def indexx():
    return render_template("/index.html")


@app.route('/Menstrual')
def Menstrual():
    return render_template("/Menstrual.html")


@app.route('/menstrualconsultancy')
def menstrualconsultancy():
    return render_template("/menstrualconsultancy.html")


@app.route('/menstrualtips')
def menstrualtips():
    return render_template("/menstrualtips.html")


@app.route('/Mental')
def Mental():
    return render_template("/Mental.html")


@app.route('/mentalconsultancy')
def mentalconsultancy():
    return render_template("/mentalconsultancy.html")


@app.route('/mentaltips')
def mentaltips():
    return render_template("/mentaltips.html")


@app.route('/Osteoporosis')
def Osteoporosis():
    return render_template("/Osteoporosis.html")


@app.route('/osteoporosisconsultancy')
def osteoporosisconsultancy():
    return render_template("/osteoporosisconsultancy.html")


@app.route('/osteoporosistips')
def osteoporosistips():
    return render_template("/osteoporosistips.html")


@app.route('/pcocconsultancy')
def pcocconsultancy():
    return render_template("/pcocconsultancy.html")


@app.route('/pcos')
def pcos():
    return render_template("/pcos.html")


@app.route('/pcosconsultancy')
def pcosconsultancy():
    return render_template("/pcosconsultancy.html")


@app.route('/pcostips')
def pcostips():
    return render_template("/pcostips.html")


@app.route('/problem')
def problem():
    return render_template("/problem.html")


@app.route('/service')
def service():
    return render_template("service.html")


@app.route('/slot2')
def signup2():
    return render_template("/slot2.html")


@app.route('/Thyroid')
def Thyroid():
    return render_template("/Thyroid.html")


@app.route('/thyroidconsultancy')
def thyroidconsultancy():
    return render_template("/thyroidconsultancy.html")


@app.route('/thyroidtips')
def thyroidtips():
    return render_template("thyroidtips.html")


@app.route('/tips')
def tips():
    return render_template("tips.html")


@app.route('/help')
def help():
    return render_template("help.html")


@app.route('/terms')
def terms():
    return render_template("tc.html")


# @app.route('/login', methods=['GET', 'POST'])
# def login2():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user and check_password_hash(user.password, form.password.data):
#             login_user(user, remember=form.remember.data)
#             return redirect(url_for('dashboard'))
#         return render_template("login.html", form=form)
#     return render_template("login.html", form=form)



# @app.route('/signup', methods=['GET', 'POST'])
# def signup22():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
#         new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()

#         return redirect("/login")
#     return render_template('signup.html', form=form)


# @app.route("/dashboard")
# def dashboard():
#     return render_template("dashboard.html")


@app.route("/cancer")
def cancer():
    return render_template("/cancer")


@app.route("/diabetes")
def diabetes2():
    return render_template("/diabetes")


@app.route("/heart")
def heart2():
    return render_template("/heart")


@app.route("/kidney")
def kidney():
    return render_template("/kidney")

@app.route("/breast_questions")
def breastquestions():
    return render_template("breast_cancer_questions.html")

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if size == 7:
        loaded_model = joblib.load('kidney_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]


@app.route("/predictkidney", methods=['GET', 'POST'])
def predictkidney():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if len(to_predict_list) == 7:
            result = ValuePredictor(to_predict_list, 7)
            prediction = ("Patient has a high risk of Kidney Disease, please consult your doctor immediately"
                          if int(result) == 1 else
                          "Patient has a low risk of Kidney Disease")
        return render_template("result.html", prediction=prediction)


diabetes_feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

@app.route("/diabetespredict", methods=["POST"])
def predict_diabetes():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        
        to_predict_df = pd.DataFrame([to_predict_list])
        
        result = diabetesmodel.predict(to_predict_df)
        result = result[0]
        if int(result) == 1:
                prediction = "Sorry, you have chances of getting the disease. Please consult a doctor immediately."
        else:
                prediction = "No need to fear. You have no dangerous symptoms of the disease."
        
        return render_template("result.html", prediction=prediction)


breast_cancer_feature_names = ['clump_thickness', 'uniform_cell_size', 'uniform_cell_shape', 'marginal_adhesion', 'single_epithelial_size', 'bare_nuclei', 'bland_chromatin', 'normal_nucleoli','mitoses']

@app.route("/breastcancerpredict", methods=["POST"])
def breastcancerpredict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        
        to_predict_df = pd.DataFrame([to_predict_list], columns=breast_cancer_feature_names)
        
        result = breastcancermodel.predict(to_predict_df)
        print("Prediction result:", result)
        result = result[0]
        if int(result) == 1:
            prediction = "Sorry, you have chances of getting the disease. Please consult a doctor immediately."
        else:
            prediction = "No need to fear. You have no dangerous symptoms of the disease."
        
        return render_template("result.html", prediction=prediction)
    
if __name__ == '__main__':
    app.run(debug=True)
