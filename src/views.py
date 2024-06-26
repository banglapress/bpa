from django.http import HttpResponse


def hello_world(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Active Server</title>
        <style>
            body {
                font-family: "Lucida Console", "Courier New", monospace;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color:black;
            }
            .message {
                text-align: center;
                color:white;
                padding-bottom:30px;
                font-size:38px;              
            }
            .image{
                height:200px;
                weight:200px;
                overflow:hidden;
                padding-left:32px;
            }
            img{
                border-radius:100px;
                height:200px;
                weight:200px;
                object-fit:fill;
            }
            .company{
                text-align:center;
                color:white;
                font-size:24px;
            }
        </style>
    </head>
    <body>
        <div class="content">
            <div class="message">
                DBA Backend!
            </div>
            <div class="image">
                <img src="https://thumbs.dreamstime.com/z/backend-developer-line-icon-linear-style-sign-mobile-concept-web-design-person-working-database-server-outline-vector-310897949.jpg?w=768">
            </div>
            <div class="company">
                <h5>Sahir Zaman</h5>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)