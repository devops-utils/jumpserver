```shell
ln -s .env.example .env

sudo docker-compose up marmot-mysql
sudo docker-compose up -d marmot-mysql
sudo docker-compose stop marmot-mysql
sudo docker-compose rm marmot-mysql

mysql -h127.0.0.1 -uroot -p -P3311
root

ssh admin@49.232.6.131 -p221

cd utils/
sh build_docker.sh v2.20.1
jumpserver/core:v2.20.1
sudo docker-compose -f local.yml run django python manage.py compilemessages
sudo docker build -t "jumpserver/core:v2.20.1" .
sudo docker build -t "jumpserver/lina:v2.20.1" .
sudo docker build -t "jumpserver/web:v2.20.1" -f Dockerfile.web .
/opt/lina/

sudo docker run -ti jumpserver/lina:v2.20.1 sh
sudo docker cp 067b11f6da0f:/opt/lina .

cd /opt/jumpserver-installer-v2.20.1
sudo ./jmsctl.sh restart
sudo ./jmsctl.sh stop
sudo ./jmsctl.sh start

sudo ./jmsctl.sh tail

git pull
sudo docker run -ti --volume="$(pwd)":/jumpserver --rm jumpserver/core:v2.20.1 bash
cd /jumpserver
apt-get update && apt-get install -y gettext
django-admin.py compilemessages
git commit --amend
git reset --soft HEAD^

sudo docker ps

sudo docker exec -it jms_core /bin/bash
cd /opt/jumpserver/apps
python manage.py shell
from users.models import User
u = User.objects.get(username='test')
# u.create_private_token()
# Out[3]: <PrivateToken: 6ad99c651ffdc792859e35844d6a5e15126133cd>
u.private_token
# Out[4]: <PrivateToken: 6ad99c651ffdc792859e35844d6a5e15126133cd>

u = User.objects.get(username='admin')
# u.create_private_token()
# Out[3]: <PrivateToken: fbb421373dcdc2f43ea76877f8ca0e279eaf584c>
u.private_token
# Out[4]: <PrivateToken: fbb421373dcdc2f43ea76877f8ca0e279eaf584c>

# https://marmot.7otech.com/api/v1/perms/users/assets/?offset=0&limit=15&display=1&draw=1

https://marmot.7otech.com/api/docs/

curl 'https://marmot.7otech.com/api/v1/perms/users/assets/?offset=0&limit=15&display=1&draw=1' \
     -H 'Authorization: Token 6ad99c651ffdc792859e35844d6a5e15126133cd' \
     -H 'Content-Type: application/json' \
     -H 'X-JMS-ORG: 00000000-0000-0000-0000-000000000002'

curl -v -X POST https://marmot.7otech.com/api/v1/authentication/sso/login-url/ \
  -H 'Content-Type: application/json' \
  -H "Authorization: Token fbb421373dcdc2f43ea76877f8ca0e279eaf584c" \
  -d '{"username": "test", "next": "/luna/"}'
  
koko/elfinder/sftp/#elf_13d923be4e45994febd3beffff285649_L0RlZmF1bHQvZ2Vub21lL3poYW5ncC9kYXRh

curl -X POST https://marmot.7otech.com/api/v1/authentication/sso/login-url/ \
  -H 'Content-Type: application/json' \
  -H "Authorization: Token fbb421373dcdc2f43ea76877f8ca0e279eaf584c" \
  -d '{"username": "test", "next": "/koko/elfinder/sftp/#elf_13d923be4e45994febd3beffff285649_L0RlZmF1bHQvZ2Vub21lL3poYW5ncC9kYXRh"}'

php -r 'echo base64_decode("L0RlZmF1bHQvZ2Vub21l");'
/Default/genome

saml2
openssl genrsa -out server.key 2048
openssl req -new -x509 -days 3650 -key server.key -out server.crt
openssl req -new -x509 -days 3650 -key server.key -out server.crt -subj "/C=CN/ST=Beijing/L=Beijing/O=yunqiic/OU=yunqiic/CN=7otech.com"  # 这个是证书

sudo docker run -p 8072:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:17.0.1 start-dev

docker exec -it keycloak bash
cd keycloak/bin
./kcadm.sh config credentials --server http://<droplet IP>:8080/auth --realm master --user admin --password {password with upcase etc.}
./kcadm.sh update realms/master -s sslRequired=NONE

cd git/keycloak
openssl req -newkey rsa:2048 -nodes \
  -keyout server.key.pem -x509 -days 3650 -out server.crt.pem
chmod 755 server.key.pem

sudo docker run \
  --name keycloak \
  -e KEYCLOAK_ADMIN=admin \
  -e KEYCLOAK_ADMIN_PASSWORD=admin \
  -e KC_HTTPS_CERTIFICATE_FILE=/opt/keycloak/conf/server.crt.pem \
  -e KC_HTTPS_CERTIFICATE_KEY_FILE=/opt/keycloak/conf/server.key.pem \
  -v $PWD/server.crt.pem:/opt/keycloak/conf/server.crt.pem \
  -v $PWD/server.key.pem:/opt/keycloak/conf/server.key.pem \
  -p 8072:8443 \
  quay.io/keycloak/keycloak:17.0.1 \
  start-dev

docker start 988f9efa76bc
docker stop 988f9efa76bc

http://www.keycloak.org/
docker run -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD='welcome1' -p 8080:8080 jboss/keycloak
docker network create keycloak-network
docker run -d --name postgres --net keycloak-network -e POSTGRES_DB=keycloak -e POSTGRES_USER=keycloak -e POSTGRES_PASSWORD=password postgres
docker run --name keycloak --net keycloak-network jboss/keycloak

http://49.232.6.131:8072
http://49.232.6.131:8072/admin
https://sso-test.7otech.com
https://www.jianshu.com/p/a845cc38abe2

https://marmot.7otech.com/core/auth/login
https://marmot.7otech.com/core/auth/saml2/metadata/ 
keycloak

{
  "organization": {
    "en": {
      "name": "JumpServer",
      "displayname": "JumpServer",
      "url": "https://jumpserver.org/"
    }
  },
  "strict": true,
  "security": {}
}

sudo docker run -d --name=zeus -p 8072:80 -v $pwd/zeus:/data bullteam/zeus-admin:latest
http://49.232.6.131:8072

docker exec -it zeus sh

# 土拨鼠 marmot
# 土拨鼠堡垒 marmot-fort
# 基石 footstone
# 门石 Gate Stone

# Downloading apps/common/utils/geoip/GeoLite2-City.mmdb (74 MB)
GIT_LFS_SKIP_SMUDGE=1 git clone git@github.com:devops-utils/jumpserver.git
git lfs fetch
git lfs pull

docker ps|grep geo
docker stop 3c0c3057b21a
docker stop 39d04bdd48d9
cd SliverWorkspace-2.0.375427/bin
docker-compose down
docker ps|grep jetbrains
docker stop 392438bc4e37

http://docs.jumpserver.org/
http://www.jumpserver.org/support/
https://jumpserver.org/enterprise.html
https://docs.jumpserver.org/zh/master/faq/other/#3-web

Replace (The key generated by MarmotServer)

https://docs.jumpserver.org/zh/master/admin-guide/authentication/sso/
https://docs.jumpserver.org/zh/master/dev/rest_api/

nginx 认证
https://cloud.tencent.com/developer/article/1581440
https://www.cnblogs.com/super-lulu/p/11741591.html
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
https://docs.jumpserver.org/zh/v2.12.0/dev/rest_api/
宁易文创

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

nginx version: nginx/1.20.1
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-44) (GCC)
built with OpenSSL 1.1.1g FIPS  21 Apr 2020 (running with OpenSSL 1.1.1k  FIPS 25 Mar 2021)
TLS SNI support enabled
configure arguments: --prefix=/usr/share/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib64/nginx/modules --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --http-client-body-temp-path=/var/lib/nginx/tmp/client_body --http-proxy-temp-path=/var/lib/nginx/tmp/proxy --http-fastcgi-temp-path=/var/lib/nginx/tmp/fastcgi --http-uwsgi-temp-path=/var/lib/nginx/tmp/uwsgi --http-scgi-temp-path=/var/lib/nginx/tmp/scgi --pid-path=/run/nginx.pid --lock-path=/run/lock/subsys/nginx --user=nginx --group=nginx --with-compat --with-debug --with-file-aio --with-google_perftools_module --with-http_addition_module --with-http_auth_request_module --with-http_dav_module --with-http_degradation_module --with-http_flv_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_image_filter_module=dynamic --with-http_mp4_module --with-http_perl_module=dynamic --with-http_random_index_module --with-http_realip_module --with-http_secure_link_module --with-http_slice_module --with-http_ssl_module --with-http_stub_status_module --with-http_sub_module --with-http_v2_module --with-http_xslt_module=dynamic --with-mail=dynamic --with-mail_ssl_module --with-pcre --with-pcre-jit --with-stream=dynamic --with-stream_ssl_module --with-stream_ssl_preread_module --with-threads --with-cc-opt='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic' --with-ld-opt='-Wl,-z,relro -specs=/usr/lib/rpm/redhat/redhat-hardened-ld -Wl,-E'
```

## Core 参数说明
```shell
SECRET_KEY=****           # 用来加密解密的 KEY
BOOTSTRAP_TOKEN=****      # koko/lion 用来向jms注册使用的 token
DEBUG=TRUE                # 是否开启 debug 模式，显示更多信息  开启以后，界面可以显示API调用信息
SITE_URL= http://1.2.3.4  # 网站的地址，发邮件时使用该地址来做 连接 跳转
LOG_LEVEL=DEBUG           # 日志级别
DB_ENGINE=mysql           # 数据库配置
DB_NAME=jumpserver        # 数据库配置
DB_HOST=127.0.0.1         # 数据库配置
DB_PORT=3306              # 数据库配置
DB_USER=root              # 数据库配置
DB_PASSWORD=****          # 数据库配置
REDIS_HOST=127.0.0.1      # redis 配置
REDIS_PORT=6379           # redis 配置
REDIS_PASSWORD=****       # redis 配置    
REDIS_DB_CELERY=3         # 存放任务相关信息，包括普通 celery 任务（如发送邮件）和 ansible 任务（如测试资产可连接性）
REDIS_DB_CACHE=4          # 存放一些程序中所需的缓存数据（如用户授权资产树结构等）
REDIS_DB_SESSION=5        # 存放用户 session 相关信息
REDIS_DB_WS=6             #  存放 websocket 相关信息
TOKEN_EXPIRATION=86400    # api 生成 token 的有效期  调用API会使用到
SESSION_COOKIE_DOMAIN=None   # session 生效域名，多个 jumpserver 共享 session 时使用
CSRF_COOKIE_DOMAIN=None      # csrftoken 生效域名，多个 jumpserver 共享 session 时使用
SESSION_COOKIE_AGE=86400     # session 有效期  默认界面用户不需要密码自动化登录时间
SESSION_EXPIRE_AT_BROWSER_CLOSE=FALSE  # 关闭浏览器失效登录的 session

# AUTH_OPENID  -  -  查看 Core 配置 AUTH_OPENID 文档
# AUTH_CAS - - 查看 Core 配置 AUTH_CAS 文档

OTP_VALID_WINDOW=2            # OTP/MFA 延迟几次依然有效
OTP_ISSUER_NAME=Jumpserver    # OTP/MFA 扫描后的名称
EMAIL_SUFFIX=jumpserver.org   # 邮箱后缀，ldap 用户时，如果没有邮箱，会用 用户名@默认后缀   

# AUTH_RADIUS  - - 查看 Core 配置 AUTH_RADIUS 文档

AUTH_LDAP_SEARCH_PAGED_SIZE=1000   # LDAP 搜索分页数量
AUTH_LDAP_SYNC_IS_PERIODIC=FALSE   # 是否定时同步 ldap 用户
AUTH_LDAP_SYNC_INTERVAL=None       # 同步间隔（单位：时）（优先）
AUTH_LDAP_SYNC_CRONTAB=None        # 同步 Crontab 表达式

AUTH_LDAP_USER_LOGIN_ONLY_IN_USERS=FALSE   # LDAP 用户登录时仅允许在用户列表中的用户执行 LDAP Server 认证
AUTH_LDAP_OPTIONS_OPT_REFERRALS=-1         # LDAP 认证时如果日志中出现以下信息将参数设置为 0
# In order to perform this operation a successful bind must be completed on the connection (详情参见：https://www.python-ldap.org/en/latest/faq.html) 一般用于LDAP配置正确，但是就是无法登录

# AUTH_LDAP 配置使用 SSL 证书认证  无
# 设置 LDAP 使用证书认证：
# LDAP 配置 SSL 证书（证书文件名及存放位置  JumpServer 部署机：/opt/jumpserver/core/data/certs/ldap_ca.pem ）
# 添加证书好后，JumpServer 会自动发现并使用证书进行认证，不需要额外的配置项。
# 证书需要是 pem 后缀，如果导出的证书为其他类型，请自行 google 转码。

HTTP_BIND_HOST=0.0.0.0           # http 监听 Host
HTTP_LISTEN_PORT=8080            # http 监听端口
WS_LISTEN_PORT=8070              # websocket 监听端口
ASSETS_PERM_CACHE_TIME=86400     # 资产授权缓存时间
SECURITY_MFA_VERIFY_TTL=3600     # 需要 MFA 确认时，确认后多少时间内不用再次确认
ASSETS_PERM_CACHE_ENABLE=FALSE   # 是否启用资产缓存
SYSLOG_ADDR=192.168.0.1          # syslog 的地址，多个地址逗号隔开(,)
SYSLOG_FACILITY=user

PERM_SINGLE_ASSET_TO_UNGROUP_NODE=FALSE  # 单独授权的资产(没有授权其所在节点)将该资产放入到未分组节点下
WINDOWS_SSH_DEFAULT_SHELL=cmd            # windows 支持 ansible 时，使用的 shell
PERIOD_TASK_ENABLED=TRUE                 # (1.5.2之后版本) 启用内部任务  内部自动推送用户，获取资产信息等任务
PERIOD_TASK=TRUE                         # (1.5.2及之前版本) 启用内部任务

LOGIN_LOG_KEEP_DAYS=90                   # 登陆日志保存默认保存时间  登陆日志保存时间，单位天。超过这个时间，后台将自动清理相应的登录信息，即使在页面中设置的审计周期超过对应的的配置参数，也只能查看最近配置（90天）的登录日志。

SECURITY_VIEW_AUTH_NEED_MFA=True         # 查看或导出密码，需要 MFA
SECURITY_LOGIN_CHALLENGE_ENABLED=False   # 登录页面是否开启 CHALLENGE 输入框
SECURITY_LOGIN_CAPTCHA_ENABLED=True      # 登录页面是否开启验证码
AUTH_SSO=False                           # 是否开启其他系统到 JumpServer 的单点登录
AUTH_SSO_AUTHKEY_TTL=900                 # 单点登录 token 有效时长 (单位：秒)
USER_LOGIN_SINGLE_MACHINE_ENABLED=False  # 只允许用户一个浏览器登录
ONLY_ALLOW_AUTH_FROM_SOURCE=False        # 是否仅允许从 用户来源 处登录，默认是 v2.8 添加
ONLY_ALLOW_EXIST_USER_AUTH=False         # 是否仅允许 已创建 的用户登录，如果是，则 ldap 需先导入再登录 v2.8 添加
DISK_CHECK_ENABLED=True                  #  是否开启 硬盘空间监测 v2.8 添加
```

## KoKo 参数说明
```shell
NAME=hostname                    # 默认是主机名
CORE_HOST=http://127.0.0.1:8080  # Jumpserver 项目的 url，api 请求注册会使用
BOOTSTRAP_TOKEN=*****            # 预共享秘钥，请和 jumpserver 配置文件中保持一致。
BIND_HOST=0.0.0.0                # 启动时绑定的 ip, 默认 0.0.0.0
SSHD_PORT=2222                   # 监听的 SSH 端口号
HTTPD_PORT=5000                  # 监听的 HTTP/WS 端口号
# ACCESS_KEY=                    # 项目使用的 ACCESS KEY, 默认会注册,并保存到文件
ACCESS_KEY_FILE=data/keys/.access_key  # ACCESS KEY 保存的地址, 默认注册后会保存到该文件中
LOG_LEVEL=DEBUG                  # 可选 [DEBUG, INFO, WARN, ERROR, FATAL, CRITICAL] debug 模式会自动把用后手动登录填写的密码打印，info 级别不需要
SSH_TIMEOUT=15                   # SSH 连接超时时间(单位=秒)  如果用户服务器启用了 useDNS 这些参数，有可能登录时间超过 15S，需要修改此参数
LANG=zh                          # 可选 [en, zh]  切换 KOKO 登录界面中英文 (v2.0之前的版本)
LANGUAGE_CODE=zh                 # 可选 [en, zh]  切换 KOKO 登录界面中英文 (v2.0之后的版本)
UPLOAD_FAILED_REPLAY_ON_START=true  # 未上传录像遗留文件，启动时是否上传
SFTP_ROOT=/tmp                   # SFTP 的根目录, 可选 /tmp, Home 其他自定义目录  1.5.7起已弃用这个选项，需要在在 core 的系统用户页面上配置
SFTP_SHOW_HIDDEN_FILE=false      # SFTP 是否显示隐藏文件
REUSE_CONNECTION=true            # 是否复用同一用户的 SSH 连接
# ASSET_LOAD_POLICY=all          # all 则用户资产缓存本地搜索分页；默认异步加载资产, 异步搜索分页;   
ZIP_MAX_SIZE=1024M               # web sftp 文件下载，zip 支持压缩的最大额度 (单位=M)
ZIP_TMP_PATH=/tmp                # web sftp 文件下载，zip压缩文件存放的临时目录
CLIENT_ALIVE_INTERVAL=30         # 用户 SSH 登陆 koko 之后，Koko 给 SSH client 发送的心跳间隔，默认 30，0 则表示不发送  保持登陆用户连接不断开
RETRY_ALIVE_COUNT_MAX=3          # 登陆资产之后，Koko 向资产发送心跳包出现错误的重试次数，默认为3。  当网络不稳定时，可以数值可设置大一些。
SHARE_ROOM_TYPE=local            # 可选择 local 和 redis  会话监控和共享使用的方式
REDIS_HOST=127.0.0.1             # redis 配置
REDIS_PORT=6379                  # redis 配置
REDIS_PASSWORD=                  # redis 配置
REDIS_CLUSTERS=                  # redis 配置
REDIS_DB_ROOM=0                  # redis 配置  选择的 redis 库索引
ENABLE_LOCAL_PORT_FORWARD=true   # 是否开启本地转发 (目前仅对 vscode remote ssh 有效果) v2.11 新增
ENABLE_VSCODE_SUPPORT=true       # 是否开启 针对 vscode 的 remote-ssh 远程开发支持 ( 前置条件: 必须开启 ENABLE_LOCAL_PORT_FORWARD ) v2.11 新增。( 注意: vscode 的连接操作，无审计功能 )
```

## lion 参数说明
```shell
NAME=hostname                    # 默认是主机名
CORE_HOST=http://127.0.0.1:8080  # Jumpserver 项目的 url，api 请求注册会使用
BOOTSTRAP_TOKEN=*****            # 预共享秘钥，请和 jumpserver 配置文件中保持一致。
BIND_HOST=0.0.0.0                # 启动时绑定的 ip, 默认 0.0.0.0
HTTPD_PORT=8081                  # 监听的 HTTP/WS 端口号
GUA_HOST=127.0.0.1               # Guacd 项目 url
GUA_PORT=4822                    # Guacd 项目 端口
LOG_LEVEL=DEBUG                  # 可选 [DEBUG, INFO, WARN, ERROR, FATAL, CRITICAL] debug 模式会自动把用后手动登录填写的密码打印，info 级别不需要
SHARE_ROOM_TYPE=local            # 可选择 local 和 redis  会话监控和共享使用的方式
REDIS_HOST=127.0.0.1             # redis 配置
REDIS_PORT=6379                  # redis 配置
REDIS_PASSWORD=                  # redis 配置
REDIS_DB_ROOM=0                  # redis 配置  选择的 redis 库索引

JUMPSERVER_DISABLE_ALL_COPY_PASTE=false             # 全局禁用上传下载
JUMPSERVER_DISABLE_ALL_UPLOAD_DOWNLOAD=false        # 全局禁用剪切板粘贴复制
JUMPSERVER_REMOTE_APP_UPLOAD_DOWNLOAD_ENABLE=false  # 开启Remote app的上传下载
JUMPSERVER_REMOTE_APP_COPY_PASTE_ENABLE=false       # 开启Remote app的剪切板粘贴复制
JUMPSERVER_COLOR_DEPTH=32                    # 颜色深度 低色 16位, 真彩 24位, 真彩 32位
JUMPSERVER_DPI=120                           # 图像每英寸长度内的像素点数 120, 160, 240 等
JUMPSERVER_DISABLE_AUDIO=false               # 禁止声音 true, false  无(允许声音)
JUMPSERVER_ENABLE_WALLPAPER=false            # 启用墙纸 true, false  无（禁用）
JUMPSERVER_ENABLE_THEMING=false              # 启用主题 true, false  无（禁用）
JUMPSERVER_ENABLE_FONT_SMOOTHING=false       # 启用平滑字体 true, false  无（禁用）
JUMPSERVER_ENABLE_FULL_WINDOW_DRAG=false     # 启用拖拽窗口时渲染全部内容 true, false  无（禁用）
JUMPSERVER_ENABLE_DESKTOP_COMPOSITION=false  # 启用透明窗口和阴影等图形效果 true, false  无（禁用）
JUMPSERVER_ENABLE_MENU_ANIMATIONS=false      # 启用菜单开关动画 true, false  无（禁用）
JUMPSERVER_DISABLE_BITMAP_CACHING=true       # 禁用RDP的内置位图缓存功能 true（禁用）, false(启用)  无（启用）
JUMPSERVER_DISABLE_OFFSCREEN_CACHING=true    # 禁用客户端中当前不可见的屏幕区域缓存 true（禁用）, false(启用)  无（启用）
JUMPSERVER_DISABLE_GLYPH_CACHING=true        # 禁用RDP会话中的字形缓存 true（禁用）, false(启用)  无（启用）
JUMPSERVER_CLEAN_DRIVE_SCHEDULE_TIME=1       # 定时清理挂载盘文件的时间间隔 (单位：小时)，如果设置值 0，则不清理。（ v2.13新增 ）
```