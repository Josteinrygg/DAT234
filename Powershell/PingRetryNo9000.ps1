Write-host "Ping IP address"

$subnet = read-host "Choose an IP in which to ping"

$pattern = "^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}$"


if ($subnet -match $pattern) {

   0..254 | % {"$subnet.$($_): $(Test-Connection -count 1 -comp $subnet.$($_) -quiet 1)"}break
}

else

{
"`n ERROR! Please try with a valid IP address."
}

#Dette er så langt jeg kommer... Koden går igjennom hele subnet, men får feil på parameter -computername (comp).
#Aner ikke hvordan jeg skal skrive for at pipen faktisk skal sjekke connection på inputen. Står "Argument is null or empty": altså -comp.
#Koden skjønner om inputen er en IP adresse (IPv4) eller ikke da, som er ganske nice! Skjekker inputen opp imot angitt pattern.