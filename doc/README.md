```shell
ln -s .env.example .env

sudo docker-compose up marmot-mysql
sudo docker-compose up -d marmot-mysql
sudo docker-compose stop marmot-mysql
sudo docker-compose rm marmot-mysql

mysql -h127.0.0.1 -uroot -p -P3311
root

ssh admin@49.232.6.131 -p221

# 土拨鼠 marmot
# 土拨鼠堡垒 marmot-fort
# 基石 footstone
# 门石 Gate Stone

# Downloading apps/common/utils/geoip/GeoLite2-City.mmdb (74 MB)
GIT_LFS_SKIP_SMUDGE=1 git clone git@github.com:devops-utils/jumpserver.git
git lfs fetch
git lfs pull
```

```shell
wget https://github.com/jumpserver/jumpserver/releases/download/v2.20.1/quick_start.sh
wget https://github.com/jumpserver/installer/releases/download/v2.20.1/jumpserver-installer-v2.20.1.tar.gz

# 默认会安装到 /opt/jumpserver-installer-v2.20.1 目录
curl -sSL https://github.com/jumpserver/jumpserver/releases/download/v2.20.1/quick_start.sh | bash
cd /opt/jumpserver-installer-v2.20.1

# 安装完成后配置文件 /opt/jumpserver/config/config.txt

cd /opt/jumpserver-installer-v2.20.1

# 启动
./jmsctl.sh start

# 停止
./jmsctl.sh down

# 卸载
./jmsctl.sh uninstall

# 帮助
./jmsctl.sh -h

/opt/jumpserver/config
/opt/jumpserver
```

```
docker exec -it jms_core /bin/bash
cd /opt/jumpserver/apps
python manage.py shell
from users.models import User
u = User.objects.get(username='admin')
u.create_private_token()

u.private_token

curl -H 'Authorization: Token 937b38011acf499eb474e2fecb424ab3' \
     -H "Content-Type:application/json" http://demo.jumpserver.org/api/v1/users/users/
     
# pip install requests
import requests, json

jms_url   = 'https://demo.jumpserver.org'
jms_token = '937b38011acf499eb474e2fecb424ab3'

def get_user_info():
    url      = jms_url + '/api/v1/users/users/'
    headers  = { "Authorization": 'Token ' + jms_token }
    response = requests.get(url, headers=headers)
    print(json.loads(response.text))

get_user_info()


# pip install requests drf-httpsig
import requests, datetime, json
from httpsig.requests_auth import HTTPSignatureAuth

jms_url         = 'https://demo.jumpserver.org'
AccessKeyID     = 'AccessKeyID'
AccessKeySecret = 'AccessKeySecret'
GMT_FORMAT      = '%a, %d %b %Y %H:%M:%S GMT'

def get_auth():
    signature_headers = ['(request-target)', 'accept', 'date']
    auth              = HTTPSignatureAuth(key_id=AccessKeyID, secret=AccessKeySecret, algorithm='hmac-sha256', headers=signature_headers)
    return auth

def get_user_info():
    url     = jms_url + '/api/v1/users/users/'
    auth    = get_auth()
    headers = {
        'Accept': 'application/json',
        'Date': datetime.datetime.utcnow().strftime(GMT_FORMAT)
    }

    response = requests.get(url, auth=auth, headers=headers)
    print(json.loads(response.text))

get_user_info()
```