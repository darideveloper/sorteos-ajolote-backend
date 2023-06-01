<div><a href='https://github.com/github.com/darideveloper/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/github.com/darideveloper.svg?style=for-the-badge' alt='MIT License' height='30px'/>
        </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper?up_rollout=true' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://github.com/darideveloper/sorteos-ajolote-frontend/blob/master/public/logo.png?raw=true' alt='Sorteos Ajolote Backend' height='80px'/>

# Sorteos Ajolote Backend

Django dashboard for manage lotteries of page Sorteos Ajolote.

Start date: **2023-05-16**

Last update: **2023-05-20**

Project type: **client's project**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#relatedprojects'>Related Projects</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#details'>Details</a></li>
<li><a href='#roadmap'>Roadmap</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a><a href='https://www.postgresql.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/postgresql.svg' alt='PostgreSQL' title='PostgreSQL' height='50px'/> </a><a href='https://aws.amazon.com/es/s3/' target='_blank'> <img src='https://cdn.svgporn.com/logos/aws-s3.svg' alt='AWS S3' title='AWS S3' height='50px'/> </a><a href='https://docs.djangoproject.com/en/4.0/' target='_blank'> <img src='https://cdn.svgporn.com/logos/django.svg' alt='Django' title='Django' height='50px'/> </a></div>

# Related projects

<div align='center'><a href='https://github.com/darideveloper/sorteos-ajolote-frontend' target='_blank'> <img src='https://github.com/darideveloper/sorteos-ajolote-frontend/blob/master/public/logo.png?raw=true' alt='Sorteos Ajolote Frontend' title='Sorteos Ajolote Frontend' height='50px'/> </a></div>

# Media

![home](https://github.com/darideveloper/sorteos-ajolote-backend/blob/master/screenshots/home.png?raw=true)

![lottery form](https://github.com/darideveloper/sorteos-ajolote-backend/blob/master/screenshots/lottery-form.png?raw=true)

![ticket form](https://github.com/darideveloper/sorteos-ajolote-backend/blob/master/screenshots/ticket-form.png?raw=true)

# Details

## Models

The project have the models **Lottery** (to save the lotteries data, like name, total price, numbers, etc).
And **Ticket** to save the Tickets selected by the clients. 

Both models are available in the Admin Dashboard.

## Endpoints

* **get-lotteries**: GET data of the current lotteries. 
* **save-tickets**: POST ticket(s) selected by the users

# Roadmap

- [x] Models in admin 
- [x] Enpoints to query lotteries
- [x] Endpoint to save tickets
- [x] Save images in S3
- [x] Views tests
- [x] Cron for disable olt tickets no payed 
- [ ] Customize dashboard colors]


