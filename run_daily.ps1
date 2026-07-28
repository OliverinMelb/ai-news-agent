# Horizon 每日运行脚本（Windows 任务计划程序调用）
# 注册每日 08:30 运行（管理员不需要，当前用户即可）：
#   schtasks /Create /TN "HorizonDaily" /TR "powershell -NoProfile -ExecutionPolicy Bypass -File C:\Users\admin\Desktop\news\horizon\run_daily.ps1" /SC DAILY /ST 08:30
$ErrorActionPreference = 'Continue'
Set-Location "C:\Users\admin\Desktop\news\horizon"
# Windows 默认 GBK 控制台会让 rich 输出 emoji 时崩溃
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
# 跟随 Windows 当前代理，避免 VPN/Clash 切换端口后定时任务继续使用失效端口
$proxySettings = Get-ItemProperty `
    -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings" `
    -ErrorAction SilentlyContinue
$proxyEndpoint = $null
if ($proxySettings.ProxyEnable -eq 1 -and $proxySettings.ProxyServer) {
    if ($proxySettings.ProxyServer -match "(?:^|;)https=([^;]+)") {
        $proxyEndpoint = $Matches[1]
    } elseif ($proxySettings.ProxyServer -match "(?:^|;)http=([^;]+)") {
        $proxyEndpoint = $Matches[1]
    } elseif ($proxySettings.ProxyServer -notmatch "=") {
        $proxyEndpoint = $proxySettings.ProxyServer
    }
}
if ($proxyEndpoint) {
    if ($proxyEndpoint -notmatch "^https?://") {
        $proxyEndpoint = "http://" + $proxyEndpoint
    }
    $env:HTTP_PROXY = $proxyEndpoint
    $env:HTTPS_PROXY = $proxyEndpoint
}

# 飞书 Webhook 走国内直连
$env:NO_PROXY = "open.feishu.cn," + $env:NO_PROXY

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
