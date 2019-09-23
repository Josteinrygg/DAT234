Write-Host "Choose function"

[int]$EType = read-host "Please type 1 to ping range 192.168.100.15/24 or type 2 for pingsweep!"

if ($EType -eq 1)
{
$a = 15
$z = 24
while ($a -le $z) {
    Test-Connection -computername "192.168.100.$a" -Quiet -count 1
        $a++
} 

"Checked range from 15 to 24!"

break

}

if ($EType -eq 2)
{
    0..254 | % {"192.168.100.$($_): $(Test-Connection -count 1 -comp 192.168.100.$($_) -quiet)"}

"Pingsweep in subnet complete!"
}


