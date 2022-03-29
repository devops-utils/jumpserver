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
```