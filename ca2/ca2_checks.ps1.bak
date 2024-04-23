#!/usr/bin/env pwsh
# CA2 checks file
# Peadar Grant

$Files = @( "plan.txt", "system.yaml", "setup.py", "teardown.py" )

$problems = $false
Write-Host "CA1 checks" -ForegroundColor Yellow
Foreach ( $File in $Files ) {
    Write-Host "checking for $File ... " -NoNewline
    If ( ! (Test-Path $File) ) {
	Write-Host "not found" -ForegroundColor Red
	$problems = $true
#	return
    }
    Else {
	Write-Host "found" -ForegroundColor Green
    }
}

if ( $problems ) {
    Write-Host "fix identified problems and re-run checks!" -ForegroundColor Yellow
}
Else {
    Write-Host "all required files present - ready to submit!" -ForegroundColor Green
}
