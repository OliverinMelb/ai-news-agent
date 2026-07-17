# Horizon 每日运行脚本（Windows 任务计划程序调用）
# 注册每日 08:30 运行（管理员不需要，当前用户即可）：
#   schtasks /Create /TN "HorizonDaily" /TR "powershell -NoProfile -ExecutionPolicy Bypass -File C:\Users\admin\Desktop\news\horizon\run_daily.ps1" /SC DAILY /ST 08:30
$ErrorActionPreference = 'Continue'
Set-Location "C:\Users\admin\Desktop\news\horizon"
# Windows 默认 GBK 控制台会让 rich 输出 emoji 时崩溃
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
# hnrss.org 直连可用、走 VPN 代理反而 SSL 失败，加入代理豁免
# Reddit/YouTube 经远程 VPN 代理 TLS RESET，本地 Clash 可达；国内站直连
$env:HTTP_PROXY = "http://127.0.0.1:7890"
$env:HTTPS_PROXY = "http://127.0.0.1:7890"
$env:NO_PROXY = "hnrss.org,open.feishu.cn,sspai.com,www.ruanyifeng.com,api.gemai.cc," + $env:NO_PROXY

$logDir = Join-Path $PSScriptRoot "logs"
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir | Out-Null }
$log = Join-Path $logDir ("run-" + (Get-Date -Format "yyyy-MM-dd") + ".log")

& "$PSScriptRoot\.venv\Scripts\horizon.exe" --hours 24 *>> $log
"exit=$LASTEXITCODE $(Get-Date -Format o)" >> $log

# Rebuild static site from summaries and sync to Vercel production
& "$PSScriptRoot\.venv\Scripts\python.exe" "$PSScriptRoot\scripts\build_site.py" *>> $log
Push-Location "$PSScriptRoot\site"
& "$env:APPDATA\npm\vercel.cmd" deploy --prod --yes *>> $log
"site-sync exit=$LASTEXITCODE $(Get-Date -Format o)" >> $log
Pop-Location
