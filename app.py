from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Attendance Management System</title>

    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:'Segoe UI',sans-serif;
        }

        body{
            background:#f4f7fc;
        }

        .navbar{
            background:#1e293b;
            color:white;
            padding:20px 40px;
            display:flex;
            justify-content:space-between;
            align-items:center;
        }

        .navbar h2{
            color:#38bdf8;
        }

        .container{
            max-width:1200px;
            margin:auto;
            padding:40px;
        }

        .hero{
            background:white;
            padding:50px;
            border-radius:15px;
            text-align:center;
            box-shadow:0 5px 15px rgba(0,0,0,0.1);
        }

        .hero h1{
            color:#0f172a;
            font-size:42px;
            margin-bottom:15px;
        }

        .hero p{
            color:#64748b;
            font-size:18px;
        }

        .status{
            margin-top:20px;
            display:inline-block;
            background:#dcfce7;
            color:#15803d;
            padding:10px 20px;
            border-radius:30px;
            font-weight:bold;
        }

        .cards{
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
            gap:20px;
            margin-top:40px;
        }

        .card{
            background:white;
            padding:25px;
            border-radius:15px;
            box-shadow:0 5px 15px rgba(0,0,0,0.08);
            transition:0.3s;
        }

        .card:hover{
            transform:translateY(-5px);
        }

        .card h3{
            color:#0f172a;
            margin-bottom:10px;
        }

        .card p{
            color:#64748b;
        }

        .footer{
            text-align:center;
            margin-top:50px;
            color:#64748b;
        }
    </style>
</head>

<body>

    <div class="navbar">
        <h2>AttendancePro</h2>
        <div>AWS CI/CD Pipeline Demo</div>
    </div>

    <div class="container">

        <div class="hero">
            <h1>Attendance Management System</h1>

            <p>
                Automated deployment using AWS CodePipeline,
                GitHub, Amazon EC2 and Amazon S3.
            </p>

            <div class="status">
                Deployment Successful ✅
            </div>
        </div>

        <div class="cards">

            <div class="card">
                <h3>👨‍🎓 Students</h3>
                <p>1,250 Registered Students</p>
            </div>

            <div class="card">
                <h3>📚 Courses</h3>
                <p>24 Active Courses</p>
            </div>

            <div class="card">
                <h3>📈 Attendance Rate</h3>
                <p>96.5% Monthly Attendance</p>
            </div>

            <div class="card">
                <h3>⚙️ Deployment</h3>
                <p>Automated through CI/CD Pipeline</p>
            </div>

        </div>

        <div class="footer">
            <h3>Version 1.0</h3>
            <p>AWS DevOps Project - Continuous Integration & Continuous Deployment</p>
        </div>

    </div>

</body>
</html>
"""
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)