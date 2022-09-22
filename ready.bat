@echo off
chcp 65001
title 正在安装依赖
python  --version
if errorlevel 1 (
	echo 您未安装python或pip，快去官网下一个吧！
	pause
	goto end
)

pip --version
if errorlevel 1 (
	echo 您未安装python或pip，快去官网下一个吧！
	pause
	goto end
)

echo 确认python与pip已安装

pip install -r requirements.txt
echo 依赖安装完毕，若未提示error，接下来请运行run.bat
:end
pause