Write-host "Ping IP address"

[IPAddress]$IP = read-host "Choose an IP in which to ping"


# En simpel konverter jeg fant som ikke ser ut til å fungere i dette scriptet (blir kluss med if-statement):

#[int]$IP_int = 0
#[bool]$result = [int]::TryParse($IP, [ref]$IP_int)


$pattern = "^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}$"

if ($IP -match $pattern) {

   0..254 | % {"$IP.$($_): $(Test-Connection -count 1 -comp read-host.$($_) -quiet)"}break
}

else
{

"`n ERROR! Please try with a valid IP address."

}

# Dette scriptet printer input som string, og må konverteres til int32 for å fungere.
# Output blir IP adressen + 0-254, istedenfor å gå igjennom hele subnet X.X.X.___
# Den sjekker inputen opp imot pattern for IP adresser, og sender en feilmelding dersom inputen i read-host ikke er en IPv4 adresse.
