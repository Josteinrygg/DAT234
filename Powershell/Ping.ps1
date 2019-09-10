1..255 | % {"192.168.100.$($_): $(Test-Connection -count 1 -comp 192.168.100.$($_) -quiet)"}
