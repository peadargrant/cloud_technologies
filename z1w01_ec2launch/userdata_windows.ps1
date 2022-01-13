<powershell>
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service -Name sshd -StartupType automatic

Install-WindowsFeature -name Web-Server -IncludeManagementTools

Restart-Computer -Force

</powershell>

