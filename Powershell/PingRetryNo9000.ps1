Write-host "Ping IP address"

$subnet = read-host "Choose an IP in which to ping"

$pattern = "^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}$"

if ($subnet -match $pattern) {

   0..254 | % {"$subnet.$($_): $(Test-Connection -count 1 -comp read-host.$($_) -quiet)"}break
}

else

{
"`n ERROR! Please try with a valid IP address."
}
